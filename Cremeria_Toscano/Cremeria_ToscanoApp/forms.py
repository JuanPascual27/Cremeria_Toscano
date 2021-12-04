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
            'idproducto': 'Id del Producto:',
            'nombreproducto': 'Nombre del producto:',
            'cantidadp': 'Cantidad:',
            'precio': 'Precio:',
            'detalles': 'Detalles:',
            'stock': 'Stock:',
            'fechacaducidad': 'Fecha de caducidad:',
        }
        widgets = {
            'idproducto': forms.TextInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el Id del producto'
                }
            ),
            'nombreproducto': forms.TextInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el nombre del producto'
                }
            ),
            'cantidadp': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese la cantidad existente del producto'
                }
            ),
            'precio': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el precio del producto'
                }
            ),
            'detalles': forms.TextInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese algunos detalles del producto'
                }
            ),
            'stock': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese la cantidad de productos para vender'
                }
            ),
            'fechacaducidad': forms.SelectDateWidget(
                attrs = {
                    'class': 'fecha',
                    'placeholder': 'Ingrese la fecha de caducidad del producto'
                }
            ),
        }