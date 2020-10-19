from django.db import models

# Create your models here.

class Autos(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    año= models.IntegerField()
    cilindraje= models.IntegerField()
    cantidad_bodega= models.IntegerField()
    

    def __str__ (self):
        return self.marca