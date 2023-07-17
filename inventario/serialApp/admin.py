from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Registro_Equipo)
class RegistroAdmin(admin.ModelAdmin):
    list_display = ('id','nombre', 'departamento', 'marca_modelo', 'serial_number', 'tipo_dispositivo')
    ordering = ('nombre','departamento',)
    search_fields = ('nombre','departamento','serial_number',)
    list_filter = ('departamento',)
    list_per_page = 20