# Generated by Django 5.0.6 on 2024-06-20 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0002_empleados_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='empleados',
            name='fotografia',
            field=models.TextField(blank=True, null=True),
        ),
    ]