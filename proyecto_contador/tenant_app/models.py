from django.db import models

# Create your models here.

status_choices = [
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
]

contract_choices = [
    ('Por Faena', 'Por Faena'),
    ('Plazo Fijo', 'Plazo Fijo'),
    ('Part Time', 'Part Time'),
    ('Contrato Indefinido', 'Contrato Indefinido'),
    ('Contrato para Practicante', 'Contrato para Practicante'),
    ('Contrato para extranjero', 'Contrato para extranjero'),
    ('Contrato para arte y espectaculo', 'Contrato para arte y espectaculo'),
    ('Contrato por honorarios', 'Contrato por honorarios'),
]

payment_choices = [
    ('Efectivo', 'Efectivo'),
    ('Transferencia Bancaria'),
]

class Empleados(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=9)
    fecha_ingreso = models.DateField()
    fecha_termino = models.DateField()
    estado = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=status_choices,
        default=1
    )

    contrato = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=contract_choices,
        default=1
    )
    


