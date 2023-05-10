from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.forms.models import modelformset_factory, inlineformset_factory
from  django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
import requests
from django.utils import timezone
import pandas as pd
from datetime import date
from io import BytesIO
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def not_admin(user):
    if user:
        return user.groups.filter(name='admin').count() == 0
    return False

def not_empleado(user):
    if user:
        return user.groups.filter(name='empleado').count() == 0
    return False

@login_required(login_url="/login")
def home(request):
    return render(request, 'main/home.html')

@login_required(login_url="/login")
def TrabajadorList(request):
    trabajador = Datos_Empleado.objects.filter(autor=request.user)
    data = {'trabajadores': trabajador}
    return render(request, 'main/lista.html', data)

@login_required(login_url="/login")
def LiquidacionList(request, id):
    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    liquidacion = Liquidacion.objects.filter(Datos_Empleado_id = id)
    data = {
        'liquidaciones': liquidacion,
        'object': obj,
        }
    return render(request, 'main/lista_liquidaciones.html', data)


@login_required(login_url="/login")
def LiquidacionesList(request):
    liquidacion = Liquidacion.objects.all()
    data = {
        'liquidaciones': liquidacion,
        }
    return render(request, 'main/lista_liquidaciones_total.html', data)


@login_required(login_url="/login")
@user_passes_test(not_empleado, login_url='/home')
def nuevo_trabajador(request):
    form = Datos_EmpleadoForm()
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('lista')
    data = {'form': form,}
    
    return render(request, 'main/nuevo_trabajador.html', data)

@login_required(login_url="/login")
@user_passes_test(not_empleado, login_url='/home')
def nueva_liquidacion(request, id):
    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)

    form_1 = LiquidacionForm()

    if request.method == 'POST':
        form_1 = LiquidacionForm(request.POST)
        if all([form_1.is_valid()]):
            liquidacion = form_1.save(commit=False)
            #--
            liquidacion.Datos_Empleado = obj
            #--
            liquidacion.save()
            return redirect('lista-liquidacion', id=obj.id)
        
    data = {
        'form_1': form_1,
        'object': obj
        }
    
    return render(request, 'main/liquidacion.html', data)

@login_required(login_url="/login")
@user_passes_test(not_empleado, login_url='/home')
def datos_liquidacion(request, id):
    
    obj = get_object_or_404(Liquidacion, id=id)
    datos_empleado = Datos_Empleado.objects.get(Rut=obj.Datos_Empleado)
    try:
        ins_regimen = Regimen_Provisional.objects.get(Liquidacion_id=obj.id)
    except Regimen_Provisional.DoesNotExist:
        ins_regimen = None
    try:
        ins_apv = APV.objects.get(Liquidacion_id=obj.id)
    except APV.DoesNotExist:
        ins_apv = None
    try:
        ins_salud = Salud.objects.get(Liquidacion_id=obj.id)
    except Salud.DoesNotExist:
        ins_salud= None
    try:
        ins_no_imponibles = No_Imponibles.objects.get(Liquidacion_id=obj.id)
    except No_Imponibles.DoesNotExist:
        ins_no_imponibles = None
    try:
        ins_adicionales = Adicionales.objects.get(Liquidacion_id=obj.id)
    except Adicionales.DoesNotExist:
        ins_adicionales = None
    try:
        ins_descuentos = Descuentos.objects.get(Liquidacion_id=obj.id)
    except Descuentos.DoesNotExist:
        ins_descuentos = None
    try:
        ins_movimiento_personal = Movimiento_Personal.objects.get(Liquidacion_id=obj.id)
    except Movimiento_Personal.DoesNotExist:
        ins_movimiento_personal = None

    
    form_2 = RegimenForm(instance=ins_regimen)
    form_3 = ApvForm(instance=ins_apv)
    form_4 = SaludForm(instance=ins_salud)
    form_5 = No_ImponiblesForm(instance=ins_no_imponibles)
    form_6 = AdicionalesForm(instance=ins_adicionales)
    form_7 = DescuentosForm(instance=ins_descuentos)
    form_8 = Movimiento_PersonalForm(instance=ins_movimiento_personal)
    if request.method == 'POST':
        
        form_2 = RegimenForm(request.POST, instance=ins_regimen)
        form_3 = ApvForm(request.POST, instance=ins_apv)
        form_4 = SaludForm(request.POST, instance=ins_salud)
        form_5 = No_ImponiblesForm(request.POST, instance=ins_no_imponibles)
        form_6 = AdicionalesForm(request.POST, instance=ins_adicionales)
        form_7 = DescuentosForm(request.POST, instance=ins_descuentos)
        form_8 = Movimiento_PersonalForm(request.POST, instance=ins_movimiento_personal)
        if all([form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(), form_6.is_valid(), form_7.is_valid(), form_8.is_valid() ]):
            regimen = form_2.save(commit=False)
            apv = form_3.save(commit=False)
            salud = form_4.save(commit=False)
            no_imponibles = form_5.save(commit=False)
            adicionales = form_6.save(commit=False)
            descuentos = form_7.save(commit=False)
            movimientos_personal = form_8.save(commit=False)
            #--
            regimen.Liquidacion = obj
            apv.Liquidacion = obj
            salud.Liquidacion = obj
            no_imponibles.Liquidacion = obj
            adicionales.Liquidacion = obj
            descuentos.Liquidacion = obj
            movimientos_personal.Liquidacion = obj
            #--
            
            regimen.save()
            apv.save()
            salud.save()
            no_imponibles.save()
            adicionales.save()
            descuentos.save()
            movimientos_personal.save()

            return redirect('lista-liquidacion', id=datos_empleado.id)
    data = {
        'form_2': form_2,
        'form_3': form_3,
        'form_4': form_4,
        'form_5': form_5,
        'form_6': form_6,
        'form_7': form_7,
        'form_8': form_8,
        'object': obj
        }
    
    return render(request, 'main/datos_liquidacion.html', data)

