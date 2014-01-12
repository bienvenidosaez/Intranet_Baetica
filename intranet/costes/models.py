# -*- encoding: utf-8 -*-

from django.db import models
from proyectos.models import Proyecto
from empleados.models import TimeStampedModel, Empleado


class LineaCoste(TimeStampedModel):
    empleado = models.ForeignKey(Empleado)
    proyecto = models.ForeignKey(Proyecto)
    descripcion = models.CharField(max_length=140)
    tiempo = models.DecimalField(max_digits=5, decimal_places=1, verbose_name="Tiempo de la tarea en horas")
    fecha = models.DateField(blank=False)

    class Meta:
        ordering = ["proyecto", "empleado"]
        verbose_name = "Línea de coste"
        verbose_name_plural = "Líneas de coste"
