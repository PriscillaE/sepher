# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 03:24
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('donaciones', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Defunciones',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_apoyo', models.DateField(default=datetime.date.today)),
                ('Apoyo', models.IntegerField()),
                ('Recipiente_nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Historial_Medico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today)),
                ('Diagnostico', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Paciente_nombre', models.CharField(max_length=40)),
                ('Paciente_apellido', models.CharField(max_length=50)),
                ('Paciente_fnacimiento', models.DateField()),
                ('Paciente_diagnostico', models.CharField(max_length=200)),
                ('Paciente_clinica', models.CharField(max_length=50)),
                ('Tutor_Padre', models.CharField(max_length=50)),
                ('Paciente_contacto', models.CharField(blank=True, max_length=15)),
                ('Estado_salud', models.CharField(choices=[('RE', 'Remision'), ('TR', 'En Tratamiento'), ('DEP', 'Fallecido')], max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Seguimiento_Apoyo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha_entrega', models.DateField(default=datetime.date.today)),
                ('Apoyo_Paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente')),
                ('Donacion_especie', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='donaciones.Donaciones_Especie')),
                ('Donacion_monetaria', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='donaciones.Donaciones_Monetarias')),
            ],
        ),
        migrations.AddField(
            model_name='historial_medico',
            name='Paciente_hm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
        ),
        migrations.AddField(
            model_name='defunciones',
            name='Paciente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.Paciente'),
        ),
    ]
