from django import forms
from .models import Contacto, Producto
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Formulario de contacto
class ContactoForm(forms.ModelForm):

    # Se especifica con que clase esta relacionada
    class Meta:
        model = Contacto
        #fields = ["nombre", "correo", "tipo_consulta", "mensaje", "avisos"]
        fields = '__all__'


# Formulario de agregar producto
class ProductoForm(forms.ModelForm):
    
    # Se especifica con que clase esta relacionada
    class Meta:
        model=Producto
        fields= '__all__'

# Formulario de registro
class CustomUserCreationForm(UserCreationForm):

    # Se especifica con que clase esta relacionada
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1']
