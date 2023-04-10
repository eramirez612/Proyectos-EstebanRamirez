from django.contrib import admin
from tenant_app.models import *

# Register your models here.
class RegimenAdmin(admin.StackedInline):
    model = Regimen_Provisional
    extra = 1
    max_num = 1
    fields = (
            'Regimen_Provisional',
            'Afp',
            'Ahorro_imponible',
            'Puesto_Trabajo_Pesado',
            'Cotizacion_Trabajo_Pesado',
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
            'Nro_Fun_Incorporacion',
            'Moneda_Plano_Salud',
            'Cotizacion_Pactada_Salud',
            'Cotizacion_Voluntaria_Salud_Pesos',
            'Cotizacion_Voluntaria_Salud_Uf',
            'Pago_Isapre_Proporcional',
    )


class LiquidacionAdmin(admin.StackedInline):
    model = Liquidacion
    extra = 1
    max_num = 1
    fields = (
            'Tipo_Trabajador',
            'Tipo_Sueldo',
            'Forma_Pago_Sueldo',
            'Horas_Semanales',
            'Informar_Horas_Trabajadas',
            'Forma_Calculo_Sueldo',
            'Monto_Calculo_Sueldo',
            'Centro_Costo',
            'Valor_Hora_Normal',
            'Valor_Dia_Normal',
            'Valor_Recargo_Dominical',
            'Duracion_Contrato',
            'Fecha_Ingreso',
            'Fecha_Termino',
            'Posee_Seguro_Cesantia',
            'Ingreso_Seguro_Cesantia',
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

@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Datos_Empleado',)

@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    inlines = [
        RegimenAdmin, 
        ApvAdmin,
        SaludAdmin, 
        LiquidacionAdmin, 
        No_ImponiblesAdmin,
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
        'Labor_en_Liquidacion',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tipo_Jornada_Trabajo',
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
        'Labor_en_Liquidacion',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tipo_Jornada_Trabajo',
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
        'Labor_en_Liquidacion',
        'Celular',
        'Email',
        'Pensionado_por_Invalidez',
        'Profesional',
        'Tipo_de_impuesto_unico',
        'Descuento_Prestamo_SII',
        'Tipo_Jornada_Trabajo',
        'Tecnico_Extranjero',
    )