from django.db import models
from tenant_app.listas import *

# Create your models here.


class Datos_Empleado(models.Model):
    Rut = models.CharField(max_length=9, primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateField(null=True)
    Sexo = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices=sex_choices,
        default=1
    )
    Estado_civil = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices=civil_status_choices,
        default=1
    )
    Nacionalidad = models.CharField(blank=True, null=True, max_length=50)
    Numero_De_Pasaporte = models.CharField(blank=True,max_length=10)
    Labor_en_Liquidacion = models.CharField(blank=True,max_length=50)
    Celular = models.CharField(max_length=9)
    Email = models.EmailField(blank=True, null=True)
    Pensionado_por_Invalidez = models.BooleanField()
    Profesional = models.BooleanField()
    Tipo_de_impuesto_unico = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices=taxes_choices,
        default=1
    )
    Descuento_Prestamo_SII = models.BooleanField()
    
    Tipo_Jornada_Trabajo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= work_choices,
        default= 1
    )
    Tecnico_Extranjero = models.BooleanField(default=False)
    #Regimen Provisional
    Regimen_Provisional = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= regimen,
        default= 1
    )
    Afp = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= afp,
        default= 1
    )
    Ahorro_imponible = models.DecimalField(max_digits=10, decimal_places=1)
    Puesto_Trabajo_Pesado = models.CharField(max_length=100)
    Cotizacion_Trabajo_Pesado = models.DecimalField(max_digits=10, decimal_places=1)
    #AFP
    Ahorro_Voluntario_Afp = models.IntegerField()
    Desea_APV = models.BooleanField()
    #APV
    Institucion_Apv = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= lista_institucion_apv,
        default= 1
    )
    Nro_Contrato_Apv = models.CharField(max_length=100)
    Forma_Pago_Apv = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= pago_apv,
        default= 1
    )
    Regimen_Apv = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= regimen_apv,
        default= 1
    )
    Ahorro_Pesos = models.DecimalField(max_digits=10, decimal_places=1)
    Ahorro_UF = models.DecimalField(max_digits=10, decimal_places=1)
    Deposito_Convenido = models.DecimalField(max_digits=10, decimal_places=1)
    #IPS
    Ex_caja = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= ex_caja,
        default= 1
    )
    Tasa_Ex_caja = models.DecimalField(max_digits=10, decimal_places=1)
    #Salud
    Institucion_Salud = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= institucion_salud,
        default= 1
    )
    Nro_Fun_Incorporacion = models.CharField(max_length=100)
    Moneda_Plano_Salud = models.DecimalField(max_digits=10, decimal_places=1)
    Cotizacion_Pactada_Salud = models.DecimalField(max_digits=10, decimal_places=1)
    Cotizacion_Voluntaria_Salud_Pesos = models.DecimalField(max_digits=10, decimal_places=1)
    Cotizacion_Voluntaria_Salud_Uf = models.DecimalField(max_digits=10, decimal_places=1)
    Pago_Isapre_Proporcional = models.BooleanField()
    #Liquidacion 
    Tipo_Trabajador = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tipo_trabajador,
        default= 1
    )
    Tipo_Sueldo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tipo_sueldo,
        default= 1
    )
    Forma_Pago_Sueldo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= forma_pago_sueldo,
        default= 1
    )
    Horas_Semanales = models.IntegerField()
    Informar_Horas_Trabajadas = models.BooleanField()
    Forma_Calculo_Sueldo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= forma_calculo_sueldo,
        default= 1
    )
    Monto_Calculo_Sueldo = models.DecimalField(max_digits=10, decimal_places=1)
    Centro_Costo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= centro,
        default= 1
    ) #Agregar opcion de añadir centros a centro costo con un boton y formulario
    Valor_Hora_Normal = models.DecimalField(max_digits=10, decimal_places=1)
    Valor_Dia_Normal = models.DecimalField(max_digits=10, decimal_places=1)
    Valor_Recargo_Dominical = models.DecimalField(max_digits=10, decimal_places=1)
    Duracion_Contrato = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= duracion_contrato,
        default= 1
    )
    Fecha_Ingreso = models.DateField(null=True)
    Fecha_Termino = models.DateField(null=True)
    Posee_Seguro_Cesantia = models.BooleanField()
    Ingreso_Seguro_Cesantia = models.DateField(null=True)
    #Forma de pago
    Banco_Deposito = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= banco,
        default= 1
    )
    Tipo_Cuenta = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tipo_cuenta,
        default= 1
    )
    Nro_Cuenta = models.CharField(max_length=50)


class Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    Datos_Empleado = models.ForeignKey(Datos_Empleado, on_delete=models.CASCADE, blank=True, null=True,)

class Nuevo_Centro_Costo(models.Model):
    Descripcion = models.CharField(max_length=400)
    Es_Primario = models.BooleanField()
    Codigo_Previred = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=50)
    Sucursal_eboleta = models.CharField(max_length=100)

class No_Imponibles(models.Model):
    Colacion = models.DecimalField(max_digits=10, decimal_places=1)
    Movilizacion = models.DecimalField(max_digits=10, decimal_places=1)
    Perdida_Caja = models.DecimalField(max_digits=10, decimal_places=1)
    Desgaste_Herramientas = models.DecimalField(max_digits=10, decimal_places=1)
    Trabajo_Remoto = models.DecimalField(max_digits=10, decimal_places=1)

