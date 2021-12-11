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

    path('detallesVentas/', MostrarDetallesVenta.as_view(), name='detallesventas'),
    path('agregarDetallesVenta/', AgregarDetallesVenta.as_view(), name='agregardetallesventas'),
    path('modificarDetallesVenta/<pk>', ModificarDetallesVenta.as_view(), name='modificardetallesventas'),
    path('eliminarDetallesVenta/<pk>', EliminarDetallesVenta.as_view(), name='eliminardetallesventas'),

    path('proveedores/', MostrarProveedor.as_view(), name='proveedores'),
    path('agregarProveedor/', AgregarProveedor.as_view(), name='agregarproveedor'),
    path('modificarProveedor/<pk>', ModificarProveedor.as_view(), name='modificarproveedor'),
    path('eliminarProveedor/<pk>', EliminarProveedor.as_view(), name='eliminarproveedor'),

    path('clientes/', MostrarCliente.as_view(), name='clientes'),
    path('agregarCliente/', AgregarCliente.as_view(), name='agregarcliente'),
    path('modificarCliente/<pk>', ModificarCliente.as_view(), name='modificarcliente'),
    path('eliminarCliente/<pk>', EliminarCliente.as_view(), name='eliminarcliente'),
]