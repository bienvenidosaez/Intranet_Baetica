from django.db import models
from empleados.models import TimeStampedModel


class Cliente(TimeStampedModel):
    empresa = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.IntegerField(max_length=10, unique=True, blank=True)

    def __unicode__(self):
        return self.empresa


class Contacto(TimeStampedModel):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.IntegerField(max_length=10, unique=True, blank=True)
    empresa = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.nombre
