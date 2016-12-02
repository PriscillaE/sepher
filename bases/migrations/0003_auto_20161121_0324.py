# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 03:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bases', '0002_auto_20161115_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='defunciones',
            name='Paciente',
        ),
        migrations.RemoveField(
            model_name='donaciones_especie',
            name='Donador',
        ),
        migrations.RemoveField(
            model_name='donaciones_monetarias',
            name='Donador',
        ),
        migrations.RemoveField(
            model_name='historial_medico',
            name='Paciente_hm',
        ),
        migrations.RemoveField(
            model_name='seguimiento_apoyo',
            name='Apoyo_Paciente',
        ),
        migrations.RemoveField(
            model_name='seguimiento_apoyo',
            name='Donacion_especie',
        ),
        migrations.RemoveField(
            model_name='seguimiento_apoyo',
            name='Donacion_monetaria',
        ),
        migrations.DeleteModel(
            name='Defunciones',
        ),
        migrations.DeleteModel(
            name='Donaciones_Especie',
        ),
        migrations.DeleteModel(
            name='Donaciones_Monetarias',
        ),
        migrations.DeleteModel(
            name='Donadores',
        ),
        migrations.DeleteModel(
            name='Historial_Medico',
        ),
        migrations.DeleteModel(
            name='Paciente',
        ),
        migrations.DeleteModel(
            name='Seguimiento_Apoyo',
        ),
    ]
