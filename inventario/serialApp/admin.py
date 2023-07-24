from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter
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
        'tipo_dispositivo',
        'fecha_ingreso_del_registro',)
    class Meta:
        model = Registro_Equipo

@admin.register(Registro_Equipo)
class RegistroAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('id','nombre', 'departamento', 'marca_modelo', 'serial_number', 'tipo_dispositivo', 'fecha_ingreso_del_registro',)
    ordering = ('-fecha_ingreso_del_registro','departamento',)
    search_fields = ('nombre','departamento','serial_number','fecha_ingreso_del_registro',)
    list_filter = (('fecha_ingreso_del_registro',DateRangeFilter),'departamento','tipo_dispositivo',)
    list_per_page = 20