# Generated by Django 4.1 on 2023-02-15 20:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shared_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sweet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('sweet_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shared_app.sweettype')),
            ],
        ),
    ]
