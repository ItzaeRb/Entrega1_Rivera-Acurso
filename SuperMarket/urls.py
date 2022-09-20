from django.urls import path
from SuperMarket.views import * 

urlpatterns = [
    path('', inicio),
    path('productos/', productos)
]
