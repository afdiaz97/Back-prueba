from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .models import Cliente
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
            username=request.data["username"]
            first_name=request.data["first_name"]
            last_name=request.data["last_name"]
            direccion=request.data["direccion"]
            telefono=request.data["telefono"]
            cedula=request.data["cedula"]
            password=request.data["password"]
        except KeyError as e:
            return Response({"mesnaje":f"Por favor ingresar el parametro {e}"},status=400)
        try:
            user=Cliente.objects.create(
                username=username,
                first_name=first_name,
                last_name=last_name,
                direccion=direccion,
                telefono=telefono,
                cedula=cedula
            )
            user.set_password(password)
            user.save()
            return Response({"Mensaje":"usuario creado correctamente","username":user.username},status=201)
        except:
            logging.exception("error en la creacion del usuario")
            return Response({"Mensaje":"No fue posible crear el usuario"},status=500)
        


