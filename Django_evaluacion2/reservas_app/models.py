from secrets import choice
from turtle import title
from django.db import models
from numpy import product

# Create your models here.

reserva_estado = [
    (1, 'Reservado'),
    (2, 'Completada'),
    (3, 'Anulada'),
    (4,'No asisten'),
]

class reserva(models.Model):
    
    reservante = models.CharField(max_length=50)
    telefono = models.CharField(max_length=20)
    fechareserva = models.DateField()
    horareserva = models.TimeField()
    
    estado = models.IntegerField(
        null=False, blank=False,
        choices=reserva_estado
    )
    
    def __str__(self):
        return self.tittle
    
    numeropersonas = models.IntegerField()
    observacion = models.CharField(max_length=100)