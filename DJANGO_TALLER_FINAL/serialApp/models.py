from django.db import models

# Create your models here.

inscripcion_estado = [
    ('Reservada', 'Reservada'),
    ('Completada', 'Completada'),
    ('Anulada', 'Anulada'),
    ('No asisten', 'No asisten'),
]

class Inscritos(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=50)
    institucion = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechareserva = models.DateField()
    horareserva = models.TimeField(auto_now_add=True)
    
    estado = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=inscripcion_estado,
        default=1
    )
    
    def __str__(self):
        return self
    
    observacion = models.CharField(blank=True, max_length=100)
    
class Instituciones(models.Model):
    id = models.AutoField(primary_key=True)
    institucion = models.CharField(max_length=20)