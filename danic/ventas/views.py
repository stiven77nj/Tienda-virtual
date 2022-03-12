from django.shortcuts import render

# Importacion del modelo producto
from .models import Producto

# Vista de la pagina home
def home(request):
    productos = Producto.objects.all() # Transforma las instancias a una lista
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/home.html', data)

# Vista de la pagina de contacto
def contacto(request):
    return render(request, 'ventas/contacto.html')