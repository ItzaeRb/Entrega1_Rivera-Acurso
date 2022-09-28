from django import forms

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