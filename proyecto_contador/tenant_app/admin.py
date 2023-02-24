from django.contrib import admin
from tenant_app.models import Empleado

# Register your models here.

@admin.register(Empleado)
class EmpleadosAdmin(admin.ModelAdmin):
    list_display = ('rut','nombre','fecha_ingreso','fecha_termino','estado','contrato','metodo_pago',)

