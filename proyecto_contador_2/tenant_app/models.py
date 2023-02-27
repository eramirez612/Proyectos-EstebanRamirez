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

work_choices = [
    ('--Seleccione el tipo de jornada--', '--Seleccione el tipo de jornada--'),
    ('ORDINARIA - ART 22 (45 Horas)','ORDINARIA-ART 22 (45 Horas)'),
    ('PARCIAL - ART 40 BIS (30 Horas max)', 'PARCIAL-ART 40 BIS (30 Horas max)'),
    ('EXTRAORDINARIA - ART 30 (sobretiempo)','EXTRAORDINARIA-ART 30 (sobretiempo)'),
    ('ESPECIAL - ART 38 INCISO 5 (trabajo fuerza mayor)', 'ESPECIAL - ART 38 INCISO 5 (trabajo fuerza mayor)'),
    ('ESPECIAL - ART 23 (NAVIERO)', 'ESPECIAL - ART 23 (NAVIERO)'),
    ('ESPECIAL - ART 106 (NAVIERO)', 'ESPECIAL - ART 106 (NAVIERO)'),
    ('ESPECIAL - ART 152 TER D (tripulantes de vuelo)', 'ESPECIAL - ART 152 TER D (tripulantes de vuelo)'),
    ('ESPECIAL - ART 152 TER F (tripulantes de vuelo)', 'ESPECIAL - ART 152 TER F (tripulantes de vuelo)'),
    ('ESPECIAL - ART 25 (locomocion colectiva interurbana)', 'ESPECIAL - ART 25 (locomocion colectiva interurbana)'),
    ('ESPECIAL - ART 25 BIS (carga terrestre interurbana)', 'ESPECIAL - ART 25 BIS (carga terrestre interurbana)'),
    ('ESPECIAL - ART 149 (trabajadores de casa particular)', 'ESPECIAL - ART 149 (trabajadores de casa particular)'),
    ('ESPECIAL - ART 149 INCISO 2 (trabajadores de casa particular)','ESPECIAL - ART 149 INCISO 2 (trabajadores de casa particular)'),
    ('ESPECIAL - ART 152 BIS (cuerpos de bomberos)', 'ESPECIAL - ART 152 BIS (cuerpos de bomberos)'),
    ('ESPECIAL - ART 36 145-D (artes y espectaculos)', 'ESPECIAL - ART 36 145-D (artes y espectaculos)'),
    ('ESPECIAL - ART 22 INCISO FINAL (deportistas profesionales)', 'ESPECIAL - ART 22 INCISO FINAL (deportistas profesionales)'),
    ('BISEMANAL - ART 149 INCISO 2 (trabajadores de casa particular)', 'BISEMANAL - ART 149 INCISO 2 (trabajadores de casa particular)'),
    ('JORNADA EXCEPCIONAL - ART 38 INCISO FINAL (trabajo fuerza mayor)', 'JORNADA EXCEPCIONAL - ART 38 INCISO FINAL (trabajo fuerza mayor)'),
    ('EXENTA - ART 22 (sin limitacion de jornada)', 'EXENTA - ART 22 (sin limitacion de jornada)'),
]

civil_status_choices = [
    ('--Seleccione el estado civil--', '--Seleccione el estado civil--'),
    ('Soltero', 'Soltero'),
    ('Casado', 'Casado'),
    ('Divorciado', 'Divorciado'),
    ('Viudo', 'Viudo'),
]


class Datos_Empleado(models.Model):
    Rut = models.CharField(max_length=9, primary_key=True)
    Nombres = models.CharField(max_length=9)
    Apellidos = models.CharField(max_length=100)
    Direccion = models.CharField(max_length=100)
    Comuna = models.CharField(max_length=100)
    Sexo = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=sex_choices,
        default=1
    )
    Estado_civil = models.CharField(
        max_length = 50,
        null=False, blank=False,
        choices=civil_status_choices,
        default=1
    )
    Nacionalidad = models.CharField(max_length=50)
    Numero_De_Pasaporte = models.CharField(blank=True,max_length=10)
    Labor_en_Liquidacion = models.CharField(blank=True,max_length=50)
    Celular = models.IntegerField()
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

class Libro_Rem_Electronico(models.Model):
    Tipo_Jornada_Trabajo = models.CharField(
        max_length=500,
        null=False, blank=False,
        choices= work_choices,
        default= 1
    )
    Profesional = models.BooleanField()
    
class Empleado(models.Model):
    ID = models.AutoField(primary_key=True)
    Datos_Empleado = models.ForeignKey(Datos_Empleado, on_delete=models.CASCADE)

