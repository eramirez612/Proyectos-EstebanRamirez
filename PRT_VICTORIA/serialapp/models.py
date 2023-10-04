from django.db import models

# Create your models here.

reserva_horario = [
    ('Mañana', 'Mañana'),
    ('Tarde', 'Tarde'),
]

class reserva(models.Model):
    
    reservante = models.CharField(max_length=50)
    telefono = models.CharField(max_length=9)
    patente = models.CharField(max_length=6)
    rut = models.CharField(max_length=9)
    fecha_reserva = models.DateField()
    
    horario = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=reserva_horario,
        default=1
    )
    
    def __str__(self):
        return self
    