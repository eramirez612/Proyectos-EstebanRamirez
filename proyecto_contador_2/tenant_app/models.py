from django.db import models
from django.contrib.auth.models import User
from tenant_app.listas import *

# Create your models here.

class Datos_Empleado(models.Model):
    id = models.AutoField(primary_key=True)
    autor = models.ForeignKey(User, on_delete=models.CASCADE)
    Rut = models.CharField(max_length=9)
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
    Celular = models.CharField(max_length=9)
    Email = models.EmailField(blank=True, null=True)
    Pensionado_por_Invalidez = models.BooleanField(null=True, blank=True)
    Profesional = models.BooleanField(null=True, blank=True)
    Tipo_de_impuesto_unico = models.CharField(
        max_length = 500,
        null=False, blank=False,
        choices=taxes_choices,
        default=1
    )
    Descuento_Prestamo_SII = models.BooleanField(null=True, blank=True)

    Tecnico_Extranjero = models.BooleanField(default=False, null=True, blank=True)

    def __str__(self):
        return self.Rut
    
class Liquidacion(models.Model):
    Datos_Empleado = models.ForeignKey('Datos_Empleado', on_delete=models.CASCADE, blank=True, null=True,)
    Fecha_Emision = models.DateField(null=True, blank=True)
    Profesion = models.CharField(
        max_length=500,
        null=True, blank=True,
    )

    Tipo_Trabajador = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tipo_trabajador,
        default= 1
    )

    Sin_Seguro_Cesantia = models.BooleanField(null=True, blank=True)
    Trabajador_Agricola = models.BooleanField(null=True, blank=True)
    Director_de_Empresa = models.BooleanField(null=True, blank=True)

    Sueldo_Base = models.DecimalField(max_digits=10, decimal_places=1, blank=True)

    Tipo_Contrato = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= duracion_contrato,
        default= 1
    )

    Tipo_Jornada_Trabajo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= work_choices,
        default= 1
    )

    Dias_Descontados = models.IntegerField(null=True, blank=True)
    Dias_Licencia = models.IntegerField(null=True, blank=True)

class APV(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Institucion_Apv = models.CharField(
        max_length=500,
        null=True, blank=True,
        choices= lista_institucion_apv,
        default= 1
    )
    Nro_Contrato_Apv = models.CharField(max_length=100, null=True, blank=True)
    Forma_Pago_Apv = models.CharField(
        max_length=500,
        null=True, blank=True,
        choices= pago_apv,
        default= 1
    )
    Regimen_Apv = models.CharField(
        max_length=500,
        null=True, blank=True,
        choices= regimen_apv,
        default= 1
    )
    Ahorro_Pesos = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    Ahorro_UF = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    Deposito_Convenido = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)

class Regimen_Provisional(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Regimen_Provisional = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= regimen,
        default= 1
    )
    Afp = models.CharField(
        max_length=500,
        null=True, blank=True,
        choices= afp,
        default= 1
    )
    Ahorro_imponible = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    #AFP
    Ahorro_Voluntario_Afp = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)
    Desea_APV = models.BooleanField(null=True, blank=True)
    #IPS
    Ex_caja = models.CharField(
        max_length=500,
        null=True, blank=True,
        choices= ex_caja,
        default= 1
    )
    Tasa_Ex_caja = models.DecimalField(max_digits=10, decimal_places=1, null=True, blank=True)

class Salud(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Institucion_Salud = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= institucion_salud,
        default= 1
    )
    Plan_UF = models.DecimalField(max_digits=10, decimal_places=1, blank=True)


class No_Imponibles(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Colacion = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)
    Movilizacion = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)
    Perdida_Caja = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)
    Desgaste_Herramientas = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)
    Trabajo_Remoto = models.DecimalField(max_digits=10, decimal_places=1, default=0, null=True, blank=True)

class Forma_de_pago(models.Model):
    Datos_Empleado = models.ForeignKey('Datos_Empleado', on_delete=models.CASCADE, blank=True, null=True,)
    Banco_Deposito = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= banco,
        default= 1
    )# si se selecciona pago contado debe deshabilitar el campo nro cuenta
    Tipo_Cuenta = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tipo_cuenta,
        default= 1
    )
    Nro_Cuenta = models.CharField(max_length=50, blank=True)

class Adicionales(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Adicional = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= adicional,
        default= 1
    )
    Tipo_de_Bono = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= bonos,
        default= 1
    )
    Valor = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)

class Descuentos(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Descuento = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= descuento,
        default= 1
    )
    Valor = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)


class Movimiento_Personal(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Movimiento_Personal = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= movimientos_personales,
        default= 1
    )
    Fecha_Inicio = models.DateField(null=True)
    Fecha_Termino = models.DateField(null=True)

class Impuesto(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Factor_impuesto_unico_primera_categoria = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)
    Cantidad_a_rebajar = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)


class Asignacion_Familiar(models.Model):
    Liquidacion = models.ForeignKey('Liquidacion', on_delete=models.CASCADE, blank=True, null=True,)
    Tramo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= tramo,
        default= 1
    )
    Cargas_simples = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)
    Cargas_maternales = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)
    Cargas_por_invalidez = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)
    Monto_retroactivo = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)
    Monto_reintegro = models.DecimalField(max_digits=10, decimal_places=1, default=0, blank=True)


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


class Nueva_Jornada(models.Model):
    Hora_Inicio_1er_Bloque = models.TimeField()
    Hora_Termino_1er_Bloque = models.TimeField()
    Tiempo_Colacion = models.TimeField()
    Hora_Inicio_2do_Bloque = models.TimeField()
    Hora_Termino_2do_Bloque = models.TimeField()


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
