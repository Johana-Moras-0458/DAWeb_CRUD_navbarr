from django.db import models

class Empleado(models.Model):
    idempleado=models.CharField(primary_key=True, max_length=6)
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    telefono=models.CharField(max_length=10)
    salario=models.FloatField()
    horario=models.CharField(max_length=20)
    direccion=models.CharField(max_length=50)

def __str__(self):
    return self.nombre

