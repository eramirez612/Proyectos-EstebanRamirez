# Generated by Django 4.1 on 2022-12-16 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inscritos',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('institucion', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('fechareserva', models.DateField()),
                ('horareserva', models.TimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('Reservada', 'Reservada'), ('Completada', 'Completada'), ('Anulada', 'Anulada'), ('No asisten', 'No asisten')], default=1, max_length=50)),
                ('observacion', models.CharField(blank=True, max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Instituciones',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('institucion', models.CharField(max_length=20)),
            ],
        ),
    ]
