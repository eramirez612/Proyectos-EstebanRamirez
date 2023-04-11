from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from tenant_app.models import *
from tenant_app.listas import *

class DateInput(forms.DateInput):
    input_type = 'date'

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email","password1", "password2"]

class Datos_EmpleadoForm(forms.ModelForm):
    Rut = forms.CharField(min_length=9, max_length=9, required=True)
    Nombres = forms.CharField(min_length=3, max_length=100, required=True)
    Apellidos = forms.CharField(min_length=3, max_length=100, required=True)
    Direccion = forms.CharField(max_length=100, required=True)
    Comuna = forms.CharField(max_length=100, required=True)
    Fecha_Nacimiento = forms.DateField(widget=DateInput)
    Sexo = forms.ChoiceField(required=True, choices=sex_choices)
    Estado_civil = forms.ChoiceField(required=True, choices=civil_status_choices)
    Nacionalidad = forms.ChoiceField(required=True,choices=Nacionalidades)
    Numero_De_Pasaporte = forms.CharField(max_length=10, required=False)
    Labor_en_Liquidacion = forms.CharField(max_length=50, required=False)
    Celular = forms.IntegerField(required=True)
    Email = forms.EmailField(required=True)
    Pensionado_por_Invalidez = forms.BooleanField(required=False)
    Profesional = forms.BooleanField(required=False)
    Tipo_de_impuesto_unico = forms.ChoiceField(required=True, choices=taxes_choices)
    Descuento_Prestamo_SII = forms.BooleanField(required=False)
    Tipo_de_Jornada_Trabajo = forms.ChoiceField(required=True, choices=work_choices)
    Tecnico_Extranjero = forms.BooleanField(required=False)
 
    class Meta:
        model = Datos_Empleado
        fields = [
            'Rut',
            'Nombres',
            'Apellidos',
            'Direccion',
            'Comuna',
            'Fecha_Nacimiento',
            'Sexo',
            'Estado_civil',
            'Nacionalidad',
            'Numero_De_Pasaporte',
            'Labor_en_Liquidacion',
            'Celular',
            'Email',
            'Pensionado_por_Invalidez',
            'Profesional',
            'Tipo_de_impuesto_unico',
            'Descuento_Prestamo_SII',
            'Tipo_de_Jornada_Trabajo',
            'Tecnico_Extranjero',
            ]

class RegimenForm(forms.ModelForm):
    Regimen_Provisional = forms.ChoiceField(choices=regimen)
    Afp = forms.ChoiceField(choices=afp)
    Ahorro_imponible = forms.DecimalField(required=False)
    Puesto_Trabajo_Pesado = forms.CharField(required=False)
    Cotizacion_Trabajo_Pesado = forms.DecimalField(required=False)
    #AFP
    Ahorro_Voluntario_Afp = forms.DecimalField(required=False)
    Desea_APV = forms.BooleanField(required=False)
    #IPS 
    Ex_caja = forms.ChoiceField(choices=ex_caja, required=False)
    Tasa_Ex_caja = forms.DecimalField(required=False)

    class Meta:
        model = Regimen_Provisional
        fields = [
            'Regimen_Provisional',
            'Afp',
            'Ahorro_imponible',
            'Puesto_Trabajo_Pesado',
            'Cotizacion_Trabajo_Pesado',
            'Ahorro_Voluntario_Afp',
            'Desea_APV',
            'Ex_caja',
            'Tasa_Ex_caja',
        ]

class ApvForm(forms.ModelForm):
    Institucion_Apv = forms.ChoiceField(choices=lista_institucion_apv)
    Nro_Contrato_Apv = forms.CharField(required=False)
    Forma_Pago_Apv = forms.ChoiceField(choices=pago_apv)
    Regimen_Apv = forms.ChoiceField(choices=regimen_apv)
    Ahorro_Pesos = forms.DecimalField(required=False)
    Ahorro_UF = forms.DecimalField(required=False)
    Deposito_Convenido = forms.DecimalField(required=False)
    
    class Meta:
        model = APV
        fields = [
            'Institucion_Apv',
            'Nro_Contrato_Apv',
            'Forma_Pago_Apv',
            'Regimen_Apv',
            'Ahorro_Pesos',
            'Ahorro_UF',
            'Deposito_Convenido',
        ]

