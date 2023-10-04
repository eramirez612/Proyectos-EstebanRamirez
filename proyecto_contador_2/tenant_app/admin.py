from django.contrib import admin
from tenant_app.models import *

# Register your models here.
class Asignacion_FamiliarAdmin(admin.StackedInline):
    model = Asignacion_Familiar
    extra = 1 
    fields = (
        'Tramo',
        'Cargas_simples',
        'Cargas_maternales',
        'Cargas_por_invalidez',
        'Monto_retroactivo',
        'Monto_reintegro',
    )


class DescuentosAdmin(admin.StackedInline):
    model = Descuentos
    extra = 1
    fields = (
        'Descuento',
        'Valor',
        )


class AdicionalesAdmin(admin.StackedInline):
    model = Adicionales
    extra = 1
    fields = (
        'Adicional',
        'Tipo_de_Bono',
        'Valor',
        )

class RegimenAdmin(admin.StackedInline):
    model = Regimen_Provisional
    extra = 1
    max_num = 1
    fields = (
            'Regimen_Provisional',
            'Afp',
            'Ahorro_imponible',
            'Ahorro_Voluntario_Afp',
            'Desea_APV',
            'Ex_caja',
            'Tasa_Ex_caja',
        )

class ApvAdmin(admin.StackedInline):
    model = APV
    extra = 1
    max_num = 1
    fields = (
            'Institucion_Apv',
            'Nro_Contrato_Apv',
            'Forma_Pago_Apv',
            'Regimen_Apv',
            'Ahorro_Pesos',
            'Ahorro_UF',
            'Deposito_Convenido',
    )


class SaludAdmin(admin.StackedInline):
    model = Salud
    extra = 1
    max_num = 1
    fields = (
            'Institucion_Salud',
            'Plan_UF',
    )

class No_ImponiblesAdmin(admin.StackedInline):
    model = No_Imponibles
    extra = 1
    max_num = 1
    fields = (
            'Colacion',
            'Movilizacion',
            'Perdida_Caja',
            'Desgaste_Herramientas',
            'Trabajo_Remoto',
    )


class PagoAdmin(admin.StackedInline):
    model = Forma_de_pago
    extra = 1
    max_num = 1
    fields = (
            'Banco_Deposito',
            'Tipo_Cuenta',
            'Nro_Cuenta',
    )

@admin.register(Liquidacion)
class LiquidacionAdmin(admin.ModelAdmin):
    inlines = [
        RegimenAdmin, 
        ApvAdmin,
        SaludAdmin,  
        AdicionalesAdmin,
        DescuentosAdmin,
        No_ImponiblesAdmin,
        ]
    extra = 1
    fields = (
            'Datos_Empleado',
            'Fecha_Emision',
            'Profesion',
            'Tipo_Trabajador',
            'Sin_Seguro_Cesantia',
            'Trabajador_Agricola',
            'Director_de_Empresa',
            'Sueldo_Base',
            'Tipo_Contrato',
            'Tipo_Jornada_Trabajo',
            'Dias_Descontados',
            'Dias_Licencia',
    )

@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    inlines = [
        PagoAdmin, 
        ]
    
    fields = (
        'Rut',
        'Nombres',
        'Apellidos',
        'Direccion',
        'Comuna',
        'Fecha_Nacimiento',
        'Sexo',
        'Estado_civil',
        'Nacionalidad',
        'Numero_De_Pasaporte',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tecnico_Extranjero',
    )

    list_display = (
        'Rut',
        'Nombres',
        'Apellidos',
        'Direccion',
        'Comuna',
        'Fecha_Nacimiento',
        'Sexo',
        'Estado_civil',
        'Nacionalidad',
        'Numero_De_Pasaporte',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tecnico_Extranjero',
    )
    
    search_fields = ('Rut', 'Nombres','Apellidos',)
    
    list_filter = ('Comuna', 'Sexo', 'Nacionalidad',)

    list_per_page = 10
    
    list_editable = (
        'Nombres',
        'Apellidos',
        'Direccion',
        'Comuna',
        'Fecha_Nacimiento',
        'Sexo',
        'Estado_civil',
        'Nacionalidad',
        'Numero_De_Pasaporte',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tecnico_Extranjero',
    )