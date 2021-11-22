from django import forms
from .models import *

class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = [
            'idproducto',
            'nombreproducto',
            'cantidadp',
            'precio',
            'detalles',
            'stock',
            'fechacaducidad',
        ]
        labels = {
            'idproducto': 'Id del Producto',
            'nombreproducto': 'Nombre del producto',
            'cantidadp': 'Cantidad',
            'precio': 'Precio',
            'detalles': 'Detalles',
            'stock': 'Stock',
            'fechacaducidad': 'Fecha de caducidad',
        }
        widgets = {
            'idproducto': forms.TextInput(),
            'nombreproducto': forms.TextInput(),
            'cantidadp': forms.NumberInput(),
            'precio': forms.NumberInput(),
            'detalles': forms.Textarea(),
            'stock': forms.NumberInput(),
            'fechacaducidad': forms.DateInput(),
        }