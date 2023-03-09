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
    Profesional = models.BooleanField()

class Empleado(models.Model):
    ID = models.AutoField(primary_key=True)
    Datos_Empleado = models.ForeignKey(Datos_Empleado, on_delete=models.CASCADE, blank=True, null=True,)

def __str__(self):
    return self.Rut

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
