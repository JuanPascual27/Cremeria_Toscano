from django.urls import path
from .views import *

urlpatterns = [
    path('index/', Inicio.as_view(), name='index'),
    path('productos/', MostrarProducto.as_view(), name='productos'),
    path('agregarProducto/', AgregarProducto.as_view(), name='agregarproducto'),
    path('modificarProducto/<pk>', ModificarProducto.as_view(), name='modificarproducto'),
    path('eliminarProducto/<pk>', EliminarProducto.as_view(), name='eliminarproducto'),
    path('respaldar_restaurar/', respaldar_restaurar, name='respaldar_restaurar'),
]