from django.db import models
from usuarios.models import Cliente
from products.models import Producto
from datetime import datetime 
# Create your models here.
class Venta(models.Model):
    id_vents=models.BigAutoField("numero_venata",primary_key=True)
    fecha=models.DateTimeField("fecha",default=datetime.now())
    cliente=models.ForeignKey(Cliente,on_delete=models.CASCADE)
    total_venta=models.DecimalField("Total venta", max_digits=10, decimal_places=2)

class Detail_venta(models.Model):
    venta=models.ForeignKey("Venta", on_delete=models.CASCADE)
    producto=models.ForeignKey(Producto, on_delete=models.CASCADE)
    valor_producto=models.DecimalField("Valor producto", max_digits=10, decimal_places=2)
    iva_calculado=models.DecimalField("Iva calculado", max_digits=10, decimal_places=2)
