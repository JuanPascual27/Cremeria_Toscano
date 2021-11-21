from django.shortcuts import render, redirect

#Para respaldar y restaurar
import os

# Create your views here.
def respaldar_restaurar(request):
    if request.method == 'POST':
        datos = request.POST.dict()
        accion = datos.get("accion")
        print(accion)
        if accion == "Respaldar":
            os.system('Python manage.py dumpdata --format=json --indent=4 > backup/respaldo_base.json')
        else:
            os.system('Python manage.py loaddata backup/respaldo_base.json')
        return redirect('http://127.0.0.1:8000/admin')
    else:
        return render(request,'Cremeria_ToscanoApp/respaldar_restaurar.html')
