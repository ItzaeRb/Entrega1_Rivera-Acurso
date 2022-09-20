from django.urls import path
from SuperMarket.views import * 

urlpatterns = [
    path('inicio/', inicio),
    path('productos/', productos)
]
