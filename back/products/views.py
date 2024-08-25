from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Producto
import logging

logger = logging.getLogger(__name__)


class Productos(APIView):
    def post(self, request):
        try:
            codigo = request.data["codigo"]
            nombre = request.data["nombre"]
            valor = request.data["valor"]
            iva = request.data["iva"]
            valoriva = request.data.get("porcentaje_iva", None)
            if not isinstance(valor, (int, float)):
                return Response({"mensaje": "El campo 'valor' debe ser numérico."}, status=400)
            if not isinstance(iva, bool):
                return Response({"mensaje": "El campo 'iva' debe ser booleano (True o False)."}, status=400)
            if iva and (valoriva is None or not isinstance(valoriva, (int, float))):
                return Response({"mensaje": "Si 'iva' es True, 'porcentaje_iva' debe ser numérico."}, status=400)        
        except KeyError as e:
            return Response({"mensaje": f"Por favor ingrese el parámetro {e}"}, status=400)
        try:
            producto=Producto.objects.create(
                Codigo=codigo,
                nombre=nombre,
                valor=valor,
                iva=iva,
                valor_iva=valoriva
            )
            return Response({"mensaje":"Se creo el producto correctamete","producto":producto.Codigo},status=201)
        except Exception as e:
            logger.exception("Error creando producto")
            return Response({"mensaje":"No fue posible crear el producto"},status=500)
