from django import forms
from reservas_app.models import reserva

class FormReservas(forms.ModelForm):
    
    reservante = forms.CharField(min_length=3, max_length=50)
    telefono = forms.IntegerField(min_value=900000000, max_value=999999999)
    numeropersonas = forms.IntegerField(min_value=1, max_value=15)
    observacion = forms.CharField(required=False)
    
    class Meta:
        model = reserva
        fields = '__all__'
    