@login_required(login_url="/login")
@user_passes_test(not_empleado, login_url='/home')
def detalle_trabajador(request, id):
    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)
    try:
        ins_pago = Forma_de_pago.objects.get(id=obj.id)
    except Forma_de_pago.DoesNotExist:
        ins_pago = None
        
    form = Datos_EmpleadoForm(instance=obj)
    form_7 = PagoForm(instance=ins_pago)
    if request.method == 'POST':
        form = Datos_EmpleadoForm(request.POST, instance=obj)
        form_7 = PagoForm(request.POST, instance=ins_pago)
        if all([form.is_valid(), form_7.is_valid()]):
            post = form.save(commit=False)
            pago = form_7.save(commit=False)
            #--
            pago.Datos_Empleado = post
            #--
            post.save()
            pago.save()

            return TrabajadorList(request)
        
    data = {
        'card': form, 
        'card_7': form_7,
        'object': obj
        }
    return render(request, 'main/trabajador.html', data)


@login_required(login_url="/login")
def liquidacion(request, id):
    liquidacion = Liquidacion.objects.get(id=id)
    datos_empleado = Datos_Empleado.objects.get(Rut=liquidacion.Datos_Empleado)
    try:
        regimen = Regimen_Provisional.objects.get(Liquidacion_id=liquidacion)
    except Regimen_Provisional.DoesNotExist:
        regimen = None
    try:
        apv = APV.objects.get(Liquidacion_id=liquidacion)
    except APV.DoesNotExist:
        apv = None
    try:
        ins_salud = Salud.objects.get(Liquidacion_id=liquidacion)
    except Salud.DoesNotExist:
        ins_salud = None
    try:
        no_imponibles = No_Imponibles.objects.get(Liquidacion_id=liquidacion)
    except No_Imponibles.DoesNotExist:
        no_imponibles = None
    try:
        adicionales = Adicionales.objects.get(Liquidacion_id=liquidacion)
    except Adicionales.DoesNotExist:
        adicionales = None
    try:
        descuentos = Descuentos.objects.get(Liquidacion_id=liquidacion)
    except Descuentos.DoesNotExist:
        descuentos = None
    try:
        movimiento_personal = Movimiento_Personal.objects.get(Liquidacion_id=liquidacion)
    except Movimiento_Personal.DoesNotExist:
        movimiento_personal = None
    try:
        impuesto = Impuesto.objects.get(Liquidacion_id=liquidacion)
    except Impuesto.DoesNotExist:
        impuesto = None

    uf_url = requests.get('https://mindicador.cl/api/uf')
    utm_url = requests.get('https://mindicador.cl/api/utm')

    uf = uf_url.json()["serie"][0]["valor"]
    utm = utm_url.json()["serie"][0]["valor"]

    dias = dias_habiles(liquidacion.Fecha_Emision)
    
    ingreso_minimo_mensual = 326.500
    utm = utm
    UF = uf #Ultimo dia del mes
    tope_imponible_uf = 81.6 #AFP y salud
    tope_imponible_clp = tope_imponible_uf * UF #AFP y salud
    tope_imponible_uf_cesantia = 122.6
    dias_trabajados = dias - liquidacion.Dias_Descontados

    #haberes imponibles
    sueldo_base = liquidacion.Sueldo_Base
    bonos = adicionales.Valor
    gratificacion = ((4.75*ingreso_minimo_mensual)/12)
    total_haberes_imponibles = (float(sueldo_base) + float(bonos) + gratificacion)
    
    #no imponibles
    colacion = no_imponibles.Colacion
    movilizacion = no_imponibles.Movilizacion
    trabajo_remoto = no_imponibles.Trabajo_Remoto
    total_no_imponibles = (colacion + movilizacion + trabajo_remoto)

    #descuentos
    regimen = float(sueldo_base)*0.1145
    salud = float(sueldo_base)*0.07
    cesantia = float(sueldo_base)*0.6
    descuento = descuentos.Valor
    total_descuentos = regimen + salud + cesantia + float(descuento)

    #sueldo liquido 
    sueldo_liquido = (total_haberes_imponibles + float(total_no_imponibles) - total_descuentos)

    #se necesita mejorar el calculo añadir tope de descuentos

    data = {
        'fecha': liquidacion.Fecha_Emision,
        'cargo': liquidacion.Profesion,
        'rut': datos_empleado.Rut,
        'nombre': datos_empleado.Nombres,
        'apellido': datos_empleado.Apellidos,
        'dias_trabajados': dias_trabajados,
        'dias_descontados': liquidacion.Dias_Descontados,
        'inst_previsional': apv.Institucion_Apv,
        'inst_salud': ins_salud.Institucion_Salud,
        'ingreso_minimo_mensual': ingreso_minimo_mensual,
        'bonos': bonos,
        'gratificacion': round(gratificacion),
        'total_haberes_imponibles': total_haberes_imponibles,
        'colacion': colacion,
        'movilizacion': movilizacion,
        'trabajo_remoto': trabajo_remoto,
        'total_no_imponibles': total_no_imponibles,
        'regimen': regimen,
        'salud': salud,
        'cesantia': cesantia, 
        'total_descuentos': total_descuentos,
        'sueldo_base': sueldo_base,
        'total_descuentos': total_descuentos,
        'sueldo_liquido': sueldo_liquido,
    }
    
    pdf = generar_pdf('main/pdf.html', data)
    response = HttpResponse(pdf, content_type='application/pdf')
    filename = "Report_for_%s.pdf" %(datos_empleado.Rut)
    content = "inline; filename= %s" %(filename)
    response['Content-Disposition']=content
    return response


