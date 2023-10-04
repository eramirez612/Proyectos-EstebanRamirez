from django import forms
from serialApp.models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class FormEquipo(forms.ModelForm):
    
    fecha_de_compra = forms.DateTimeField(widget=DateInput)

    class Meta:
        model = Registro_Equipo
        fields = '__all__'