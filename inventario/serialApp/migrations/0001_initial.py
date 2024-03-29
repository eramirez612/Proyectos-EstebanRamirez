# Generated by Django 4.1.2 on 2023-07-07 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Registro_Equipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=128)),
                ('rut', models.CharField(blank=True, max_length=9, null=True)),
                ('departamento', models.CharField(choices=[('Seleccion Departamento', 'Seleccion Departamento'), ('Informatica', 'Informatica'), ('Turismo y Economia', 'Turismo y Economia'), ('DIDECO', 'DIDECO'), ('Tesoreria', 'Tesoreria'), ('Programa Familias', 'Programa Familias'), ('Registro Social de Hogares', 'Registro Social de Hogares'), ('Recursos Humanos', 'Recursos Humanos'), ('Alcalde', 'Alcalde'), ('Alcaldia', 'Alcaldia'), ('Secretaría Municipal', 'Secretaría Municipal'), ('Comunicaciones', 'Comunicaciones'), ('Oficina de Partes', 'Oficina de partes'), ('OMIL', 'OMIL'), ('Movilizacion y Transparecia', 'Movilizacion y Transparecia'), ('Direccion de Control', 'Direccion de Control'), ('Asesoria Juridica', 'Asesoria Juridica'), ('Secpla', 'Secpla'), ('Departamento de Obras', 'Departamento de Obras'), ('Emergencia y Seguridad Publica', 'Emergencia y Seguridad Publica'), ('Rentas y Patentes', 'Rentas y patentes'), ('Inspectores Municipales', 'Inspectores Municipales'), ('Departamento de Transito', 'Departamento de Transito'), ('Departamento de Administracion y Finanzas', 'Departamento de Administracion y Finanzas'), ('Ayuda Social', 'Ayuda Social'), ('Departamento de Salud', 'Departamento de Salud'), ('Adquisiciones', 'Adquisiciones'), ('Administracion y Finanzas', 'Administracion y Finanzas'), ('Biblioteca', 'Biblioteca')], default=1, max_length=100)),
                ('serial_number', models.CharField(max_length=128, unique=True)),
                ('marca_modelo', models.CharField(blank=True, max_length=128, null=True)),
                ('correo', models.EmailField(blank=True, max_length=254, null=True)),
                ('contraseña', models.CharField(blank=True, max_length=128, null=True)),
                ('tipo_licencias_windows', models.CharField(choices=[('Seleccion Licencia de Windows', 'Seleccion Licencia de Windows'), ('Windows 7 Home Basic', 'Windows 7 Home Basic'), ('Windows 7 Home Premium', 'Windows 7 Home Premium'), ('Windows 7 Professional', 'Windows 7 Professional'), ('Windows 7 Ultimate', 'Windows 7 Ultimate'), ('Windows 7 Enterprise', 'Windows 7 Enterprise'), ('Windows 8 Single Language', 'Windows 8 Single Language'), ('Windows 8', 'Windows 8'), ('Windows 8 Pro', 'Windows 8 Pro'), ('Windows 8 Enterprise', 'Windows 8 Enterprise'), ('Windows 10 Home', 'Windows 10 Home'), ('Windows 10 Pro', 'Windows 10 Pro'), ('Windows 10 Enterprise', 'Windows 10 Enterprise'), ('Windows 11 Home', 'Windows 11 Home'), ('Windows 11 Pro', 'Windows 11 Pro'), ('Windows 11 Enterprise', 'Windows 11 Enterprise'), ('Licencia Vencida', 'Licencia Vencida'), ('Sin Licencia', 'Sin Licencia')], default=1, max_length=100)),
                ('nro_licencia_windows', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('tipo_licencias_office', models.CharField(choices=[('Seleccion Licencia Office', 'Seleccion Licencia Office'), ('Microsoft Office Standard 2019', 'Microsoft Office Standard 2019'), ('Microsoft Office 2019 Professional', 'Microsoft Office 2019 Professional'), ('Microsoft Office 2019 Professional Plus', 'Microsoft Office 2019 Professional Plus'), ('Microsoft Office Standard 2021', 'Microsoft Office Standard 2021'), ('Microsoft Office 2021 Professional', 'Microsoft Office 2021 Professional'), ('Microsoft Office 2021 Professional Plus', 'Microsoft Office 2021 Professional Plus'), ('Microsoft Office Hogar y Empresas', 'Microsoft Office Hogar y Empresas'), ('Microsoft Office 365 Enterprise Básico', 'Microsoft Office 365 Enterprise Básico'), ('Microsoft Office 365 Enterprise Estándar', 'Microsoft Office 365 Enterprise Estándar'), ('Microsoft Office 365 Enterprise Premium', 'Microsoft Office 365 Enterprise Premium'), ('Licencia OEM', 'Licencia OEM'), ('Sin Licencia', 'Sin Licencia')], default=1, max_length=100)),
                ('nro_licencia_office', models.CharField(blank=True, max_length=100, null=True, unique=True)),
                ('tipo_dispositivo', models.CharField(choices=[('Notebook', 'Notebook'), ('All-In-one', 'All-In-one'), ('Celular', 'Celular'), ('Monitor', 'Monitor'), ('Otros', 'Otros')], default=1, max_length=100)),
                ('fecha_ingreso_del_registro', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