class Nueva_Carga_Familiar(models.Model):
    Inicio_Beneficio = models.DateField(null=True)
    Termino_Beneficio = models.DateField(null=True)
    Rut_Beneficiario = models.CharField(max_length=50)
    Nombres = models.CharField(max_length=100)
    Apellido_Paterno = models.CharField(max_length=100)
    Apellido_Materno = models.CharField(max_length=100)
    Folio_Ips = models.CharField(max_length=100)
    Fecha_Nacimiento = models.DateField(null=True)
    Sexo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= sex_choices,
        default= 1
    )
    Tipo_Beneficio = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= beneficios,
        default= 1
    )

class Nuevo_Tramo_AF(models.Model):
    Tramo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tramo,
        default= 1
    )
    Fecha_Desde = models.DateField(null=True)
    Fecha_Hasta = models.DateField(null=True)

class Nuevo_Haber_Permanente(models.Model):
    Fecha_Inicio = models.DateField(null=True)
    Fecha_Termino = models.DateField(null=True)
    Descripcion_Haber = models.CharField(max_length=300)
    Monto = models.DecimalField(max_digits=10, decimal_places=1)
    Es_Proporcional = models.BooleanField()
    Es_Imponible = models.BooleanField()
    Es_Gratificable = models.BooleanField()
    Es_Tributable = models.BooleanField()

class Nuevo_Descuento_Permanente(models.Model):
    #nombre y/o rut del empleado 
    Persona = models.CharField(max_length=222)
    Causa_Descuento = models.DecimalField(max_digits=10, decimal_places=1)
    Monto = models.DecimalField(max_digits=10, decimal_places=1)
    Inicio = models.DateField(null=True)
    Termino = models.DateField(null=True)

class Datos_Para_Contrato(models.Model):
    Plantilla_Contrato = models.CharField(
        max_length=500,
        null=False, blank=False,
        #choices= ,
        default= 1
    )
    Comuna_Documento = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= Comunas,
        default= 1
    )
    Fecha_Documento = models.DateField(null=True)
    Labor = models.CharField(
        max_length=500,
        null=False, blank=False,
        #choices= ,
        default= 1
    )#agregar boton para añadir labor con formulario
    Texto_Labor = models.CharField(max_length=600)
    Lugares_Trabajo = models.CharField(
        max_length=500,
        null=False, blank=False,
        #choices= ,
        default= 1
    )#agregar boton para añadir lugar de trabajo con formulario
    Jornada = models.CharField(max_length=100) #agregar boton para añadir jornada con formulario

class Nueva_Jornada(models.Model):
    Hora_Inicio_1er_Bloque = models.TimeField()
    Hora_Termino_1er_Bloque = models.TimeField()
    Tiempo_Colacion = models.TimeField()
    Hora_Inicio_2do_Bloque = models.TimeField()
    Hora_Termino_2do_Bloque = models.TimeField()
    #Dias_Semana = agregar manera de seleccionar dias de la semana


#Modelos empresa

class Datos_basicos(models.Model):
    Rut_Empresa = models.CharField(max_length=9, primary_key=True)
    Nombre_Empresa = models.CharField(max_length=100)
    Logotipo = models.ImageField(upload_to='logos')
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Giro = models.IntegerField()
    Fecha_Constitucion = models.DateField(null=True)
    Notas = models.CharField(max_length=500)

class Representante(models.Model):
    Rut_Representante = models.CharField(max_length=9, primary_key=True)
    Nombre_Representante = models.CharField(max_length=100)
    Email_Representante = models.CharField(max_length=100)
    Direccion = models.EmailField(blank=True, null=True)
    Estado_Civil = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= civil_status_choices,
        default=1
    )
    Nacionalidad = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= Nacionalidades,
        default=1
    )

    Incluir_Pie_Firma_Liquidacion = models.BooleanField()
    Imagen_Firma_Representante_Legal = models.ImageField(upload_to='firma')

class Contabilidad(models.Model):
    Codigo_Actividad_SII_Primario =  models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= Lista_SII,
        default=1
    )
    Derecho_Credito_Fiscal = models.BooleanField()
    Modo_Numeracion_Asientos = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= lista_numeracion_asientos,
        default=1
    )
    Dias_Pago = models.IntegerField()
    Usa_Auxiliar = models.BooleanField()

class Sueldos(models.Model):
    Mutual_de_accidentes = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= mutual,
        default=1
    )
    Mutualidad = models.DecimalField(max_digits=10, decimal_places=1)
    Adicional_Mutualidad = models.DecimalField(max_digits=10, decimal_places=1)
    Modo_Gratificacion = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= gratificacion,
        default=1
    )
    Caja_Compensacion = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= compensacion,
        default=1
    )
    Utiliza_Recargo_Dominical = models.BooleanField()
    Detallar_Inasistencia_en_liquidacion = models.BooleanField()
    Informacion_Libro_Remuneraciones = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices= remuneraciones,
        default=1
    )
    Solicita_Bonificacion_Zona_Extrema = models.BooleanField()
    Informar_Datos_Hora_Extra = models.BooleanField()
    Informar_Vacaciones = models.BooleanField()
