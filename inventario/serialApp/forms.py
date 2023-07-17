from django import forms
from serialApp.models import *

class FormEquipo(forms.ModelForm):

    class Meta:
        model = Registro_Equipo
        fields = '__all__'