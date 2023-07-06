from django.db import models
from serialApp.listas import *
from django.contrib.auth.hashers import make_password

#Modelo de la DB 

class Registro_Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=128)
    rut = models.CharField(max_length=9)
    departamento = models.CharField(
        max_length=100,
        null=False, blank=False,
        choices=depto_choices,
        default=1
    )
    serial_number = models.CharField(unique=True, max_length=128)
    marca = models.CharField(max_length=128)
    modelo = models.CharField(max_length=128)
    correo = models.EmailField()
    #Encriptacion de la contraseña
    contraseña = models.CharField(max_length=128)
    def save(self, *args, **kwargs):
        if self.contraseña:
            self.contraseña = make_password(self.contraseña)
        super().save(*args, **kwargs)
    #----------------------------------------------------------------#
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
    fecha_ingreso_del_registro = models.DateTimeField(auto_now_add=True)



    

