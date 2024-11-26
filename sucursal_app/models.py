from django.db import models

class Sucursal(models.Model):
    idsucursal=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    idempleado=models.CharField(max_length=6)
    horario=models.CharField(max_length=20)
    correo=models.CharField(max_length=50)