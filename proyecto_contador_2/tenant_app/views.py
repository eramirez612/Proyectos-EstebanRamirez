from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms.models import modelformset_factory, inlineformset_factory
from  django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
import requests
import json
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
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
            return redirect('/lista')
    data = {'form': form,}
    
    return render(request, 'main/nuevo_trabajador.html', data)

@login_required(login_url="/login")
def actualizar_trabajador(request, id):
    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    try:
        ins_regimen = Regimen_Provisional.objects.get(id=obj.id)
    except Regimen_Provisional.DoesNotExist:
        ins_regimen = None
    try:
        ins_apv = APV.objects.get(id=obj.id)
    except APV.DoesNotExist:
        ins_apv = None
    try:
        ins_salud = Salud.objects.get(id=obj.id)
    except Salud.DoesNotExist:
        ins_salud= None
    try:
        ins_liquidacion = Liquidacion.objects.get(id=obj.id)
    except Liquidacion.DoesNotExist:
        ins_liquidacion = None
    try:
        ins_no_imponibles = No_Imponibles.objects.get(id=obj.id)
    except No_Imponibles.DoesNotExist:
        ins_no_imponibles = None
    try:
        ins_pago = Forma_de_pago.objects.get(id=obj.id)
    except Forma_de_pago.DoesNotExist:
        ins_pago = None
        
    form = Datos_EmpleadoForm(instance=obj)
    form_2 = RegimenForm(instance=ins_regimen)
    form_3 = ApvForm(instance=ins_apv)
    form_4 = SaludForm(instance=ins_salud)
    form_5 = LiquidacionForm(instance=ins_liquidacion)
    form_6 = No_ImponiblesForm(instance=ins_no_imponibles)
    form_7 = PagoForm(instance=ins_pago)
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST, instance=obj)
        form_2 = RegimenForm(request.POST, instance=ins_regimen)
        form_3 = ApvForm(request.POST, instance=ins_apv)
        form_4 = SaludForm(request.POST, instance=ins_salud)
        form_5 = LiquidacionForm(request.POST, instance=ins_liquidacion)
        form_6 = No_ImponiblesForm(request.POST, instance=ins_no_imponibles)
        form_7 = PagoForm(request.POST, instance=ins_pago)
        if all([form.is_valid(), form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(), form_6.is_valid(),  form_7.is_valid()]):
            post = form.save(commit=False)
            regimen = form_2.save(commit=False)
            apv = form_3.save(commit=False)
            salud = form_4.save(commit=False)
            liquidacion = form_5.save(commit=False)
            no_imponibles = form_6.save(commit=False)
            pago = form_7.save(commit=False)
            #--
            regimen.Datos_Empleado = post
            apv.Datos_Empleado = post
            salud.Datos_Empleado = post
            liquidacion.Datos_Empleado = post
            no_imponibles.Datos_Empleado = post
            pago.Datos_Empleado = post
            #--
            post.save()
            regimen.save()
            apv.save()
            salud.save()
            liquidacion.save()
            no_imponibles.save()
            pago.save()


            return TrabajadorList(request)
    data = {
        'form': form, 
        'form_2': form_2,
        'form_3': form_3,
        'form_4': form_4,
        'form_5': form_5,
        'form_6': form_6,
        'form_7': form_7,
        'object': obj
        }
    
    return render(request, 'main/actualizar_trabajador.html', data)

@login_required(login_url="/login")
def detalle_trabajador(request, id):
    obj =  get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    try:
        card_2 = Regimen_Provisional.objects.get(id=obj.id)
    except Regimen_Provisional.DoesNotExist:
        card_2 = RegimenForm()
    try:
        card_3 = APV.objects.get(id=obj.id)
    except APV.DoesNotExist:
        card_3 = ApvForm()
    try:
        card_4 = Salud.objects.get(id=obj.id)
    except Salud.DoesNotExist:
        card_4 = SaludForm()
    try:
        card_5 = Liquidacion.objects.get(id=obj.id)
    except Liquidacion.DoesNotExist:
        card_5 = LiquidacionForm()
    try:
        card_6 = No_Imponibles.objects.get(id=obj.id)
    except No_Imponibles.DoesNotExist:
        card_6 = No_ImponiblesForm()
    try:
        card_7 = Forma_de_pago.objects.get(id=obj.id)
    except Forma_de_pago.DoesNotExist:
        card_7 = PagoForm()

    data = {
        'card': obj, 
        'card_2': card_2,
        'card_3': card_3,
        'card_4': card_4,
        'card_5': card_5,
        'card_6': card_6,
        'card_7': card_7,
        }
    return render(request, 'main/trabajador.html', data)


