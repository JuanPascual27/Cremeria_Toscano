from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import PermissionRequiredMixin
from .mixins import ValidarPermisosMixin

#Para respaldar y restaurar
import os
from .models import *
from .forms import *

# Create your views here.

'''
    1- dispatch(): valida la peticion y elige que metodo HTTP se utilizo para la solicitud
    2- http_method_not:allowed(): retorna un error cuando se utiliza un metodo HTTP no soportado o definido
    3- options(): para utilizar opciones del view
'''

class Ingreso(LoginView):
    template_name = 'Cremeria_ToscanoApp/login.html'

class Inicio(LoginRequiredMixin, TemplateView):
    template_name = 'Cremeria_ToscanoApp/index.html'
'''
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(self.template_name)
        else:
            return redirect('Cremeria_ToscanoApp:login')'''

class MostrarProducto(LoginRequiredMixin, ValidarPermisosMixin, ListView):
    permission_required = 'Cremeria_ToscanoApp.view_productos'

    model = Productos
    template_name = 'Cremeria_ToscanoApp/mostrar_productos.html'
    context_object_name = 'productos'
    queryset = Productos.objects.all()

    def post(self, request, *args, **kwargs):
        buscar = request.POST['consulta']
        productos = Productos.objects.filter(nombreproducto__contains=buscar)
        return render(request,self.template_name,{"productos":productos})

class AgregarProducto(LoginRequiredMixin, ValidarPermisosMixin, CreateView):
    permission_required = 'Cremeria_ToscanoApp.add_productos'

    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_producto.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')

class ModificarProducto(LoginRequiredMixin, ValidarPermisosMixin, UpdateView):
    permission_required = 'Cremeria_ToscanoApp.change_productos'

    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/modificar_producto.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')

class EliminarProducto(LoginRequiredMixin, ValidarPermisosMixin, DeleteView):
    permission_required = 'Cremeria_ToscanoApp.delete_productos'

    model = Productos
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')


class MostrarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, ListView):
    permission_required = 'Cremeria_ToscanoApp.view_detallesventas'

    model = Detallesventas
    template_name = 'Cremeria_ToscanoApp/mostrar_detallesventas.html'
    context_object_name = 'detallesventas'
    queryset = Detallesventas.objects.all()

    def post(self, request, *args, **kwargs):
        buscar = request.POST['consulta']
        detallesventas = Detallesventas.objects.filter(idventa__idventa__icontains=buscar)
        return render(request,self.template_name,{"detallesventas":detallesventas})

class AgregarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, CreateView):
    permission_required = 'Cremeria_ToscanoApp.add_detallesventas'

    model = Detallesventas
    form_class = DetallesVentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_detallesventa.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:detallesventas')
    
    def post(self, request, *args, **kwargs):
        register = DetallesVentasForm(request.POST)
        if register.is_valid():
            with transaction.atomic():
                try:
                    if int(request.POST['cantidadpv']) <= 0:
                        y = 1/0
                    else:
                        y = 1
                        register.save()
                except Exception as e:
                    messages.error(request, 'Debes ingresar una cantidad de producto mayor a 0')
        else:
            pass
        return redirect('Cremeria_ToscanoApp:detallesventas')

class ModificarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, UpdateView):
    permission_required = 'Cremeria_ToscanoApp.change_detallesventas'

    model = Detallesventas
    form_class = DetallesVentasForm
    template_name = 'Cremeria_ToscanoApp/formularios/modificar_detallesventa.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:detallesventas')

class EliminarDetallesVenta(LoginRequiredMixin, ValidarPermisosMixin, DeleteView):
    permission_required = 'Cremeria_ToscanoApp.delete_detallesventas'

    model = Detallesventas
    success_url = reverse_lazy('Cremeria_ToscanoApp:detallesventas')


class RespaldarRestaurar(LoginRequiredMixin, TemplateView):
    template_name = 'Cremeria_ToscanoApp/respaldar_restaurar.html'
    
    def post(self, request, *args, **kwargs):
        accion = request.POST['accion']
        print(accion)
        if accion == "Respaldar":
            os.system('Python manage.py dumpdata --format=json --indent=4 > backup/respaldo_base.json')
        else:
            os.system('Python manage.py loaddata backup/respaldo_base.json')
        return redirect('Cremeria_ToscanoApp:index')
