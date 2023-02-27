from django.contrib import admin
from tenant_app.models import Empleado, Datos_Empleado, Libro_Rem_Electronico

# Register your models here.
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Rut',
                    'Nombres',
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


@admin.register(Libro_Rem_Electronico)
class Libro_Rem_ElectronicoAdmin(admin.ModelAdmin):
    list_display = ('Tipo_Jornada_Trabajo',
                    'Profesional',)

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('ID',
                    'Datos_Empleado',)
    