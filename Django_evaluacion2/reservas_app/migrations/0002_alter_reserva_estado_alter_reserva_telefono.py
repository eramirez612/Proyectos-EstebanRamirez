# Generated by Django 4.1.2 on 2023-06-12 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservas_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserva',
            name='estado',
            field=models.CharField(choices=[('Reservado', 'Reservado'), ('Completada', 'Completada'), ('Anulada', 'Anulada'), ('No asisten', 'No asisten')], default=1, max_length=50),
        ),
        migrations.AlterField(
            model_name='reserva',
            name='telefono',
            field=models.IntegerField(),
        ),
    ]
