from __future__ import unicode_literals

from datetime import datetime, time, date, timedelta
from django.db import models
from django.contrib.auth.models import User
from oauth2client.contrib.django_util.models import CredentialsField

# Create your models here.

class Personal(models.Model):
    Personal_nombre=models.CharField(max_length=40)
    Personal_apellidos=models.CharField(max_length=50)
    Personal_funcion=models.CharField(max_length=60)
    Personal_tel=models.CharField(max_length=15)
    Personal_correo=models.EmailField()

class Administradores(models.Model):
    perfil=models.OneToOneField(User)
    Admon_nombre=models.CharField(max_length=40)
    Admon_tel=models.CharField(max_length=15)
    Admon_correo=models.EmailField()

class Minutas(models.Model):
    Fecha_reunion=models.DateField()
    Asistentes=models.ManyToManyField(Administradores)
    Total_donacionesmon=models.IntegerField()
    Valor_donacionesesp=models.IntegerField()
    Duracion_reunion=models.CharField(max_length=15)
    Pacientes_beneficiados=models.IntegerField()
    Observaciones=models.TextField()

class Eventos(models.Model):
    Fecha_evento=models.DateField()
    Lugar_evento=models.CharField(max_length=100)
    Personal_evento=models.ManyToManyField(Personal)
    Hora_evento=models.TimeField()



# Create your models here.

class CredentialsModel(models.Model):
    user = models.OneToOneField(User)
    credential = CredentialsField()

class DriveCredentialsModel(models.Model):
    user = models.OneToOneField(User)
    credential = CredentialsField()

class Event(models.Model):
    summary = models.CharField(max_length=100)
    date = models.DateField()


