from django.urls import path
from SuperMarket.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('create_productos/', productos),
    path('read_productos/', read_productos),
]
