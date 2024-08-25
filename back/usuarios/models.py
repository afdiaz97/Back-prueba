from django.contrib.auth.models import AbstractUser
from django.db import models
# Create your models here.
class Cliente(AbstractUser):
    # Aquí puedes agregar campos adicionales si lo deseas
    cedula = models.BigIntegerField("Cedula")
    direccion= models.CharField("Direccion")
    telefono= models.BigIntegerField("Telefono")
    def __str__(self):
        return self.username