from django import forms
from serialApp.models import Proyecto, User

class DateInput(forms.DateInput):
    input_type = 'date'
    

class ProyectoForm(forms.ModelForm):
    
    nombre = forms.CharField(min_length=3, max_length=50)
    fecha_inicio = forms.DateField(widget=DateInput)
    responsable = forms.CharField(min_length=3, max_length=50)
    prioridad = forms.IntegerField(min_value=1, max_value=10)
    imagen = forms.ImageField(required=False)
    
    
    class Meta:
        model = Proyecto
        fields = '__all__'

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'