class SaludForm(forms.ModelForm):
    Institucion_Salud = forms.ChoiceField(choices=institucion_salud)
    Nro_Fun_Incorporacion = forms.CharField(required=False)
    Moneda_Plano_Salud = forms.DecimalField(required=False)
    Cotizacion_Pactada_Salud = forms.DecimalField(required=False)
    Cotizacion_Voluntaria_Salud_Pesos = forms.DecimalField(required=False)
    Cotizacion_Voluntaria_Salud_Uf = forms.DecimalField(required=False)
    Pago_Isapre_Proporcional = forms.BooleanField(required=False)

    class Meta:
        model = Salud
        fields = [
            'Institucion_Salud',
            'Nro_Fun_Incorporacion',
            'Moneda_Plano_Salud',
            'Cotizacion_Pactada_Salud',
            'Cotizacion_Voluntaria_Salud_Pesos',
            'Cotizacion_Voluntaria_Salud_Uf',
            'Pago_Isapre_Proporcional',
        ]

class LiquidacionForm(forms.ModelForm):
    #Liquidacion
    Tipo_Trabajador = forms.ChoiceField(choices=tipo_trabajador)
    Tipo_Sueldo = forms.ChoiceField(choices=tipo_sueldo)
    Forma_Pago_Sueldo = forms.ChoiceField(choices=forma_pago_sueldo)
    Horas_Semanales = forms.IntegerField()
    Informar_Horas_Trabajadas = forms.BooleanField()
    Forma_Calculo_Sueldo = forms.ChoiceField(choices=forma_calculo_sueldo)
    Monto_Calculo_Sueldo = forms.DecimalField()
    Centro_Costo = forms.ChoiceField(choices=centro)
    Valor_Hora_Normal = forms.DecimalField()
    Valor_Dia_Normal = forms.DecimalField()
    Valor_Recargo_Dominical = forms.DecimalField()
    Duracion_Contrato = forms.ChoiceField(choices=duracion_contrato)
    Fecha_Ingreso = forms.SelectDateWidget()
    Fecha_Termino = forms.SelectDateWidget()
    Posee_Seguro_Cesantia = forms.BooleanField()
    Ingreso_Seguro_Cesantia = forms.SelectDateWidget()


    class Meta:
        model = Liquidacion
        fields = [
            'Tipo_Trabajador',
            'Tipo_Sueldo',
            'Forma_Pago_Sueldo',
            'Horas_Semanales',
            'Informar_Horas_Trabajadas',
            'Forma_Calculo_Sueldo',
            'Monto_Calculo_Sueldo',
            'Centro_Costo',
            'Valor_Hora_Normal',
            'Valor_Dia_Normal',
            'Valor_Recargo_Dominical',
            'Duracion_Contrato',
            'Fecha_Ingreso',
            'Fecha_Termino',
            'Posee_Seguro_Cesantia',
            'Ingreso_Seguro_Cesantia',
        ]

class No_ImponiblesForm(forms.ModelForm):
    #No imponibles 
    Colacion = forms.DecimalField()
    Movilizacion = forms.DecimalField()
    Perdida_Caja = forms.DecimalField()
    Desgaste_Herramientas = forms.DecimalField()
    Trabajo_Remoto = forms.DecimalField()

    class Meta:
        model = No_Imponibles
        fields = [
            'Colacion',
            'Movilizacion',
            'Perdida_Caja',
            'Desgaste_Herramientas',
            'Trabajo_Remoto',
        ]

class PagoForm(forms.ModelForm):
    #Forma de pago 
    Banco_Deposito = forms.ChoiceField(choices=banco)
    Tipo_Cuenta = forms.ChoiceField(choices=tipo_cuenta)
    Nro_Cuenta = forms.CharField()

    class Meta:
        model = Forma_de_pago
        fields = [
            'Banco_Deposito',
            'Tipo_Cuenta',
            'Nro_Cuenta',
        ]


#Formsets
#RegimenFormSet = inlineformset_factory(
#    Datos_Empleado, Regimen_Provisional, form=RegimenForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)
#ApvFormSet = inlineformset_factory(
#    Datos_Empleado, APV, form=ApvForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)
#SaludFormset = inlineformset_factory(
#    Datos_Empleado, Salud, form=SaludForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)
#LiquidacionFormSet = inlineformset_factory(
#    Datos_Empleado, Liquidacion, form=LiquidacionForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)
#No_imponiblesFormSet = inlineformset_factory(
#    Datos_Empleado, No_Imponibles, form=No_ImponiblesForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)
#PagoFormSet = inlineformset_factory(
#    Datos_Empleado, Forma_de_pago, form=PagoForm,
#    extra=1, max_num=1, can_delete=True, can_delete_extra=True
#)

#Validaciones 
