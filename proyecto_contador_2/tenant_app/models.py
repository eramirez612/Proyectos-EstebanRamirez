from django.db import models

# Create your models here.

status_choices = [
    ('--Seleccion Estado--', '--Seleccion Estado--'),
    ('Activo', 'Activo'),
    ('Inactivo', 'Inactivo'),
]

contract_choices = [
    ('--Seleccion Contrato--', '--Seleccion Contrato--'),
    ('Plazo Fijo', 'Plazo Fijo'),
    ('Part Time', 'Part Time'),
    ('Por Faena', 'Por Faena'),
    ('Contrato Indefinido', 'Contrato Indefinido'),
    ('Contrato para Practicante', 'Contrato para Practicante'),
    ('Contrato para extranjero', 'Contrato para extranjero'),
    ('Contrato para arte y espectaculo', 'Contrato para arte y espectaculo'),
    ('Contrato por honorarios', 'Contrato por honorarios'),
]

payment_choices = [
    ('--Metodo Pago--', '--Metodo Pago--'),
    ('Efectivo', 'Efectivo'),
    ('Transferencia Bancaria', 'Transferencia Bancaria'),
]

class Empleado(models.Model):
    rut = models.CharField(max_length=9, primary_key=True)
    nombre = models.CharField(max_length=100)
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
    metodo_pago = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=payment_choices,
        default=1
    )

