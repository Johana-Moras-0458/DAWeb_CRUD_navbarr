# Generated by Django 5.1.2 on 2024-11-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Empleado',
            fields=[
                ('idempleado', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=10)),
                ('apellido', models.CharField(max_length=10)),
                ('telefono', models.CharField(max_length=10)),
                ('salario', models.FloatField()),
                ('horario', models.CharField(max_length=20)),
                ('direccion', models.CharField(max_length=50)),
            ],
        ),
    ]