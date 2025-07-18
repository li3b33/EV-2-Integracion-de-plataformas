from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Herramienta
from django import forms

from django import forms
from .models import MensajeContacto

class MensajeContactoForm(forms.ModelForm):
    class Meta:
        model = MensajeContacto
        fields = ['tipo', 'mensaje']
        widgets = {
            'tipo': forms.Select(attrs={'class': 'form-select'}),
            'mensaje': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu mensaje aquí...'
            })
        }
    
class RegistroUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class HerramientaForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = [
            'codigo_interno',
            'codigo_fabricante',
            'marca',
            'nombre',
            'descripcion',
            'categoria', 
            'precio',
            'stock',
            'imagen',
        ]

class OrdenForm(forms.Form):
    monto = forms.IntegerField(
        label='Monto a pagar',
        min_value=1,
        widget=forms.NumberInput(attrs={
            'placeholder': 'Ingrese el monto en pesos',
            'class': 'form-control'
        })
    )


class HerramientaStockForm(forms.ModelForm):
    class Meta:
        model = Herramienta
        fields = ['stock']


from django import forms
from .models import RespuestaMensaje

class RespuestaMensajeForm(forms.ModelForm):
    class Meta:
        model = RespuestaMensaje
        fields = ['respuesta']
        widgets = {
            'respuesta': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Escribe tu respuesta aquí...'
            })
        }

