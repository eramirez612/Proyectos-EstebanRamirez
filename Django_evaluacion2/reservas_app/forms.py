from django import forms
from reservas_app.models import reserva

class FormReservas(forms.ModelForm):
    
    reservante = forms.CharField(min_length=3, max_length=50)
    telefono = forms.CharField(min_length=9, max_length=9)
    fechareserva = forms.DateField()
    horareserva = forms.TimeField()
    numeropersonas = forms.IntegerField(min_value=1, max_value=15)
    observacion = forms.CharField(required=False)
    
    class Meta:
        model = reserva
        fields = 'reservante','telefono','fechareserva','horareserva','estado','numeropersonas','observacion'
    