def generar_pdf(template_src, context_dict={}):
    template = get_template(template_src)
    html = template.render(context_dict)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode("ISO-8859-1")), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return None
    


@login_required(login_url="/login")
@user_passes_test(not_empleado, login_url='/home')
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

def dias_habiles(date_field):
    # feriados nacionales en Chile
    feriados = [
        date_field.replace(month=1, day=1),   # Año Nuevo
        date_field.replace(month=4, day=19),  # Día del Trabajo
        date_field.replace(month=5, day=1),   # Día del Trabajo
        date_field.replace(month=9, day=18),  # Día de las Glorias del Ejército
        date_field.replace(month=9, day=19),  # Día de las Glorias del Ejército (Feriado Irrenunciable)
        date_field.replace(month=10, day=12), # Día del Descubrimiento de Dos Mundos
        date_field.replace(month=11, day=1),  # Día de Todos los Santos
        date_field.replace(month=12, day=8),  # Inmaculada Concepción
        date_field.replace(month=12, day=25), # Navidad
    ]
    
    inicio = date_field.replace(day=1)
    fin = inicio.replace(day=28) if inicio.month < 12 else inicio.replace(month=1, day=1, year=inicio.year+1)
    dias = pd.date_range(start=inicio, end=fin, freq='D').to_pydatetime().tolist()
    
    dias_habiles = [d for d in dias if d.weekday() < 5 and d not in feriados]
    
    return len(dias_habiles)