# Generated by Django 5.1.2 on 2024-11-20 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Proveedor',
            fields=[
                ('idproveedor', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('idpeluche', models.CharField(max_length=6)),
                ('nombre', models.CharField(max_length=10)),
                ('direccion', models.CharField(max_length=50)),
                ('telefono', models.CharField(max_length=10)),
                ('precio', models.FloatField()),
                ('horarios', models.CharField(max_length=20)),
            ],
        ),
    ]
