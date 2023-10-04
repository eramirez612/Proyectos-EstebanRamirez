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
        'fecha_de_compra',)
    class Meta:
        model = Registro_Equipo

@admin.register(Registro_Equipo)
class RegistroAdmin(ImportExportModelAdmin ,admin.ModelAdmin):
    list_display = ('id','nombre', 'departamento', 'marca_modelo', 'serial_number', 'tipo_dispositivo', 'fecha_de_compra',)
    ordering = ('-fecha_de_compra','departamento',)
    search_fields = ('nombre','departamento','serial_number','fecha_de_compra',)
    list_filter = (('fecha_de_compra',DateRangeFilter),'departamento','tipo_dispositivo',)
    list_per_page = 20