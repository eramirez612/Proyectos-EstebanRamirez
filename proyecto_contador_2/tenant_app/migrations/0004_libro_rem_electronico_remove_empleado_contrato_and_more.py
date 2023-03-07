# Generated by Django 4.1 on 2023-02-27 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tenant_app', '0003_datos_empleado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Libro_Rem_Electronico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tipo_Jornada_Trabajo', models.CharField(choices=[('--Seleccione el tipo de jornada--', '--Seleccione el tipo de jornada--'), ('ORDINARIA - ART 22 (45 Horas)', 'ORDINARIA-ART 22 (45 Horas)'), ('PARCIAL - ART 40 BIS (30 Horas max)', 'PARCIAL-ART 40 BIS (30 Horas max)'), ('EXTRAORDINARIA - ART 30 (sobretiempo)', 'EXTRAORDINARIA-ART 30 (sobretiempo)'), ('ESPECIAL - ART 38 INCISO 5 (trabajo fuerza mayor)', 'ESPECIAL - ART 38 INCISO 5 (trabajo fuerza mayor)'), ('ESPECIAL - ART 23 (NAVIERO)', 'ESPECIAL - ART 23 (NAVIERO)'), ('ESPECIAL - ART 106 (NAVIERO)', 'ESPECIAL - ART 106 (NAVIERO)'), ('ESPECIAL - ART 152 TER D (tripulantes de vuelo)', 'ESPECIAL - ART 152 TER D (tripulantes de vuelo)'), ('ESPECIAL - ART 152 TER F (tripulantes de vuelo)', 'ESPECIAL - ART 152 TER F (tripulantes de vuelo)'), ('ESPECIAL - ART 25 (locomocion colectiva interurbana)', 'ESPECIAL - ART 25 (locomocion colectiva interurbana)'), ('ESPECIAL - ART 25 BIS (carga terrestre interurbana)', 'ESPECIAL - ART 25 BIS (carga terrestre interurbana)'), ('ESPECIAL - ART 149 (trabajadores de casa particular)', 'ESPECIAL - ART 149 (trabajadores de casa particular)'), ('ESPECIAL - ART 149 INCISO 2 (trabajadores de casa particular)', 'ESPECIAL - ART 149 INCISO 2 (trabajadores de casa particular)'), ('ESPECIAL - ART 152 BIS (cuerpos de bomberos)', 'ESPECIAL - ART 152 BIS (cuerpos de bomberos)'), ('ESPECIAL - ART 36 145-D (artes y espectaculos)', 'ESPECIAL - ART 36 145-D (artes y espectaculos)'), ('ESPECIAL - ART 22 INCISO FINAL (deportistas profesionales)', 'ESPECIAL - ART 22 INCISO FINAL (deportistas profesionales)'), ('BISEMANAL - ART 149 INCISO 2 (trabajadores de casa particular)', 'BISEMANAL - ART 149 INCISO 2 (trabajadores de casa particular)'), ('JORNADA EXCEPCIONAL - ART 38 INCISO FINAL (trabajo fuerza mayor)', 'JORNADA EXCEPCIONAL - ART 38 INCISO FINAL (trabajo fuerza mayor)'), ('EXENTA - ART 22 (sin limitacion de jornada)', 'EXENTA - ART 22 (sin limitacion de jornada)')], default=1, max_length=500)),
                ('Profesional', models.BooleanField()),
            ],
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='contrato',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='estado',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_ingreso',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='fecha_termino',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='metodo_pago',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='empleado',
            name='rut',
        ),
        migrations.AddField(
            model_name='datos_empleado',
            name='Estado_civil',
            field=models.CharField(choices=[('--Seleccione el estado civil--', '--Seleccione el estado civil--'), ('Soltero', 'Soltero'), ('Casado', 'Casado'), ('Divorciado', 'Divorciado'), ('Viudo', 'Viudo')], default=1, max_length=50),
        ),
        migrations.AddField(
            model_name='datos_empleado',
            name='Nacionalidad',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='empleado',
            name='Datos_Empleado',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tenant_app.datos_empleado'),
        ),
        migrations.AddField(
            model_name='empleado',
            name='ID',
            field=models.AutoField(default=1, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='datos_empleado',
            name='Celular',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='datos_empleado',
            name='Labor_en_Liquidacion',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='datos_empleado',
            name='Nombres',
            field=models.CharField(max_length=9),
        ),
        migrations.AlterField(
            model_name='datos_empleado',
            name='Numero_De_Pasaporte',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]