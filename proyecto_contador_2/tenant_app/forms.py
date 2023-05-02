from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import inlineformset_factory
from django.core.validators import *
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
    Rut = forms.CharField(validators=[MinLengthValidator(9, 'Debe tener 9 digitos y con guion'), MaxLengthValidator(9, 'Debe tener 9 digitos y con guion')], required=True)
    Nombres = forms.CharField(validators=[MinLengthValidator(3, 'Minimo de caracteres 3'), MaxLengthValidator(100, 'Maximo de caracteres 100')], required=True)
    Apellidos = forms.CharField(validators=[MinLengthValidator(3, 'Minimo de caracteres 3'), MaxLengthValidator(100, 'Maximo de caracteres 100')], required=True)
    Direccion = forms.CharField(validators=[MinLengthValidator(5, 'Minimo de caracteres 5'), MaxLengthValidator(100, 'Maximo de caracteres 100')], required=True)
    Comuna = forms.ChoiceField(choices=Comunas, required=True)
    Fecha_Nacimiento = forms.DateField(widget=DateInput)
    Sexo = forms.ChoiceField(required=True, choices=sex_choices)
    Estado_civil = forms.ChoiceField(required=True, choices=civil_status_choices)
    Nacionalidad = forms.ChoiceField(required=True,choices=Nacionalidades)
    Numero_De_Pasaporte = forms.CharField(validators=[MinLengthValidator(3, 'Minimo de caracteres 3'), MaxLengthValidator(100, 'Maximo de caracteres 100')], required=False)
    Celular = forms.IntegerField(validators=[MinLengthValidator(9, 'Debe ser en el siguiente formato 91111111'), MaxLengthValidator(9, 'Debe ser en el siguiente formato 91111111')], required=True)
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
            'Celular',
            'Email',
            'Pensionado_por_Invalidez',
            'Profesional',
            'Tipo_de_impuesto_unico',
            'Descuento_Prestamo_SII',
            'Tipo_de_Jornada_Trabajo',
            'Tecnico_Extranjero',
            ]
        
    def clean_comuna(self):
        Comuna = self.cleaned_data.get('Comuna')
        if Comunas in Comuna:
            return Comuna
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_sexo(self):
        Sexo = self.cleaned_data.get('Sexo')
        if sex_choices in Sexo:
            return Sexo
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_estado_civil(self):
        Estado_civil = self.cleaned_data.get('Estado_civil')
        if civil_status_choices in Estado_civil:
            return Estado_civil
        else: 
            raise forms.ValidationError('Error en select')

    def clean_nacionalidad(self):
        Nacionalidad = self.cleaned_data.get('Nacionalidad')
        if Nacionalidades in Nacionalidad:
            return Nacionalidad
        else: 
            raise forms.ValidationError('Error en select')
        
    def clean_tipo_de_impuesto_unico(self):
        Tipo_de_impuesto_unico = self.cleaned_data.get('Tipo_de_impuesto_unico')
        if taxes_choices in Tipo_de_impuesto_unico:
            return Tipo_de_impuesto_unico
        else:
            raise forms.ValidationError('Error en select')

class RegimenForm(forms.ModelForm):
    Regimen_Provisional = forms.ChoiceField(choices=regimen)
    Afp = forms.ChoiceField(choices=afp)
    Ahorro_imponible = forms.DecimalField(validators=[MinValueValidator(0)], required=False)
    #AFP
    Ahorro_Voluntario_Afp = forms.DecimalField(validators=[MinValueValidator(0)], required=False)
    Desea_APV = forms.BooleanField(required=False)
    #IPS 
    Ex_caja = forms.ChoiceField(choices=ex_caja, required=False)
    Tasa_Ex_caja = forms.DecimalField(validators=[MinValueValidator(0)], required=False)

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

    def clean_regimen_provisional(self):
        Regimen_Provisional = self.cleaned_data.get('Regimen_Provisional')
        if regimen in Regimen_Provisional:
            return Regimen_Provisional
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_afp(self):
        Afp = self.cleaned_data.get('Afp')
        if afp in Afp:
            return Afp
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_ex_caja(self):
        Ex_caja = self.cleaned_data.get('Ex_caja')
        if ex_caja in Ex_caja:
            return ex_caja
        else:
            raise forms.ValidationError('Error en select')

class ApvForm(forms.ModelForm):
    Institucion_Apv = forms.ChoiceField(choices=lista_institucion_apv)
    Nro_Contrato_Apv = forms.CharField(required=False)
    Forma_Pago_Apv = forms.ChoiceField(choices=pago_apv)
    Regimen_Apv = forms.ChoiceField(choices=regimen_apv)
    Ahorro_Pesos = forms.DecimalField(validators=[MinValueValidator(0)], required=False)
    Ahorro_UF = forms.DecimalField(validators=[MinValueValidator(0)], required=False)
    Deposito_Convenido = forms.DecimalField(validators=[MinValueValidator(0)], required=False)
    
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

    def clean_institucion_apv(self):
        Institucion_Apv = self.cleaned_data.get('Institucion_Apv')
        if lista_institucion_apv in Institucion_Apv:
            return Institucion_Apv
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_forma_pago_apv(self):
        Forma_Pago_Apv = self.cleaned_data.get('Forma_Pago_Apv')
        if pago_apv in Forma_Pago_Apv:
            return Forma_Pago_Apv
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_regimen_apv(self):
        Regimen_Apv = self.cleaned_data.get('Regimen_Apv')
        if regimen_apv in Regimen_Apv:
            return Regimen_Apv
        else:
            raise forms.ValidationError('Error en select')

