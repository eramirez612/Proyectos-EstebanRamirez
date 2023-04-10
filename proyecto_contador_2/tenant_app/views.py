from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms.models import modelformset_factory, inlineformset_factory
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def TrabajadorList(request):
    trabajador = Datos_Empleado.objects.filter(autor=request.user)
    data = {'trabajadores': trabajador}
    return render(request, 'main/trabajadores.html', data)

@login_required(login_url="/login")
def nuevo_trabajador(request):
    form = Datos_EmpleadoForm()
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('/trabajadores')
    data = {'form': form,}
    
    return render(request, 'main/nuevo_trabajador.html', data)

@login_required(login_url="/login")
def actualizar_trabajador(request, id):
    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    form = Datos_EmpleadoForm(instance=obj)
    form_2 = RegimenForm(instance=obj)
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST, instance=obj)
        form_2 = RegimenForm(request.POST, queryset=obj)
        if all([form.is_valid(), form_2.is_valid()]):
            parent = form.save(commit=False)
            parent.save
            child = form_2.save(commit=False)
            child.Datos_Empleado = parent
            child.save

            return redirect('/trabajadores')
    data = {
        'form': form, 
        'form_2': form_2,
        'object': obj}
    
    return render(request, 'main/actualizar_trabajador.html', data)

def sign_up(request):
    if  request.method == 'POST':
        form = RegisterForm(request.POST)
        if  form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/home')
    else:
        form = RegisterForm()
    
    return render(request, 'registration/sign_up.html', {'form': form})

