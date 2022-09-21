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
        producto = Productos(nombre = request.POST['nombre'], apellido = request.POST['apellido'], email = request.POST['email'])
        producto.save()
        productos = Productos.objects.all()    
        return render(request, "estudiantesCRUD/read_productos.html", {"productos": productos})
    return render(request, "estudiantesCRUD/create_productos.html")