from distutils.command.upload import upload
from random import choices
from secrets import choice
from django.db import models
from django.forms import IntegerField

# Create your models here.

# Modelo para la Marca
class Marca(models.Model):
    # El id lo pone django
    nombre = models.CharField(max_length=50)

    # ToString
    def __str__(self):
        return self.nombre

# Modelo para el Producto
class Producto(models.Model):
    # El id lo pone django
    nombre = models.CharField(max_length=100)
    precio = models.FloatField()
    descripcion = models.TextField()
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT) # Foreign Key
    imagen = models.ImageField(upload_to="productos", null=True) # Las imagenes se guardan en la subcarpeta productos y no en la base de datos

    # ToString
    def __str__(self):
        return self.nombre

# Opciones para la consulta
opciones_consulta = [
    [0, "Consulta"],
    [1, "Reclamo"],
    [2, "Sugerencia"],
    [3, "Felicitaciones"]
]

# Modelo para el formulario de Contacto
class Contacto(models.Model):
    nombre = models.CharField(max_length=50)
    correo = models.EmailField()
    tipo_consulta = models.IntegerField(choices=opciones_consulta)
    mensaje = models.TextField()
    avisos = models.BooleanField()

    # ToString
    def __str__(self):
        return self.nombre
    
