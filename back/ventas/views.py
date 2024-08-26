from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Venta,Detail_venta
from products.models import Producto
from usuarios.models import Cliente
from django.db import IntegrityError
from .serializers import VentaSerializer

import logging

logger = logging.getLogger(__name__)

class Ventas(APIView):
    def post(self,request):
        try:
            cliente=request.data["cliente"]
        except KeyError as e:
            return Response({"mensaje": f"Por favor ingrese el parámetro {e}"}, status=400)
        try:
            cliente=Cliente.objects.get(cedula=cliente)
        except Cliente.DoesNotExist:
            return Response({"mensaje": f"No se encontro el cliente"}, status=400)
        except Exception as e:
            logger.exception("Error")
            return Response({"mensaje": f"No se pudo registrar la venta"}, status=500)
        try:
            venta=Venta.objects.create(cliente=cliente,total_venta=0)
            return Response({"mensaje":"Se registro la venta","id_venta":venta.id_vents},status=201)
        except Exception as e:
            logger.exception("Error")
            return Response({"mensaje": f"No se pudo registrar la venta"}, status=500)
    def get(self,request):
        try:
            ventas=Venta.objects.all()
            ventas=VentaSerializer(ventas,many=True)
            return Response(ventas.data,status=200)
        except Exception as e:
            logger.exception("Error")
            return Response({"mensaje": f"Ocurrio un error al obtener los datos"}, status=500)


class Addventa(APIView):
    def post(self,request):
        try:
            venta=request.data["venta"]
            producto=request.data["producto"]
        except KeyError as e:
            return Response({"mensaje": f"Por favor ingrese el parámetro {e}"}, status=400)   
        try:
            venta=Venta.objects.get(id_vents=venta)
        except Venta.DoesNotExist:
            return Response({"mensaje": f"No se encuentra una venta registrada con este id{venta}"}, status=400)  
        except Exception as e:
             return Response({"mensaje": f"No se pudo registrar el detalle de la venta"}, status=500)
        try:
            producto=Producto.objects.get(Codigo=producto)
        except Producto.DoesNotExist:
            return Response({"mensaje": f"No se encuentra el producto registrado con el codigo{producto}"}, status=400)  
        except Exception as e:
             return Response({"mensaje": f"No se pudo registrar el detalle de la venta"}, status=500)
        try:
            iva=calculos_venta(producto,venta)
            detail=Detail_venta.objects.create(venta=venta,producto=producto,valor_producto=producto.valor,iva_calculado=iva)
            return Response({"mensaje":"Se registro el detalle de la venta","id_venta":detail.iva_calculado},status=201)
        except Exception as e:
            logger.exception("Error")
            return Response({"mensaje": f"No se pudo registrar el detalle de la venta"}, status=500)
            
def calculos_venta(producto,venta):
    try:
        if producto.iva:
            valoriva=producto.valor_iva
        else:
            valoriva=0
        total=producto.valor+(valoriva*producto.valor)/100 
        venta.total_venta += venta.total_venta+total
        venta.save()
        return (valoriva*producto.valor)/100 
    except Exception as e:
            logger.exception("Error")

