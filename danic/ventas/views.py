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