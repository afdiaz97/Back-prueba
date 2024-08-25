from django.db import models
# Create your models here.
class Cliente(models.Model):
    # Aquí puedes agregar campos adicionales si lo deseas
    cedula = models.BigIntegerField("Cedula",primary_key=True)
    nombre = models.CharField("Nombre", max_length=50)
    email = models.EmailField("correo")
    direccion= models.CharField("Direccion")
    telefono= models.BigIntegerField("Telefono")
    def __str__(self):
        return self.nombre