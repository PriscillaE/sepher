from __future__ import unicode_literals

from datetime import datetime, time, date, timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Donadores(models.Model):
    Donador_nombre=models.CharField(max_length=50)
    Donador_correo=models.EmailField()
    Donador_tel=models.CharField(max_length=15)

    def __unicode__(self):
        return "Nombre: %s"%(self.Donador_nombre)


class Donaciones_Monetarias(models.Model):
    Donaciones_opciones=(
    ('CH','Cheque'),
    ('DE','Deposito'),
    ('EF','Efectivo')
    )
    Fecha=models.DateField(default=date.today)
    Donador=models.ForeignKey(Donadores)
    Cantidad=models.IntegerField()
    Forma_pago=models.CharField(max_length=15,choices=Donaciones_opciones)


class Donaciones_Especie(models.Model):
    Fecha=models.DateField(default=date.today)
    Donador=models.ForeignKey(Donadores)
    Descripcion=models.CharField(max_length=60)
    Unidades=models.CharField(max_length=20)
    Cantidad=models.IntegerField()
