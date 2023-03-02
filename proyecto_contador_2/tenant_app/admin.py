from django.contrib import admin
from tenant_app.models import Datos_Empleado, Empleado

# Register your models here.
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Rut',
                    'Nombres',
                    'Apellidos',
                    'Direccion',
                    'Comuna',
                    'Fecha_Nacimiento',
                    'Sexo',
                    'Estado_civil',
                    'Nacionalidad',
                    'Numero_De_Pasaporte',
                    'Labor_en_Liquidacion',
                    'Celular',
                    'Email',
                    'Pensionado_por_Invalidez',
                    'Profesional',
                    'Tipo_de_impuesto_unico',
                    'Descuento_Prestamo_SII',)
    search_fields = ('Rut', 'Nombres','Apellidos',)
    
    list_filter = ('Comuna', 'Sexo', 'Nacionalidad',)
    
    list_editable = ('Nombres',
                    'Apellidos',
                    'Direccion',
                    'Comuna',
                    'Sexo',
                    'Estado_civil',
                    'Nacionalidad',
                    'Numero_De_Pasaporte',
                    'Labor_en_Liquidacion',
                    'Celular',
                    'Email',
                    'Pensionado_por_Invalidez',
                    'Profesional',
                    'Tipo_de_impuesto_unico',
                    'Descuento_Prestamo_SII',)



    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Datos_Empleado',)
