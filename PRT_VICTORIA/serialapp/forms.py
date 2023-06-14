from django import forms
from django.core.validators import *
from serialapp.models import reserva

class DateInput(forms.DateInput):
    input_type = 'date'

class FormReservas(forms.ModelForm):
    
    reservante = forms.CharField(min_length=3, max_length=50)

    rut = forms.CharField(validators=[MinLengthValidator(9, 'Debe tener 9 digitos sin puntos ni guion'), MaxLengthValidator(9, 'Debe tener 9 digitos sin puntos ni guion')], required=True)

    telefono = forms.CharField(validators=[MinLengthValidator(9, 'Debe ser en el siguiente formato 91111111'), MaxLengthValidator(9, 'Debe ser en el siguiente formato 91111111')], required=True)

    fecha_reserva = forms.DateField(widget=DateInput, required=True)

    patente = forms.CharField(validators=[MinLengthValidator(5, 'Ingrese una patente válida'), MaxLengthValidator(6, 'Ingrese una patente válida')], required=True)
    
    class Meta:
        model = reserva
        fields = 'reservante','rut','patente','telefono','fecha_reserva','horario', 
    