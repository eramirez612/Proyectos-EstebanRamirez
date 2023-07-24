from django.db import models
from serialApp.listas import *

#Modelo de la DB 

class Registro_Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    departamento = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=depto_choices,
        default=1
    )

    serial_number = models.CharField(unique=True, max_length=128)
    marca_modelo = models.CharField(max_length=128, null=True, blank=True)
    correo = models.EmailField(null=True, blank=True)
    contraseña = models.CharField(max_length=128, null=True, blank=True)
    #----------------------------------------------------------------#
    tipo_licencias_windows = models.CharField(
        max_length=100,
        null=False, blank=False, unique=False,
        choices=windows_choices,
        default=1)
    
    nro_licencia_windows = models.CharField(max_length=100, null=True, blank=True)
#----------------------------------------------------------------#
    tipo_licencias_office = models.CharField(
        max_length=100,
        null=False, blank=False, unique=False,
        choices=office_choices,
        default=1)
    
    nro_licencia_office = models.CharField(max_length=100, null=True, blank=True)
#----------------------------------------------------------------#

    tipo_dispositivo = models.CharField(
    max_length=100,
    null=False, blank=False, unique=False,
    choices=dispositivo_choices,
    default=1)
    
    fecha_de_compra = models.DateTimeField()

    def __str__(self):
        return self.nombre


