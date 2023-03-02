from django import forms
from tenant_app.models import Datos_Empleado

class DateInput(forms.DateInput):
    input_type = 'date'

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
    Pensionado_por_Invalidez = forms.BooleanField(required=True)
    Profesional = forms.BooleanField(required=False)
    Tipo_de_impuesto_unico = forms.CharField(required=True)
    Descuento_Prestamo_SII = forms.BooleanField(required=False)
    
    class Meta:
        model: Datos_Empleado
        fields = '__all__'
    