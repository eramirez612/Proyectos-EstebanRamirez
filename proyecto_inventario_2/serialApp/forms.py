from django import forms
from serialApp.models import *

class FormEquipo(forms.ModelForm):
    # nombre = forms.CharField(min_length=3, max_length=128, required=True)
    # serial_number = forms.CharField(min_length=5, max_length=128, required=True)
    # marca = forms.CharField(min_length=2, max_length=128, required=False)
    # modelo = forms.CharField(min_length=2, max_length=128, required=False)
    # correo = forms.EmailField(required=False)
    # contraseña = forms.CharField(max_length=128, required=False)
    # tipo_licencia_windows = forms.SelectMultiple()
    # nro_licencia_windows = forms.CharField(min_length=10,max_length=100, required=False)
    # tipo_licencia_office = forms.SelectMultiple()
    # nro_licencia_office = forms.CharField(min_length=10, max_length=100, required=False)


    class Meta:
        model = Registro_Equipo
        fields = '__all__'