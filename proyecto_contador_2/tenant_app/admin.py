from django.contrib import admin
from tenant_app.models import Datos_Empleado, Empleado

# Register your models here.
    
@admin.register(Datos_Empleado)
class Datos_EmpleadoAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Datos Basicos', {
            'fields':('Rut',
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
                    'Tecnico_Extranjero',),
        }),
        ('Regimen Provisional', {
            'fields':('Regimen_Provisional',
                      'Afp',
                      'Ahorro_imponible',
                      'Puesto_Trabajo_Pesado',
                      'Cotizacion_Trabajo_Pesado',),
        }),
        ('AFP',{
            'fields':('Ahorro_Voluntario_Afp',
                      'Desea_APV',),
        }),
        ('APV',{
            'fields':('Institucion_Apv',
                      'Nro_Contrato_Apv',
                      'Forma_Pago_Apv',
                      'Regimen_Apv',
                      'Ahorro_Pesos',
                      'Ahorro_UF',
                      'Deposito_Convenido',),
        }),
        ('IPS',{
            'fields':('Ex_caja',
                      'Tasa_Ex_caja',),
        }),
        ('Salud',{
            'fields':('Institucion_Salud',
                      'Nro_Fun_Incorporacion',
                      'Moneda_Plano_Salud',
                      'Cotizacion_Pactada_Salud',
                      'Cotizacion_Voluntaria_Salud_Pesos',
                      'Cotizacion_Voluntaria_Salud_Uf',
                      'Pago_Isapre_Proporcional',),
        }),
        ('Liquidacion',{
            'fields':('Tipo_Trabajador',
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
                      'Ingreso_Seguro_Cesantia',),
        }),
        ('No Imponibles',{
            'fields':('Colacion',
                      'Movilizacion',
                      'Perdida_Caja',
                      'Desgaste_Herramientas',
                      'Trabajo_Remoto',)
        }),
        ('Forma de pago',{
            'fields':('Banco_Deposito',
                      'Tipo_Cuenta',
                      'Nro_Cuenta',)
        })
    )


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
                    'Profesional',
                    'Tipo_Jornada_Trabajo',
                    'Tecnico_Extranjero',)
    
    search_fields = ('Rut', 'Nombres','Apellidos',)
    
    list_filter = ('Comuna', 'Sexo', 'Nacionalidad',)

    list_per_page = 10
    
    #list_editable = ('Nombres',
    #                'Apellidos',
    #                'Direccion',
    #                'Comuna',
    #                'Sexo',
    #                'Estado_civil',
    #                'Nacionalidad',
    #                'Numero_De_Pasaporte',
    #                'Labor_en_Liquidacion',
    #                'Celular',
    #                'Email',
    #                'Pensionado_por_Invalidez',
    #                'Profesional',
    #                'Tipo_de_impuesto_unico',
    #                'Descuento_Prestamo_SII',
    #                'Tipo_Jornada_Trabajo',
    #                'Tecnico_Extranjero',)



    
@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    list_display = ('Datos_Empleado',)
