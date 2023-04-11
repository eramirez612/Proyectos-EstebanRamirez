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
    return render(request, 'main/lista.html', data)

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
    ins_regimen = Regimen_Provisional.objects.get(id=obj.id)
    ins_apv = APV.objects.get(id=obj.id)
    ins_salud = Salud.objects.get(id=obj.id)
    ins_liquidacion = Liquidacion.objects.get(id=obj.id)
    #ins_no_imponibles = No_Imponibles.objects.get(id=obj.id)
    ins_pago = Forma_de_pago.objects.get(id=obj.id)
    form = Datos_EmpleadoForm(instance=obj)
    form_2 = RegimenForm(instance=ins_regimen)
    form_3 = ApvForm(instance=ins_apv)
    form_4 = SaludForm(instance=ins_salud)
    form_5 = LiquidacionForm(instance=ins_liquidacion)
    #form_6 = No_ImponiblesForm(instance=ins_no_imponibles)
    form_7 = PagoForm(instance=ins_pago)
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST, instance=obj)
        form_2 = RegimenForm(request.POST, instance=ins_regimen)
        form_3 = ApvForm(request.POST, instance=ins_apv)
        form_4 = SaludForm(request.POST, instance=ins_salud)
        form_5 = LiquidacionForm(request.POST, instance=ins_liquidacion)
        #form_6 = No_ImponiblesForm(request.POST, instance=ins_no_imponibles)
        form_7 = PagoForm(request.POST, instance=ins_pago)
        if all([form.is_valid(), form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(),  form_7.is_valid()]):
            post = form.save(commit=False)
            regimen = form_2.save(commit=False)
            apv = form_3.save(commit=False)
            salud = form_4.save(commit=False)
            liquidacion = form_5.save(commit=False)
            #no_imponibles = form_6.save(commit=False)
            pago = form_7.save(commit=False)
            #--
            regimen.Datos_Empleado = post
            apv.Datos_Empleado = post
            salud.Datos_Empleado = post
            liquidacion.Datos_Empleado = post
            #no_imponibles.Datos_Empleado = post
            pago.Datos_Empleado = post
            #--
            post.save()
            regimen.save()
            apv.save()
            salud.save()
            liquidacion.save()
            #no_imponibles.save()
            pago.save()


            return TrabajadorList(request)
    data = {
        'form': form, 
        'form_2': form_2,
        'form_3': form_3,
        'form_4': form_4,
        'form_5': form_5,
        'form_7': form_7,
        'object': obj
        }
    
    return render(request, 'main/actualizar_trabajador.html', data)

@login_required(login_url="/login")
def detalle_trabajador(request, id):
    obj =  get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    card_2 = Regimen_Provisional.objects.get(id=obj.id)
    card_3 = APV.objects.get(id=obj.id)
    card_4 = Salud.objects.get(id=obj.id)
    card_5 = Liquidacion.objects.get(id=obj.id)
    #card_6 = No_Imponibles.objects.get(id=obj.id)
    card_7 = Forma_de_pago.objects.get(id=obj.id)
    data = {
        'card': obj, 
        'card_2': card_2,
        'card_3': card_3,
        'card_4': card_4,
        'card_5': card_5,
        #'card_6': card_6,
        'card_7': card_7,
        }
    return render(request, 'main/trabajador.html', data)


@login_required(login_url="/login")
def liquidacion(request, id):
    obj =  get_object_or_404(Datos_Empleado, id=id, autor=request.user)

@login_required(login_url="/login")
def eliminarTrabajadores(request, id):
    trabajador = Datos_Empleado.objects.get(id = id)
    trabajador.delete()
    return redirect('/Trabajadores')

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

