from django.urls import path
'''from django.contrib.auth.decorators import login_required'''
from .views import *

urlpatterns = [
    path('accounts/login/', Ingreso.as_view(), name='login'),
    path('', Inicio.as_view(), name='index'),
    path('productos/', MostrarProducto.as_view(), name='productos'),
    path('agregarProducto/', AgregarProducto.as_view(), name='agregarproducto'),
    path('modificarProducto/<pk>', ModificarProducto.as_view(), name='modificarproducto'),
    path('eliminarProducto/<pk>', EliminarProducto.as_view(), name='eliminarproducto'),
    path('respaldar_restaurar/', RespaldarRestaurar.as_view(), name='respaldar_restaurar'),
]