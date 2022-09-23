from django.urls import path
from SuperMarket.views import * 

urlpatterns = [
    path('', inicio),
    path('inicio/', inicio),
    path('create_productos/', create_productos),
    path('read_productos/', read_productos),
    path('buscar_producto/', buscar_producto),
    path('create_empleados/', create_empleados),
    path('read_empleados/', read_empleados), 
    path('create_clientes/', create_clientes),
]
