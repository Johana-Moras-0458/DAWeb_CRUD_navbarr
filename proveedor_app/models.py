from django.db import models

class Proveedor(models.Model):
    idproveedor=models.CharField(primary_key=True, max_length=6)
    idpeluche=models.CharField(max_length=6)
    nombre=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    precio=models.FloatField()
    horarios=models.CharField(max_length=20)

def __str__(self):
    return self.nombre

