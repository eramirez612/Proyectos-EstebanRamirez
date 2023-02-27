from django.contrib import admin
from tenant_app.models import Empleado, Datos_Empleado, Libro_Rem_Electronico

# Register your models here.
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('__all__',)

@admin.register(Libro_Rem_Electronico)
class Libro_Rem_ElectronicoAdmin(admin.ModelAdmin):
    list_display = ('__all__',)
