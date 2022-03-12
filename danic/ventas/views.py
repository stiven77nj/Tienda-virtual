from django.shortcuts import render

# Importacion del modelo producto
from .models import Producto
from .forms import ContactoForm
from .forms import ProductoForm

# Vista de la pagina home
def home(request):
    productos = Producto.objects.all() # Transforma las instancias a una lista
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/home.html', data)

# Vista de la pagina de contacto
def contacto(request):
    data = {
        'form': ContactoForm()
    }

    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Contacto guardado"
        else:
            data['form'] = formulario
    return render(request, 'ventas/contacto.html', data)

# Vista de la pagina de agregar producto
def agregar_producto(request):
    data={
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario =ProductoForm(data=request.POST ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"]= "guardado correctamente"
        else:
            data["form"]=formulario

    return render(request, 'ventas/producto/agregar.html',data)

# Vista de la pagina de listar producto
def listar_productos(request):

    productos=Producto.objects.all()
    data={
        'productos':productos
    }
    return render(request,'ventas/producto/listar.html',data)