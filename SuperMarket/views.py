from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

#Se crea una funcion para cada pagina
def inicio(request):
    return render(request, "login.html")

def productos(request):
    return render(request, "productos.html")