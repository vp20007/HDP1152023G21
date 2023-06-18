from django import forms
from .models import *

class productosEditForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ('nombre_producto', 'gramos_persona')

class mesesEditForm(forms.ModelForm):
    class Meta:
        model = Mes
        fields = ('indice_precio',)

class canastaEditForm(forms.ModelForm):
    class Meta:
        model = CanastaBasica
        fields = ('tipo_de_zona','integrantes_por_familia')
