from django import forms
from django.core.validators import *
from serial_app.models import reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class FormReservas(forms.ModelForm):
    
    reservante = forms.CharField(min_length=3, max_length=50)

    rut = forms.CharField(min_length=8 ,max_length=9, required=True)

    telefono = forms.CharField(min_length=9, max_length=9)

    fecha_reserva = forms.DateField(widget=DateInput)

    patente = forms.CharField(min_length=5, max_length=6, required=True)
    
    class Meta:
        model = reserva
        fields = '__all__' 