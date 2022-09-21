from django.contrib import admin

from SuperMarket.models import *

# Register your models here.

admin.site.register(Productos)
admin.site.register(Empleados)
admin.site.register(Clientes)
admin.site.register(Departamento)

