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

sex_choices = [
    ('--Seleccione su genero--', '--Seleccione su genero--'),
    ('Masculino', 'Masculino'),
    ('Femenino', 'Femenino'),
    ('No binario', 'No binario'),
    ('Prefiero no decirlo', 'Prefiero no decirlo'),
]

taxes_choices = [
    ('--Seleccione el tipo de impuesto--', '--Seleccione el tipo de impuesto--'),
    ('Normal', 'Normal'),
    ('Trabajador Agricola', 'Trabajador Agricola'),
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

class Datos_Empleado(models.Model):
    Rut = models.CharField(max_length=9, primary_key=True)
    Nombres = models.CharField(max_length=100)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Sexo = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=sex_choices,
        default=1
    )
    Numero_De_Pasaporte = models.CharField(max_length=10)
    Labor_en_Liquidacion = models.CharField(max_length=50)
    Celular = models.IntegerField(max_length=9)
    Email = models.EmailField()
    Pensionado_por_Invalidez = models.BooleanField()
    Profesional = models.BooleanField()
    Tipo_de_impuesto_unico = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=taxes_choices,
        default=1
    )
    Descuento_Prestamo_SII = models.BooleanField()
