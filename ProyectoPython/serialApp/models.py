from django.db import models

# Create your models here.

class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    fecha_inicio = models.DateField()
    responsable = models.CharField(max_length=50)
    prioridad = models.IntegerField()
    imagen = models.ImageField(upload_to="projects/", null=True)




class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=20)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=50)




