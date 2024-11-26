# Generated by Django 5.1.2 on 2024-11-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ventas',
            fields=[
                ('idventa', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('idempleado', models.CharField(max_length=10)),
                ('idproducto', models.CharField(max_length=10)),
                ('idcliente', models.CharField(max_length=10)),
                ('idsucursal', models.CharField(max_length=10)),
                ('total', models.FloatField()),
                ('fechacompra', models.DateField()),
            ],
        ),
    ]