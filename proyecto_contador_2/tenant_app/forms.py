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
    Plan_UF = forms.DecimalField(required=False)

    class Meta:
        model = Salud
        fields = [
            'Institucion_Salud',
            'Plan_UF',
        ]

class LiquidacionForm(forms.ModelForm):
    #Liquidacion
    Fecha_Emision = forms.DateField(widget=DateInput)
    #Profesion = forms.ChoiceField(choices=profesion, required=False)
    Tipo_Trabajador = forms.ChoiceField(choices=tipo_trabajador)
    Sin_Seguro_Cesantia = forms.BooleanField()
    Trabajador_Agricola = forms.BooleanField()
    Director_de_Empresa = forms.BooleanField()
    Sueldo_Base = forms.DecimalField()
    Tipo_Contrato = forms.ChoiceField(choices=duracion_contrato)
    Tipo_Jornada_Trabajo = forms.ChoiceField(choices=work_choices)
    Dias_Descontados = forms.IntegerField()
    Dias_Licencia = forms.IntegerField()
    Cargas_Familiares = forms.BooleanField()

    class Meta:
        model = Liquidacion
        fields = [
            'Fecha_Emision',
            #'Profesion',
            'Tipo_Trabajador',
            'Sin_Seguro_Cesantia',
            'Trabajador_Agricola',
            'Director_de_Empresa',
            'Sueldo_Base',
            'Tipo_Contrato',
            'Tipo_Jornada_Trabajo',
            'Dias_Descontados',
            'Dias_Licencia',
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


class AdicionalesForm(forms.ModelForm):
    Adicional = forms.ChoiceField(choices=adicional)
    Tipo_de_Bono = forms.ChoiceField(choices=bonos)
    Valor = forms.DecimalField()

    class Meta:
        model = Adicionales
        fields = [
            'Adicional',
            'Tipo_de_Bono',
            'Valor',
        ]


class DescuentosForm(forms.ModelForm):
    Descuento = forms.ChoiceField(choices=descuento)
    Valor = forms.DecimalField()
    
    class Meta:
        model = Descuentos
        fields = [
            'Descuento',
            'Valor',
        ]
    
class Movimiento_PersonalForm(forms.ModelForm):
    Movimiento_Personal = forms.ChoiceField(choices=movimientos_personales)
    Fecha_Inicio = forms.DateField(widget=DateInput)
    Fecha_Termino = forms.DateField(widget=DateInput)

    class Meta:
        model = Movimiento_Personal
        fields = [
            'Movimiento_Personal',
            'Fecha_Inicio',
            'Fecha_Termino',
        ]

class ImpuestoForm(forms.ModelForm):
    Factor_Impuesto_unico_primera_categoria = forms.DecimalField()
    Cantidad_a_rebajar = forms.DecimalField()

    class Meta:
        model = Impuesto
        fields = [
            'Factor_Impuesto_unico_primera_categoria',
            'Cantidad_a_rebajar',
        ]