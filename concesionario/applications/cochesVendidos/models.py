from django.db import models
from applications.cliente.models import Clientes

# Create your models here.
class CochesVendidos (models.Model):
    matricula = models.CharField(max_length= 20)
    marca = models.CharField(max_length= 20)
    modelo = models.IntegerField()
    color = models.CharField(max_length= 20)
    precio = models.FloatField()
    extras_instalados= models.CharField(max_length= 100)
    codigo_cliente = models.ForeignKey(Clientes, on_delete=models.CASCADE)
    numero_puertas = models.IntegerField()
    


    def __str__(self):
        return self.matricula
