from django.shortcuts import render, redirect
from .forms import RegisterForm, Datos_EmpleadoForm
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

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

@login_required(login_url="/login")
def nuevo_trabajador(request):
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('/home')
    else:
        form = Datos_EmpleadoForm()
    
    return render(request, 'main/nuevo_trabajador.html', {"form": form})