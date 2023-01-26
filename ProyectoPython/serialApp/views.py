from django.shortcuts import render, redirect
from serialApp.models import User, Proyecto
from serialApp.forms import ProyectoForm

# Create your views here.

def personadata(request):
    personas = Proyecto.objects.all()
    data = {'personas' : personas}
    return render(request, 'empleados.html', data)

def index(request):
    return render(request, 'index.html')

def listadoproyectos(request):
    proyectos = Proyecto.objects.all()
    data = {'proyectos': proyectos}
    return render(request, 'proyectos.html', data)

def agregarproyecto(request):
    form = ProyectoForm()
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarproyecto.html', data)

def eliminarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    pro.delete()
    return redirect('/proyectos')

def actualizarProyecto(request, id):
    pro = Proyecto.objects.get(id = id)
    form = ProyectoForm(instance=pro)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=pro)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)