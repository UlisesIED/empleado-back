# Generated by Django 5.0.6 on 2024-06-20 00:00

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Empleados',
            fields=[
                ('nombre', models.CharField(max_length=32)),
                ('a_paterno', models.CharField(max_length=32)),
                ('a_materno', models.CharField(blank=True, max_length=32, null=True)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('fecha_nacimiento', models.DateField()),
                ('fecha_ingreso', models.DateField(auto_now_add=True)),
                ('fotografia', models.TextField()),
                ('salario', models.FloatField()),
                ('puesto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogos.puesto')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
