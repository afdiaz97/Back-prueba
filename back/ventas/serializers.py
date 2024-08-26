from rest_framework import serializers
from .models import Venta,Detail_venta
from usuarios.models import Cliente
from products.models import Producto

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = ['nombre']

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['nombre','valor']
class VentaSerializer(serializers.ModelSerializer):
    cliente = ClienteSerializer()  # Usa el serializer del cliente

    class Meta:
        model = Venta
        fields = ['id_vents', 'fecha', 'cliente', 'total_venta']

class DetailSerializer(serializers.ModelSerializer):
    producto = ProductoSerializer()  # Usa el serializer del cliente

    class Meta:
        model = Detail_venta
        fields = ['producto', 'valor_producto', 'iva_calculado']