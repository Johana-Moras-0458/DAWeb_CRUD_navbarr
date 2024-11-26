from django.db import models

class Cliente(models.Model):
    idcliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=10)
    apellido=models.CharField(max_length=10)
    direccion=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    telefono=models.CharField(max_length=10)
    fecharegistro=models.DateField()
    def __str__(self):
        return self.nombre
