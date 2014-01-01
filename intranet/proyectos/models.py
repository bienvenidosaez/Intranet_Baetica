from django.db import models
from empleados.models import TimeStampedModel, Empleado
from clientes.models import Cliente


class Proyecto(TimeStampedModel):
    nombre = models.CharField(max_length=150)
    f_inicio = models.DateTimeField(auto_now=True)
    descripcion = models.TextField(max_length=500, blank=True)
    cliente = models.ForeignKey(Cliente)

    def __unicode__(self):
        return self.nombre


class Muro(TimeStampedModel):
    descripcion = models.CharField(max_length=150, blank=False)
    proyecto = models.ForeignKey(Proyecto)

    def __unicode__(self):
        return self.descripcion


class Mensaje(TimeStampedModel):
    muro = models.ForeignKey(Muro)
    empleado = models.ForeignKey(Empleado)
    texto = models.TextField(max_length=500, blank=False)
    respuesta = models.ForeignKey('self', blank=True, null=True, help_text='Es respuesta de')

    def __unicode__(self):
        return self.texto


class Tarea(TimeStampedModel):
    texto = models.TextField(max_length=200)
    proyecto = models.ForeignKey(Proyecto)
    autor = models.ForeignKey(Empleado, related_name='Creador de la tarea')
    para = models.ManyToManyField(Empleado, related_name='Destinatarios de la tarea')
    terminado = models.BooleanField(default=False)