class SaludForm(forms.ModelForm):
    Institucion_Salud = forms.ChoiceField(choices=institucion_salud)
    Plan_UF = forms.DecimalField(validators=[MinValueValidator(0)], required=False)

    class Meta:
        model = Salud
        fields = [
            'Institucion_Salud',
            'Plan_UF',
        ]

    def clean_institucion_salud(self):
        Institucion_Salud = self.cleaned_data.get('Institucion_Salud')
        if institucion_salud in Institucion_Salud:
            return Institucion_Salud
        else:
            raise forms.ValidationError('Error en select')

class LiquidacionForm(forms.ModelForm):
    #Liquidacion
    Fecha_Emision = forms.DateField(widget=DateInput)
    #Profesion = forms.ChoiceField(choices=profesion, required=False)
    Tipo_Trabajador = forms.ChoiceField(choices=tipo_trabajador)
    Sin_Seguro_Cesantia = forms.BooleanField(required=False)
    Trabajador_Agricola = forms.BooleanField(required=False)
    Director_de_Empresa = forms.BooleanField(required=False)
    Sueldo_Base = forms.DecimalField(validators=[MinValueValidator(0)])
    Tipo_Contrato = forms.ChoiceField(choices=duracion_contrato)
    Tipo_Jornada_Trabajo = forms.ChoiceField(choices=work_choices)
    Dias_Descontados = forms.IntegerField(validators=[MinValueValidator(0)])
    Dias_Licencia = forms.IntegerField(validators=[MinValueValidator(0)])
    Cargas_Familiares = forms.BooleanField(required=False)

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

    def clean_tipo_trabajador(self):
        Tipo_Trabajador = self.cleaned_data.get('Tipo_Trabajador')
        if tipo_trabajador in Tipo_Trabajador:
            return Tipo_Trabajador
        else:
            raise forms.ValidationError('Error en select')
    
    def clean_tipo_contrato(self):
        Tipo_Contrato = self.cleaned_data.get('Tipo_Contrato')
        if duracion_contrato in Tipo_Contrato:
            return Tipo_Contrato
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_jornada_trabajo(self):
        Tipo_Jornada_Trabajo = self.cleaned_data.get('Tipo_Jornada_Trabajo')
        if work_choices in Tipo_Jornada_Trabajo:
            return Tipo_Jornada_Trabajo
        else:
            raise forms.ValidationError('Error en select')

class No_ImponiblesForm(forms.ModelForm):
    #No imponibles 
    Colacion = forms.DecimalField(validators=[MinValueValidator(0)])
    Movilizacion = forms.DecimalField(validators=[MinValueValidator(0)])
    Perdida_Caja = forms.DecimalField(validators=[MinValueValidator(0)])
    Desgaste_Herramientas = forms.DecimalField(validators=[MinValueValidator(0)])
    Trabajo_Remoto = forms.DecimalField(validators=[MinValueValidator(0)])

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

    def clean_banco_deposito(self):
        Banco_Deposito = self.cleaned_data.get('Banco_Deposito')
        if banco in Banco_Deposito:
            return Banco_Deposito
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_tipo_cuenta(self):
        Tipo_Cuenta = self.cleaned_data.get('Tipo_Cuenta')
        if tipo_cuenta in Tipo_Cuenta:
            return Tipo_Cuenta
        else:
            raise forms.ValidationError('Error en select')


class AdicionalesForm(forms.ModelForm):
    Adicional = forms.ChoiceField(choices=adicional)
    Tipo_de_Bono = forms.ChoiceField(choices=bonos)
    Valor = forms.DecimalField(validators=[MinValueValidator(0)])

    class Meta:
        model = Adicionales
        fields = [
            'Adicional',
            'Tipo_de_Bono',
            'Valor',
        ]

    def clean_adicional(self):
        Adicional = self.cleaned_data.get('Adicional')
        if adicional in Adicional:
            return Adicional
        else:
            raise forms.ValidationError('Error en select')
        
    def clean_tipo_de_bono(self):
        Tipo_de_Bono = self.cleaned_data.get('Tipo_de_Bono')
        if bonos in Tipo_de_Bono:
            return Tipo_de_Bono
        else:
            raise forms.ValidationError('Error en select')


class DescuentosForm(forms.ModelForm):
    Descuento = forms.ChoiceField(choices=descuento)
    Valor = forms.DecimalField(validators=[MinValueValidator(0)])
    
    class Meta:
        model = Descuentos
        fields = [
            'Descuento',
            'Valor',
        ]

    def clean_descuento(self):
        Descuento = self.cleaned_data.get('Descuento')
        if Descuento in Descuento:
            return Descuento
        else:
            raise forms.ValidationError('Error en select')
    
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

    def clean_movimiento_personal(self):
        Movimiento_Personal = self.cleaned_data.get('Moviemiento_Personal')
        if movimientos_personales in Movimiento_Personal:
            return Movimiento_Personal
        else:
            raise forms.ValidationError('Error en select')

class ImpuestoForm(forms.ModelForm):
    Factor_Impuesto_unico_primera_categoria = forms.DecimalField(validators=[MinValueValidator(0)])
    Cantidad_a_rebajar = forms.DecimalField(validators=[MinValueValidator(0)])

    class Meta:
        model = Impuesto
        fields = [
            'Factor_Impuesto_unico_primera_categoria',
            'Cantidad_a_rebajar',
        ]