from rest_framework import serializers
from .models import Venta
from usuarios.models import Cliente

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre']

class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  # Usa el serializer del cliente

    class Meta:
        model = Venta
        fields = ['id_vents', 'fecha', 'cliente', 'total_venta']
