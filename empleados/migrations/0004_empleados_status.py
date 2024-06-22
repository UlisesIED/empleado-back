# Generated by Django 5.0.6 on 2024-06-22 01:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empleados', '0003_alter_empleados_fotografia'),
    ]

    operations = [
        migrations.AddField(
            model_name='empleados',
            name='status',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Activo'), (2, 'De baja'), (3, 'Enfermo'), (4, 'Vacaciones')], default=1),
        ),
    ]