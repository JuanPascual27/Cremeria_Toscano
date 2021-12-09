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

class DetallesVentasForm(forms.ModelForm):
    class Meta:
        model = Detallesventas
        fields = [
            'idventa',
            'idproducto',
            'cantidadpv',
            'costov',
            'subtotalv',
        ]
        labels = {
            'idventa': 'Id de la venta',
            'idproducto': 'Id del producto',
            'cantidadpv': 'Cantidad de producto venta',
            'costov': 'Costo de venta',
            'subtotalv': 'Subtotal de la venta',
        }
        widgets = {
            'idventa': forms.TextInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el Id de la venta'
                }
            ),
            'idproducto': forms.TextInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el Id del producto'
                }
            ),
            'cantidadpv': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'name': 'cantidadpv',
                    'placeholder': 'Ingrese la cantidad del producto que se vendio'
                }
            ),
            'costov': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el costo del producto en la venta'
                }
            ),
            'subtotalv': forms.NumberInput(
                attrs = {
                    'class': 'input_texto',
                    'placeholder': 'Ingrese el subtotalde la venta'
                }
            ),
        }
