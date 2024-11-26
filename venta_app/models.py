from django.db import models

class Ventas(models.Model):
    idventa=models.CharField(primary_key=True, max_length=6)
    idempleado=models.CharField(max_length=10)
    idproducto=models.CharField(max_length=10)
    idcliente=models.CharField(max_length=10)
    idsucursal=models.CharField(max_length=10)
    total=models.FloatField()
    fechacompra=models.DateField()

def __str__(self):
    return (self).nombre 
