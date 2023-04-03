from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from tenant_app.models import Datos_Empleado

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
    Direccion = forms.CharField(max_length=100, required=False)
    Comuna = forms.CharField(max_length=100, required=True)
    Fecha_Nacimiento = forms.DateField(widget=DateInput)
    Nacionalidad = forms.CharField(max_length=50, required=True)
    Numero_De_Pasaporte = forms.CharField(max_length=10, required=False)
    Labor_en_Liquidacion = forms.CharField(max_length=50, required=False)
    Celular = forms.IntegerField(min_value=900000000, max_value=999999999, required=False)
    Email = forms.EmailField(required=False,)
    Pensionado_por_Invalidez = forms.BooleanField(required=False)
    Profesional = forms.BooleanField(required=False)
    Tipo_de_impuesto_unico = forms.CharField(required=True)
    Descuento_Prestamo_SII = forms.BooleanField(required=False)
    Tipo_de_Jornada_Trabajo = forms.CharField(required=True)
    Tecnico_Extranjero = forms.BooleanField(required=False)
    #Regimen provisional
    Regimen_Provisional = forms.SelectMultiple()
    Afp = forms.SelectMultiple()
    Ahorro_imponible = forms.DecimalField()
    Puesto_Trabajo_Pesado = forms.CharField()
    Cotizacion_Trabajo_Pesado = forms.DecimalField()
    #AFP
    Ahorro_Voluntario_Afp = forms.DecimalField()
    Desea_APV = forms.BooleanField()
    #APV
    Institucion_Apv = forms.SelectMultiple()
    Nro_Contrato_Apv = forms.CharField()
    Forma_Pago_Apv = forms.SelectMultiple()
    Regimen_Apv = forms.SelectMultiple()
    Ahorro_Pesos = forms.DecimalField()
    Ahorro_UF = forms.DecimalField()
    Deposito_Convenido = forms.DecimalField()
    #IPS 
    Ex_caja = forms.SelectMultiple()
    Tasa_Ex_caja = forms.DecimalField()
    #Salud
    Institucion_Salud = forms.SelectMultiple()
    Nro_Fun_Incorporacion = forms.CharField()
    Moneda_Plano_Salud = forms.DecimalField()
    Cotizacion_Pactada_Salud = forms.DecimalField()
    Cotizacion_Voluntaria_Salud_Pesos = forms.DecimalField()
    Cotizacion_Voluntaria_Salud_Uf = forms.DecimalField()
    Pago_Isapre_Proporcional = forms.BooleanField()
    #Liquidacion
    Tipo_Trabajador = forms.SelectMultiple()
    Tipo_Sueldo = forms.SelectMultiple()
    Forma_Pago_Sueldo = forms.SelectMultiple()
    Horas_Semanales = forms.IntegerField()
    Informar_Horas_Trabajadas = forms.BooleanField()
    Forma_Calculo_Sueldo = forms.SelectMultiple()
    Monto_Calculo_Sueldo = forms.DecimalField()
    Centro_Costo = forms.SelectMultiple()
    Valor_Hora_Normal = forms.DecimalField()
    Valor_Dia_Normal = forms.DecimalField()
    Valor_Recargo_Dominical = forms.DecimalField()
    Duracion_Contrato = forms.SelectMultiple()
    Fecha_Ingreso = forms.SelectDateWidget()
    Fecha_Termino = forms.SelectDateWidget()
    Posee_Seguro_Cesantia = forms.BooleanField()
    Ingreso_Seguro_Cesantia = forms.SelectDateWidget()
    #No imponibles 
    Colacion = forms.DecimalField()
    Movilizacion = forms.DecimalField()
    Perdida_Caja = forms.DecimalField()
    Desgaste_Herramientas = forms.DecimalField()
    Trabajo_Remoto = forms.DecimalField()
    #Forma de pago 
    Banco_Deposito = forms.SelectMultiple()
    Tipo_Cuenta = forms.SelectMultiple()
    Nro_Cuenta = forms.CharField()
 
    class Meta:
        model = Datos_Empleado
        fields = [
            'Rut',
            'Nombres',
            'Apellidos',
            'Direccion',
            'Comuna',
            'Fecha_Nacimiento',
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
            'Regimen_Provisional',
            'Afp',
            'Ahorro_imponible',
            'Puesto_Trabajo_Pesado',
            'Cotizacion_Trabajo_Pesado',
            'Ahorro_Voluntario_Afp',
            'Desea_APV',
            'Institucion_Apv',
            'Nro_Contrato_Apv',
            'Forma_Pago_Apv',
            'Regimen_Apv',
            'Ahorro_Pesos',
            'Ahorro_UF',
            'Deposito_Convenido',
            'Ex_caja',
            'Tasa_Ex_caja',
            'Institucion_Salud',
            'Nro_Fun_Incorporacion',
            'Moneda_Plano_Salud',
            'Cotizacion_Pactada_Salud',
            'Cotizacion_Voluntaria_Salud_Pesos',
            'Cotizacion_Voluntaria_Salud_Uf',
            'Pago_Isapre_Proporcional',
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
            'Colacion',
            'Movilizacion',
            'Perdida_Caja',
            'Desgaste_Herramientas',
            'Trabajo_Remoto',
            'Banco_Deposito',
            'Tipo_Cuenta',
            'Nro_Cuenta',
            ]
