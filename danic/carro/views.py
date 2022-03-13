from itertools import product
from django.shortcuts import render
from django.shortcuts import redirect

# Importacion de la clase carro
from .carro import Carro
# Importacion del modelo del producto
from ventas.models import Producto


# Agregar un producto
def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.agregar(producto = producto)

    return redirect("home")


# Eliminar un producto
def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.eliminar(producto = producto)

    return redirect("home")


# Restar cantidad de un producto
def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id = producto_id)
    carro.restar_producto(producto = producto)

    return redirect("home")


# limpiar un producto
def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()

    return redirect("home")



