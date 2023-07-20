from import_export import resources
from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import *

# Register your models here.

class RegistroResource(resources.ModelResource):
    fields = (
        'id',
        'nombre',
        'departamento',
        'marca_modelo',
        'serial_number',
        'tipo_dispositivo')
    class Meta:
        model = Registro_Equipo

@admin.register(Registro_Equipo)
class RegistroAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = RegistroResource
    list_display = ('id','nombre', 'departamento', 'marca_modelo', 'serial_number', 'tipo_dispositivo')
    ordering = ('nombre','departamento',)
    search_fields = ('nombre','departamento','serial_number',)
    list_filter = ('departamento', 'tipo_dispositivo',)
    list_per_page = 20