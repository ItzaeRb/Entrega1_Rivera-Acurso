from django.shortcuts import render
from django.http import HttpResponse
from SuperMarket.models import *


# Create your views here.

#Se crea una funcion para cada pagina
def inicio(request):
    return render(request, "login.html")

def productos(request):
    return render(request, "create_productos.html")

def create_productos(request):
    if request.method == 'POST':
        producto = Productos(claveProducto = request.POST['claveProducto'], nombre = request.POST['nombreProducto'], departamento = request.POST['departamento'], tipo = request.POST['tipo'], marca = request.POST['marca'], unidadMedida = request.POST['unidadMedida'], fechaCaducidad = request.POST['fechaCaducidad'], stock = request.POST['stock'])
        producto.save()
        productos = Productos.objects.all()    
        return render(request, "read_productos.html", {"productos": productos})
    return render(request, "create_productos.html")

def create_clientes(request):
    if request.method == "POST":
        cliente = Clientes(claveCliente = request.POST["claveCliente"],
                           nombreProducto = request.POST["nombreProducto"],
                           apellidoPaterno = request.POST["apellidoPaterno"],
                           apellidoMaterno = request.POST["apellidoMaterno"],
                           edad = request.POST["edad"],
                           fechaNacimiento = request.POST["fechaNacimiento"],
                           email = request.POST["email"],
                           membresia = request.POST["membresia"]
                           )
        cliente.save()
        clientes = Clientes.objects.all()
        return render(request, "read_clientes.html", {"clientes": clientes} )
    return render(request, "create_clientes.html" )


def read_clientes(request):
    clientes = Clientes.objects.all() #Trae todo
    return render(request, "read_clientes.html", {"clientes": clientes})

    
def read_productos(request):
    productos = Productos.objects.all() #Trae todo
    return render(request, "read_productos.html", {"productos": productos})


def create_empleados(request):
    if request.method == 'POST':
        empleado = Empleados(claveEmpleado = request.POST['claveEmpleado'], nombre = request.POST['nombreEmpleado'], apellidoPaterno = request.POST['apellidoPaterno'], apellidoMaterno = request.POST['apellidoMaterno'], edad = request.POST['edad'], fechaNacimiento = request.POST['fechaNacimiento'], cargo = request.POST['cargo'], area = request.POST['area'])
        empleado.save()
        empleados = Empleados.objects.all()    
        return render(request, "read_empleados.html", {"empleados": empleados})
    return render(request, "create_empleados.html")

def read_empleados(request):
    empleados = Empleados.objects.all() #Trae todo
    return render(request, "read_empleados.html", {"empleados": empleados})

#AÑADIR LAS DEF PARA CREAR Y MOSTRAR CLIENTES Y EMPLEADOS

def buscar_producto(request):
    if request.GET["nombre"]:
        nombre = request.GET["nombre"]
        productos = Productos.objects.filter(nombre__icontains = nombre) 
        return render(request, "buscar_producto.html", {"productos": productos})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)