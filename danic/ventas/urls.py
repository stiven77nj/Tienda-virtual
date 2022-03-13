from unicodedata import name
from django.urls import path
from .views import eliminar_producto, estufas,cuenta, freidoras, home, celulares, lavadoras, microondas, neveras, televisores, ventiladores, contacto, agregar_producto, listar_productos, modificar_producto, registro

urlpatterns = [
    path('', home, name='home'),
    path('celulares/', celulares, name="celulares"),
    path('ventiladores/', ventiladores, name="ventiladores"),
    path('estufas/', estufas, name="estufas"),
    path('freidoras/', freidoras, name="freidoras"),
    path('lavadoras/', lavadoras, name="lavadoras"),
    path('televisores/', televisores, name="televisores"),
    path('neveras/', neveras, name="neveras"),
    path('microondas/', microondas, name="microondas"),
    path('contacto/', contacto, name="contacto"),
    path('cuenta/',cuenta,name="cuenta"),
    path('agregar-producto/', agregar_producto, name="agregar_producto"),
    path('listar-productos/',listar_productos, name="listar_productos"),
    path('modificar-producto/<id>/',modificar_producto,name='modificar_producto'),
    path('eliminar-producto/<id>/',eliminar_producto,name="eliminar_producto"),
    path('registro/', registro, name="registro"),
]