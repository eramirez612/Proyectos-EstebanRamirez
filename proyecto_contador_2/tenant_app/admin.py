from django.contrib import admin
from tenant_app.models import Empleado, Datos_Empleado

# Register your models here.
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('__all__',)
