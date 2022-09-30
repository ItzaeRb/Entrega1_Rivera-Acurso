from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from platformdirs import user_cache_dir

# se crean los formularios nuevos.



class Form_clientes(forms.Form):
    claveCliente = forms.CharField()
    nombreProducto = forms.CharField()
    apellidoPaterno = forms.CharField()
    apellidoMaterno = forms.CharField()
    edad = forms.IntegerField()
    fechaNacimiento = forms.DateTimeField()
    email = forms.EmailField()
    membresia = forms.CharField()

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget= forms.PasswordInput)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_text = {k:"" for k in fields}
        
    