from django.db import models

# Create your models here.

class Clientes (models.Model):
    codigo = models.CharField(max_length= 50)
    nombre = models.CharField(max_length= 50)
    apellidos = models.CharField(max_length=50)
    direccion = models.CharField(max_length= 100)
    poblacion = models.CharField(max_length=100)
    codigo_postal= models.CharField(max_length= 50)
    provincia = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_nacimiento= models.DateField()


    def __str__(self):
        return self.codigo
