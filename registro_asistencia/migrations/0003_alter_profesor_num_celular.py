# Generated by Django 4.2.6 on 2023-10-07 22:55

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registro_asistencia', '0002_alter_asistenciaclase_tema_delete_tema'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profesor',
            name='num_celular',
            field=models.CharField(max_length=9, unique=True, validators=[django.core.validators.MinLengthValidator(9), django.core.validators.MaxLengthValidator(9)]),
        ),
    ]
