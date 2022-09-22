from django.db import models

# Create your models here.
class Productos(models.Model):
    claveProducto = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    departamento = models.CharField(max_length=80)
    tipo = models.CharField(max_length=80)
    marca = models.CharField(max_length=60)
    unidadMedida = models.CharField(max_length=30)
    fechaCaducidad = models.DateField()
    stock = models.IntegerField()

    #esta def es para mostrar los datos en la web
    def __str__(self):
        return f"Clave:{self.claveProducto}, Nombre: {self.nombre}, Departamento: {self.departamento}, Tipo: {self.tipo}, Marca: {self.marca}, Unidad de medida: {self.unidadMedida}, Fecha de caducidad:{self.fechaCaducidad}, Stock: {self.stock}"

    

class Empleados(models.Model):
    claveEmpleado = models.CharField(max_length=10)
    nombre = models.CharField(max_length=80)
    apellidoPaterno = models.CharField(max_length=80)
    apellidoMaterno = models.CharField(max_length=80)
    edad= models.IntegerField()
    fechaNacimiento = models.DateField()
    cargo = models.CharField(max_length=80)
    area = models.CharField(max_length=80)

class Clientes(models.Model):
    claveCliente = models.CharField(max_length=10)
    nombreProducto = models.CharField(max_length=80)
    apellidoPaterno = models.CharField(max_length=80)
    apellidoMaterno = models.CharField(max_length=80)
    edad = models.IntegerField()
    fechaNacimiento = models.DateField()
    email = models.EmailField()
    membresia = models.BooleanField()

class Departamento(models.Model):
    claveDepartamento = models.CharField(max_length=10)
    nombreDepartamento = models.CharField(max_length=50)
    empleadoResponsable = models.CharField(max_length=80)
    


