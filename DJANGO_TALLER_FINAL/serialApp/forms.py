from django import forms
from serialApp.models import Inscritos, Instituciones

class DateInput(forms.DateInput):
    input_type = 'date'

class FormInscritos(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=50)
    telefono = forms.IntegerField(min_value=900000000, max_value=999999999)
    fechareserva = forms.DateField(widget=DateInput)
    observacion = forms.CharField(required=False)
    
    class Meta:
        model = Inscritos
        fields = '__all__'

class FormInstituciones(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=20)
    
    class Meta:
        model = Instituciones
        fields = '__all__'
