from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
from .serializers import ClienteSerializer

import logging

logger = logging.getLogger(__name__)


class UserLoginView(APIView):
    def post(self, request):
        try:
            user = authenticate(username=request.data['username'], password=request.data['password'])
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key},status=200)
            else:
                return Response({'error': 'Invalid credentials'}, status=401)
        except KeyError:
            return Response({"mensaje":"Error,revisar username y password"},status=400)
        
class Clientes(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request):
        try:
            nombre=request.data["nombre"]
            direccion=request.data["direccion"]
            telefono=request.data["telefono"]
            cedula=request.data["cedula"]
            email=request.data["email"]
        except KeyError as e:
            return Response({"menaaje":f"Por favor ingresar el parametro {e}"},status=400)
        try:
            user=Cliente.objects.create(
                nombre=nombre,
                direccion=direccion,
                telefono=telefono,
                cedula=cedula,
                email=email
            )
            return Response({"Mensaje":"usuario creado correctamente","usuario":user.cedula},status=201)
        except:
            logging.exception("error en la creacion del usuario")
            return Response({"Mensaje":"No fue posible crear el usuario"},status=500)
    def get(self,request):
        try:
            clientes=Cliente.objects.all()
            serializer=ClienteSerializer(clientes, many=True)
            return Response(serializer.data,status=200)
        except Exception as e:
            logger.exception("Error obteniendo los clientes")
            return Response({"Mensaje":"No fue posible obtener los clientes"},status=500)
        


