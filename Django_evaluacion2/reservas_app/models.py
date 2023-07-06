
from django.db import models

# Create your models here.

reserva_estado = [
    ('Reservado', 'Reservado'),
    ('Completada', 'Completada'),
    ('Anulada', 'Anulada'),
    ('No asisten', 'No asisten'),
]

class reserva(models.Model):
    
    reservante = models.CharField(max_length=50)
    telefono = models.IntegerField()
    fechareserva = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=reserva_estado,
        default=1
    )
    
    def __str__(self):
        return self
    
    numeropersonas = models.IntegerField()
    observacion = models.CharField(max_length=100)