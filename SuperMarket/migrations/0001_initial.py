# Generated by Django 4.1 on 2022-09-21 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Clientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveCliente', models.CharField(max_length=10)),
                ('nombreProducto', models.CharField(max_length=80)),
                ('apellidoPaterno', models.CharField(max_length=80)),
                ('apellidoMaterno', models.CharField(max_length=80)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('membresia', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveDepartamento', models.CharField(max_length=10)),
                ('nombreDepartamento', models.CharField(max_length=50)),
                ('empleadoResponsable', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveEmpleado', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('apellidoPaterno', models.CharField(max_length=80)),
                ('apellidoMaterno', models.CharField(max_length=80)),
                ('edad', models.IntegerField()),
                ('fechaNacimiento', models.DateField()),
                ('cargo', models.CharField(max_length=80)),
                ('area', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('claveProducto', models.CharField(max_length=10)),
                ('nombre', models.CharField(max_length=80)),
                ('departamento', models.CharField(max_length=80)),
                ('tipo', models.CharField(max_length=80)),
                ('marca', models.CharField(max_length=60)),
                ('unidadMedida', models.CharField(max_length=30)),
                ('fechaCaducidad', models.DateField()),
                ('stock', models.IntegerField()),
            ],
        ),
    ]
