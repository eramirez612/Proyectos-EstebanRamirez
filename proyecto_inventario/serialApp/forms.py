from django import forms
from serialApp.models import *

class FormEquipo(forms.ModelForm):
    nombre = forms.CharField(min_length=3, max_length=128, required=True)
    rut = forms.CharField(min_length=8, max_length=9, required=True)
    serial_number = forms.CharField(min_length=9, max_length=11, required=True)
    marca = forms.CharField(min_length=2, max_length=128, required=True)
    modelo = forms.CharField(min_length=2, max_length=128, required=True)
    correo = forms.EmailField()
    contraseña = forms.CharField(max_length=128)
    tipo_licencia_windows = forms.SelectMultiple()
    nro_licencia_windows = forms.CharField(min_length=10,max_length=100, required=False)
    tipo_licencia_office = forms.SelectMultiple()
    nro_licencia_office = forms.CharField(min_length=10, max_length=100, required=False)


    class Meta:
        model = Registro_Equipo
        fields = '__all__'
