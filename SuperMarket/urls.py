from django.urls import path
from SuperMarket.views import * 
from SuperMarket.forms import Form_clientes

urlpatterns = [
    path('', inicio),
    path('inicio/', inicio),
    path('create_productos/', create_productos),
    path('read_productos/', read_productos),
    path('buscar_producto/', buscar_producto),
    path('create_empleados/', create_empleados),
    path('read_empleados/', read_empleados), 
    path('create_clientes/', create_clientes),
    path('read_clientes/', read_clientes),
    path('api_clientes/', api_clientes),
    path('buscar_clientes/', buscar_clientes),
    path("delete_clientes/<cliente_id>", delete_clientes),
    path("update_clientes/<cliente_id>", update_clientes),
    path('login/', login_request),
    path('registro/', registro),
]
