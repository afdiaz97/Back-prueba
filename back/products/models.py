from django.db import models

class Producto(models.Model):
    Codigo=models.CharField("codigo",primary_key=True)
    nombre=models.CharField("nombre")
    valor=models.DecimalField(max_digits=10, decimal_places=2)
    iva=models.BooleanField("Tiene iva")
    valor_iva=models.DecimalField(max_digits=4, decimal_places=2 , null=True)
    def __str__(self):
        return self.codigo + " "+self.nombre
