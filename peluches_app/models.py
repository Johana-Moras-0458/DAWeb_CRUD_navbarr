from django.db import models

class Peluche(models.Model):
    idpeluche=models.CharField(primary_key=True,max_length=6)
    idproveedor=models.CharField(max_length=6)
    nombre=models.CharField(max_length=20)
    color=models.CharField(max_length=20)
    tamaño=models.CharField(max_length=50)
    precio=models.FloatField()
    tipotela=models.CharField(max_length=20)
    idsucursal=models.CharField(max_length=6)

def __str__(self):
    return self.nombre

