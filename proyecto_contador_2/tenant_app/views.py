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

    ingreso_minimo_mensual = ""
    utm = ""
    UF = "" #Ultimo dia del mes
    tope_imponible_uf = "" #AFP y salud
    tope_imponible_clp = tope_imponible_uf * UF #AFP y salud
    tope_imponible_uf_cesantia = ""

    sueldo_base = ""
    sobresueldo = "" #horas extras
    comision = ""
    bono = ""
    diferencia_gratificacion = ""
    gratificacion_legal =((4.75*ingreso_minimo_mensual)/12) #4,75 sueldos minimos /12 meses o sueldo_base * 0.25
    total_haberes_imponibles = sueldo_base + sobresueldo + comision + bono + diferencia_gratificacion + gratificacion_legal

    otras_asignaciones = no_imponibles.Perdida_Caja + no_imponibles.Desgaste_Herramientas + no_imponibles.Trabajo_Remoto
    transporte_y_colacion = no_imponibles.Colacion + no_imponibles.Movilizacion
    asignacion_familiar = ""
    total_haberes_no_imponibles = otras_asignaciones + transporte_y_colacion + asignacion_familiar

    #Cotizacion obligatoria afp
    pago_electronico_cotizacion_adicional = "" #costo afp
    pago_electronico_cotizacion_obligatoria = "" #fondo individual
    cotizacion_obligatoria_afp = pago_electronico_cotizacion_obligatoria + pago_electronico_cotizacion_adicional
    
    cotizacion_salud = "" # 7%* total haberes imponible
    adicional_cotizacion_salud = ""
    seguro_de_cesantia = ""

    sueldo_antes_de_impuestos = total_haberes_imponibles - cotizacion_obligatoria_afp - cotizacion_salud - adicional_cotizacion_salud - seguro_de_cesantia
    tasa_impuesto_unica_segunda_categoria = ""






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



#def actualizar_trabajadorv2(request, id):
#    obj = get_object_or_404(Datos_Empleado, id=id, autor=request.user)
#    try:
#        ins_regimen = Regimen_Provisional.objects.get(id=obj.id)
#    except Regimen_Provisional.DoesNotExist:
#        ins_regimen = None
#    try:
#        ins_apv = APV.objects.get(id=obj.id)
#    except APV.DoesNotExist:
#        ins_apv = None
#    try:
#        ins_salud = Salud.objects.get(id=obj.id)
#    except Salud.DoesNotExist:
#        ins_salud= None
#    try:
#        ins_liquidacion = Liquidacion.objects.get(id=obj.id)
#    except Liquidacion.DoesNotExist:
#        ins_liquidacion = None
#    try:
#        ins_no_imponibles = No_Imponibles.objects.get(id=obj.id)
#    except No_Imponibles.DoesNotExist:
#        ins_no_imponibles = None
#    try:
#        ins_pago = Forma_de_pago.objects.get(id=obj.id)
#    except Forma_de_pago.DoesNotExist:
#        ins_pago = None
#    form = Datos_EmpleadoForm(instance=obj)
#    form_2 = RegimenForm(instance=ins_regimen)
#    form_3 = ApvForm(instance=ins_apv)
#    form_4 = SaludForm(instance=ins_salud)
#    form_5 = LiquidacionForm(instance=ins_liquidacion)
#    form_6 = No_ImponiblesForm(instance=ins_no_imponibles)
#    form_7 = PagoForm(instance=ins_pago)
#    if request.method == 'POST':
#        form = Datos_EmpleadoForm(request.POST, instance=obj)
#        form_2 = RegimenForm(request.POST, instance=ins_regimen)
#        form_3 = ApvForm(request.POST, instance=ins_apv)
#        form_4 = SaludForm(request.POST, instance=ins_salud)
#        form_5 = LiquidacionForm(request.POST, instance=ins_liquidacion)
#        form_6 = No_ImponiblesForm(request.POST, instance=ins_no_imponibles)
#        form_7 = PagoForm(request.POST, instance=ins_pago)
#        if all([form.is_valid(), form_2.is_valid(), form_3.is_valid(), form_4.is_valid(), form_5.is_valid(), form_6.is_valid(),  form_7.is_valid()]):
#            post = form.save(commit=False)
#            regimen = form_2.save(commit=False)
#            apv = form_3.save(commit=False)
#            salud = form_4.save(commit=False)
#            liquidacion = form_5.save(commit=False)
#            no_imponibles = form_6.save(commit=False)
#            pago = form_7.save(commit=False)
#            #--
#            regimen.Datos_Empleado = post
#            apv.Datos_Empleado = post
#            salud.Datos_Empleado = post
#            liquidacion.Datos_Empleado = post
#            no_imponibles.Datos_Empleado = post
#            pago.Datos_Empleado = post
#            #--
#            post.save()
#            regimen.save()
#            apv.save()
#            salud.save()
#            liquidacion.save()
#            #no_imponibles.save()
#            pago.save()
#
#
#            return TrabajadorList(request)
#    data = {
#        'form': form, 
#        'form_2': form_2,
#        'form_3': form_3,
#        'form_4': form_4,
#        'form_5': form_5,
#        'form_7': form_7,
#        'object': obj
#        }
#    
#    return render(request, 'main/actualizar_trabajador.html', data)