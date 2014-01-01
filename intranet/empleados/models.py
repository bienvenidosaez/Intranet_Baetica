# -*- encoding: utf-8 -*-
from django.db import models


class TimeStampedModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Empleado(TimeStampedModel):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    telefono = models.IntegerField(max_length=10, unique=True, blank=True, null=True)
    # titulo = models.CharField(max_length=150)
    # titulo_movil = models.CharField(max_length=100, blank=True, null=True)
    # url = models.SlugField(max_length=150, unique=True)
    # usuario = models.ForeignKey(User)
    # actualizado = models.DateTimeField(auto_now=True)
    # categorias = models.ManyToManyField('Categoria', blank=True)
    # tags = models.ManyToManyField('Tag', blank=True)
    # contenido = HTMLField(blank=True)
    # extracto = HTMLField(blank=True)
    # imagen_destacada = models.ImageField(upload_to='articulos', blank=True)

    def __unicode__(self):
        return self.nombre
