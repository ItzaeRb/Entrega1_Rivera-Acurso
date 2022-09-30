import email
from django.shortcuts import render
from django.http import HttpResponse
from SuperMarket.models import *
from SuperMarket.forms import *

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
# Create your views here.

#Se crea una funcion para cada pagina
def inicio(request):
    return render(request, "home.html")

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


# def para crear formulario de clientesinformacion
def api_clientes(request):
    if request.method == "POST":
        formulario = Form_clientes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente = Clientes(claveCliente = informacion["claveCliente"],
                           nombreProducto = informacion["nombreProducto"],
                           apellidoPaterno = informacion["apellidoPaterno"],
                           apellidoMaterno = informacion["apellidoMaterno"],
                           edad = informacion["edad"],
                           fechaNacimiento = informacion["fechaNacimiento"],
                           email = informacion["email"],
                           membresia = informacion["membresia"]
                           )
            cliente.save()
            return render(request, "api_clientes.html")
    else:
        formulario = Form_clientes()
    return render(request, "api_clientes.html", {"formulario": formulario})


def buscar_clientes(request):
    if request.GET["claveCliente"]:
        claveCliente = request.GET["claveCliente"]
        clientes = Clientes.objects.filter(claveCliente__icontains = claveCliente)
        return render(request, "buscar_clientes.html", {"clientes": clientes})
    else:
        respuesta = "No se enviaron los datos"
    return HttpResponse(respuesta)

def delete_clientes(request, cliente_id):
    cliente = Clientes.objects.get(id = cliente_id)
    cliente.delete()
    clientes = Clientes.objects.all()
    return render(request, "read_clientes.html", {"clientes":clientes})

def update_clientes(request, cliente_id):
    cliente = Clientes.objects.get(id = cliente_id)
    if request.method == "POST":
        formulario = Form_clientes(request.POST)
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            cliente.claveCliente = informacion["claveCliente"]
            cliente.nombreProducto = informacion["nombreProducto"]
            cliente.apellidoPaterno = informacion["apellidoPaterno"]
            cliente.apellidoMaterno = informacion["apellidoMaterno"]
            cliente.edad = informacion["edad"]
            cliente.fechaNacimiento = informacion["fechaNacimiento"]
            cliente.email = informacion["email"]
            cliente.membresia = informacion["membresia"]
            cliente.save()
            clientes = Clientes.objects.all() #Trae todo
            return render(request, "read_clientes.html", {"clientes": clientes})
    else:
        formulario = Form_clientes(initial={"claveCliente":cliente.claveCliente,
                                            "nombreProducto":cliente.nombreProducto,
                                            "apellidoPaterno":cliente.apellidoPaterno,
                                            "apellidoMaterno":cliente.apellidoMaterno,
                                            "edad":cliente.edad,
                                            "email":cliente.email,
                                            "membresia":cliente.membresia,
                                            })
    return render(request, "update_clientes.html", {"formulario":formulario})

def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            user = form.cleaned_data.get("username")
            pwd = form.cleaned_data.get("password")
            user = authenticate(username = user, password = pwd)
            if user is not None:
                login(request, user)
                return render(request, "home.html")
            else:
                return render(request, "login.html", {"form": form})
        return render(request, "login.html", {"form": form})
    form = AuthenticationForm()
    return render(request, "login.html", {"form":form})

