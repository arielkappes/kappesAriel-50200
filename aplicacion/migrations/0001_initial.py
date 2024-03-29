# Generated by Django 5.0.1 on 2024-02-07 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Areas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Area', models.CharField(max_length=50)),
                ('Destino', models.CharField(max_length=50)),
                ('Responsable', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Bienes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Dominio', models.CharField(max_length=50)),
                ('SubClase', models.CharField(max_length=50)),
                ('Anio', models.DateField(max_length=50)),
                ('MarcaModelo', models.CharField(max_length=50)),
                ('NroChasis', models.CharField(max_length=50)),
                ('NroMotor', models.CharField(max_length=50)),
                ('Accesorios', models.CharField(max_length=100)),
                ('AeguradoraPoliza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Personal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('NroLegajo', models.CharField(max_length=50)),
                ('Apellido_y_Nombre', models.CharField(max_length=50)),
                ('Agrupamiento', models.CharField(max_length=50)),
                ('Cargo', models.CharField(max_length=50)),
                ('Destino', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Rubros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Clase', models.CharField(max_length=50)),
                ('SubClase', models.CharField(max_length=50)),
            ],
        ),
    ]
