from django.contrib import admin
from tenant_app.models import Empleado, Datos_Empleado

# Register your models here.

@admin.register(Empleado)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','fecha_ingreso','fecha_termino','estado','contrato','metodo_pago',)
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    list_display = 
