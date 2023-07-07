from django.db import models
from inventory_app.listas import * 

# Create your models here.

class Registro_Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)

    departamento = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=depto_choices,
        default=1
    )
    
    
    serial_number = models.CharField(max_length=128, unique=True)
    nombre_y_modelo = models.CharField(max_length=128)
    correo = models.EmailField(null=True, blank=True)
    contraseña = models.CharField(max_length=128)

    tipo_licencias_windows = models.CharField(
    max_length=100,
    null=False, blank=False,
    choices=windows_choices,
    default=1)
    
    nro_licencia_windows = models.CharField(max_length=100, unique=True)
#----------------------------------------------------------------#
    tipo_licencias_office = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=office_choices,
        default=1)
    
    nro_licencia_office = models.CharField(max_length=100, unique=True)
#----------------------------------------------------------------#

    tipo_dispositivo = models.CharField(
    max_length=100,
    null=False, blank=False,
    choices=dispositivo_choices,
    default=1)
    
    fecha_ingreso_del_registro = models.DateTimeField(auto_now_add=True)


