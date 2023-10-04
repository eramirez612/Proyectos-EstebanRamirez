from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.


reserva_horario = [
    ('Mañana', 'Mañana'),
    ('Tarde', 'Tarde'),
]

class reserva(models.Model):
    
    reservante = models.CharField(max_length=50, unique=True)
    telefono = models.CharField(max_length=9, unique=True)
    patente = models.CharField(max_length=6, unique=True)
    rut = models.CharField(max_length=9, unique=True)
    fecha_reserva = models.DateField()
    
    horario = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=reserva_horario,
        default=1
    )
    
    def __str__(self):
        return self
    