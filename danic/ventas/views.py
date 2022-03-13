from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
# Importacion del modelo producto
from .models import Producto
# Importacion de los formularios
from .forms import ContactoForm
from .forms import ProductoForm
from .forms import CustomUserCreationForm
# Importacion de la clase Paginator
from django.core.paginator import Paginator
from django.http import Http404

from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, permission_required

# Vista de la pagina home
def home(request):
    productos = Producto.objects.all() # Transforma las instancias a una lista
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/home.html', data)

def cuenta(request):
    return render(request, 'ventas/cuenta.html')

def celulares(request):
    productos = Producto.objects.filter(categoria_id=1)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/celulares.html', data)

def ventiladores(request):
    productos = Producto.objects.filter(categoria_id=2)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/ventiladores.html', data)

def estufas(request):
    productos = Producto.objects.filter(categoria_id=3)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/estufas.html', data)

def freidoras(request):
    productos = Producto.objects.filter(categoria_id=4)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/freidoras.html', data)

def lavadoras(request):
    productos = Producto.objects.filter(categoria_id=5)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/lavadoras.html', data)

def microondas(request):
    productos = Producto.objects.filter(categoria_id=6)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/microondas.html', data)

def televisores(request):
    productos = Producto.objects.filter(categoria_id=7)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/televisores.html', data)

def neveras(request):
    productos = Producto.objects.filter(categoria_id=8)
    data = { # Se traen los productos de la base de datos
        'productos': productos
    }
    return render(request, 'ventas/categorias/neveras.html', data)

@login_required # Debe estar registrado para contactar
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

@login_required # Debe estar registrado para agregar productos
# Vista de la pagina de agregar producto
def agregar_producto(request):
    data={
        'form':ProductoForm()
    }
    if request.method == 'POST':
        formulario =ProductoForm(data=request.POST ,files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request,"Guardado correctamente")
        else:
            data["form"]=formulario

    return render(request, 'ventas/producto/agregar.html',data)

# Vista de la pagina de listar producto
def listar_productos(request):
    productos=Producto.objects.all()
    page = request.GET.get('page', 1) # De la url se obtiene la variable page

    try:
        paginator = Paginator(productos, 2)
        productos = paginator.page(page)
    except:
        raise Http404

    data={
        'entity': productos,
        'paginator': paginator
    }
    return render(request,'ventas/producto/listar.html',data)

@login_required # Debe estar registrado para modificar productos
# Vista para modificar producto
def modificar_producto(request,id):
    producto= get_object_or_404(Producto,id=id)
    data={
        'form': ProductoForm(instance=producto)
    }

    if request.method == 'POST':
        formulario=ProductoForm(data=request.POST, instance=producto, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Modificado Correctamente")
            return redirect(to="listar_productos")
            data["form"]=formulario

    return render(request,'ventas/producto/modificar.html',data)

@login_required # Debe estar registrado para eliminar productos
# Vista para eliminar producto
def eliminar_producto(request,id):
    producto=get_object_or_404(Producto,id=id)
    producto.delete()
    messages.success(request, "Eliminado Correctamente")
    return redirect(to="listar_productos")

# Vista para Registro
def registro(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(data=request.POST)

        if formulario.is_valid():
            formulario.save()
            user = authenticate(username=formulario.cleaned_data["username"], password=formulario.cleaned_data["password1"])
            login(request, user)
            messages.success(request, "Te has registrado correctamente")
            return redirect(to='home')
        data['form'] = formulario

    return render(request, 'registration/registro.html', data)