@login_required(login_url="/login")
def liquidacion(request, id):
    obj =  get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    try:
        regimen = Regimen_Provisional.objects.get(id=obj.id)
    except Regimen_Provisional.DoesNotExist:
        regimen = None
    try:
        apv = APV.objects.get(id=obj.id)
    except APV.DoesNotExist:
        apv = None
    try:
        salud = Salud.objects.get(id=obj.id)
    except Salud.DoesNotExist:
        salud = None
    try:
        liquidacion = Liquidacion.objects.get(id=obj.id)
    except Liquidacion.DoesNotExist:
        liquidacion = None
    try:
        no_imponibles = No_Imponibles.objects.get(id=obj.id)
    except No_Imponibles.DoesNotExist:
        no_imponibles = None
    try:
        pago = Forma_de_pago.objects.get(id=obj.id)
    except Forma_de_pago.DoesNotExist:
        pago = None
    try:
        adicionales = Adicionales.objects.get(id=obj.id)
    except Adicionales.DoesNotExist:
        adicionales = None
    try:
        descuentos = Descuentos.objects.get(id=obj.id)
    except Descuentos.DoesNotExist:
        descuentos = None
    try:
        movimiento_personal = Movimiento_Personal.objects.get(id=obj.id)
    except Movimiento_Personal.DoesNotExist:
        movimiento_personal = None
    try:
        impuesto = Impuesto.objects.get(id=obj.id)
    except Impuesto.DoesNotExist:
        impuesto = None

    uf_url = requests.get('https://mindicador.cl/api/uf')
    utm_url = requests.get('https://mindicador.cl/api/utm')

    uf = uf_url.json()["serie"][0]["valor"]
    utm = utm_url.json()["serie"][0]["valor"]

    
    ingreso_minimo_mensual = 326.500
    utm = utm
    UF = uf #Ultimo dia del mes
    tope_imponible_uf = 81.6 #AFP y salud
    tope_imponible_clp = tope_imponible_uf * UF #AFP y salud
    tope_imponible_uf_cesantia = 122.6


    sueldo_base = Liquidacion.Sueldo_Base
    bonos = Adicionales.Valor
    gratificacion_legal = (4.75*ingreso_minimo_mensual)/12
    haberes_imponibles = sueldo_base + bonos + gratificacion_legal

    colacion = No_Imponibles.Colacion
    movilizacion = No_Imponibles.Movilizacion
    trabajo_remoto = No_Imponibles.Trabajo_Remoto
    haberes_no_imponibles = colacion + movilizacion + trabajo_remoto
    
    prevision = haberes_imponibles*11.45 #se necesita una variable que cambie la tasa dependiendo de la prevision
    salud = haberes_imponibles*7
    adi_salud = Salud.Plan_UF
    seguro_cesantia = haberes_imponibles*0.6
    descuentos_legales = prevision + salud + adi_salud + seguro_cesantia

    sueldo_antes_de_impuesto = haberes_imponibles -descuentos_legales
    impuesto_primera_categoria = Impuesto.Factor_impuesto_unico_primera_categoria + sueldo_antes_de_impuesto # agregar a forms
    rebaja = Impuesto.Cantidad_a_rebajar
    impuesto_segunda_categoria = impuesto_primera_categoria + rebaja
    impuesto = impuesto_primera_categoria + impuesto_segunda_categoria
    total_descuento = descuentos_legales+ impuesto

    total_liquido = haberes_imponibles + haberes_no_imponibles - total_descuento

    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter, bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont("Helvetica", 14)

    lines = []

    lines.append(total_liquido)

    return total_liquido


@login_required(login_url="/login")
def eliminarTrabajadores(request, id):
    trabajador = Datos_Empleado.objects.get(id = id)
    trabajador.delete()
    return redirect('/lista')

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