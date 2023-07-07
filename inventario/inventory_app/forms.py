from django import forms
from .models import *


class FormEquipo(forms.ModelForm):
    nombre = forms.CharField(max_length=128)
    serial_number = forms.CharField(max_length=128, required=True)
    nombre_y_modelo = forms.CharField(max_length=128)
    correo = forms.EmailField(required=False)
    contraseña = forms.CharField(max_length=128)
    tipo_licencias_windows = forms.SelectMultiple()
    nro_licencia_windows = forms.CharField(max_length=128)
    tipo_licencias_office = forms.SelectMultiple()
    nro_licencia_office = forms.CharField(max_length=128)
    tipo_dispositivo = forms.SelectMultiple()


    class Meta:
        model = Registro_Equipo
        fields = '__all__'