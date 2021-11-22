from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, CreateView, UpdateView, DeleteView

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

class Inicio(TemplateView):
    template_name = 'Cremeria_ToscanoApp/index.html'

class MostrarProducto(ListView):
    model = Productos
    template_name = 'Cremeria_ToscanoApp/mostrar_productos.html'
    context_object_name = 'productos'
    queryset = Productos.objects.all()

class AgregarProducto(CreateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_producto.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')

class ModificarProducto(UpdateView):
    model = Productos
    form_class = ProductosForm
    template_name = 'Cremeria_ToscanoApp/formularios/agregar_producto.html'
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')

class EliminarProducto(DeleteView):
    model = Productos
    success_url = reverse_lazy('Cremeria_ToscanoApp:productos')

def respaldar_restaurar(request):
    if request.method == 'POST':
        datos = request.POST.dict()
        accion = datos.get("accion")
        print(accion)
        if accion == "Respaldar":
            os.system('Python manage.py dumpdata --format=json --indent=4 > backup/respaldo_base.json')
        else:
            os.system('Python manage.py loaddata backup/respaldo_base.json')
        return redirect('Cremeria_ToscanoApp:index')
    else:
        return render(request,'Cremeria_ToscanoApp/respaldar_restaurar.html')
