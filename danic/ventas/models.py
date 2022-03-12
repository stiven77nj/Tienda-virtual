from distutils.command.upload import upload
from django.db import models

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
    
