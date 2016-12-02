from __future__ import unicode_literals

from datetime import datetime, time, date, timedelta
from django.db import models
from donaciones.models import Donaciones_Monetarias, Donaciones_Especie
from bases.models import Personal,Administradores,Minutas,Eventos
from django.contrib.auth.models import User

# Create your models here.
class Paciente(models.Model):
    Estado_opciones=(
    ('RE','Remision'),
    ('TR','En Tratamiento'),
    ('DEP','Fallecido'),
    )
    Paciente_nombre=models.CharField(max_length=40)
    Paciente_apellido=models.CharField(max_length=50)
    Paciente_fnacimiento=models.DateField()
    Paciente_diagnostico=models.CharField(max_length=200)
    Paciente_clinica=models.CharField(max_length=50)
    Tutor_Padre=models.CharField(max_length=50)
    Paciente_contacto=models.CharField(max_length=15,blank=True)
    Estado_salud=models.CharField(max_length=10,choices=Estado_opciones)


class Historial_Medico(models.Model):
    Paciente_hm=models.ForeignKey(Paciente)
    Fecha=models.DateField(default=date.today)
    Diagnostico=models.TextField()

class Seguimiento_Apoyo(models.Model):
    Apoyo_Paciente=models.ForeignKey(Paciente)
    Donacion_monetaria=models.ForeignKey(Donaciones_Monetarias,blank=True)
    Donacion_especie=models.ForeignKey(Donaciones_Especie,blank=True)
    Fecha_entrega=models.DateField(default=date.today)

class Defunciones(models.Model):
    Paciente=models.ForeignKey(Paciente)
    Fecha_apoyo=models.DateField(default=date.today)
    Apoyo=models.IntegerField()
    Recipiente_nombre=models.CharField(max_length=50)