# Generated by Django 4.1 on 2023-01-26 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serialApp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proyecto',
            name='fecha_termino',
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
