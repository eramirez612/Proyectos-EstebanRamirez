# Generated by Django 4.1.2 on 2023-07-14 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serialApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro_equipo',
            name='tipo_dispositivo',
            field=models.CharField(choices=[('Notebook', 'Notebook'), ('All-In-one', 'All-In-one'), ('Celular', 'Celular'), ('Monitor', 'Monitor'), ('Impresora', 'Impresora'), ('Otros', 'Otros')], default=1, max_length=100),
        ),
    ]