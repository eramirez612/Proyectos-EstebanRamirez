from django.shortcuts import render, redirect
from serialApp.models import Registro_Equipo
from serialApp.forms import FormEquipo

#Clase para cuando se haga el ingreso redireccione al indice

def index(request):
    return render(request, 'index.html')

#Clase para mostrar el listado de los equipos
def listado_equipos(request):
    equipos = Registro_Equipo.objects.all()
    data = {'equipos': equipos}
    return render(request, 'listado_registros.html', data)

#Clase para ingresar un equipo a la DB
def agregar_equipo(request):
    form = FormEquipo()
    if request.method == 'POST':
        form = FormEquipo(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregar_registro.html', data)

#Clase para eliminar un equipo de la DB
def eliminar_equipo(request, serial_number):
    registro = Registro_Equipo.objects.get(serial_number = serial_number)
    registro.delete()
    return redirect('listado_registros.html')

#Clase para actualizar un registro existente 
def actualizar_equipo(request, serial_number):
    registro = Registro_Equipo.objects.get(serial_number = serial_number)
    form = FormEquipo(instance = registro)
    if request.method == 'POST':
        form = FormEquipo(request.POST, instance=registro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregar_registro.html', data)