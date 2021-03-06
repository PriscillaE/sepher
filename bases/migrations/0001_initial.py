# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-14 04:09
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donaciones_Especie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today)),
                ('Descripcion', models.CharField(max_length=60)),
                ('Unidades', models.CharField(max_length=20)),
                ('Cantidad', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Donaciones_Monetarias',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Fecha', models.DateField(default=datetime.date.today)),
                ('Cantidad', models.IntegerField()),
                ('Forma_pago', models.CharField(choices=[('CH', 'Cheque'), ('DE', 'Deposito'), ('EF', 'Efectivo')], max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Donadores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Donador_nombre', models.CharField(max_length=50)),
                ('Donador_correo', models.EmailField(max_length=254)),
                ('Donador_tel', models.CharField(max_length=15)),
            ],
        ),
        migrations.AddField(
            model_name='donaciones_monetarias',
            name='Donador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Donadores'),
        ),
        migrations.AddField(
            model_name='donaciones_especie',
            name='Donador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bases.Donadores'),
        ),
    ]
