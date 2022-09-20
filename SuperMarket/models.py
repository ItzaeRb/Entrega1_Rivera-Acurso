from django.db import models

# Create your models here.
class Productos(models.Model):
    nombre = models.CharField(max_length=80)
    clave = models.CharField(max_length=10)
    categoria = models.CharField(max_length=80)
    tipo = models.CharField(max_length=80)
    marca = models.CharField(max_length=60)
    unidadMedida = models.CharField(max_length=30)
    fechaCaducidad = models.DateField()
    stock = models.IntegerField()