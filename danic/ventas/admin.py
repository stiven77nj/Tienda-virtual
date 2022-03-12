from re import search
from django.contrib import admin
# Se importan los modelos
from .models import Marca, Producto, Contacto

# Register your models here.

# Forma de obersar los productos del admin
class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre","precio","marca"] # Columnas mostradas al agregar un producto
    list_editable = ["precio"] # Se puede editar
    search_fields = ["nombre","precio","precio"] # Campos validos en la barra de busqueda
    list_filter = ["marca"] # Filtrar por marca
    list_per_page = 5 # Registro por pagina (paginacion)

admin.site.register(Marca) # Modelo Marca
admin.site.register(Producto, ProductoAdmin) # Modelo Producto
admin.site.register(Contacto) # Modelo Producto
