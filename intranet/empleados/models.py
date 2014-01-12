# -*- encoding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class TimeStampedModel(models.Model):
    creado = models.DateTimeField(auto_now_add=True)
    modificado = models.DateTimeField(auto_now=True)
    activo = models.BooleanField(default=False)

    class Meta:
        abstract = True


class EmpleadoManager(BaseUserManager):
    def _create_user(self, email, password, nombre, telefono, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('El email debe ingresarse,')
        email = self.normalize_email(email)
        emp = self.model(email=email, nombre=nombre, telefono=telefono, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        emp.set_password(password)
        emp.save(using=self._db)
        return emp

    def create_user(self, email, password=None, nombre=None, telefono=None, **extra_fields):
        return self._create_user(email, password, nombre, telefono, False, False, **extra_fields)

    def create_superuser(self, email, password, nombre, telefono, **extra_fields):
        return self._create_user(email, password, nombre, telefono, True, True, **extra_fields)


class Empleado(AbstractBaseUser, PermissionsMixin):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(max_length=150, unique=True)
    telefono = models.IntegerField(max_length=10, unique=True)
    p_hora = models.DecimalField(max_digits=5, decimal_places=1, default=0, verbose_name="Precio por hora en €")

    is_staff = models.BooleanField(default=False)

    objects = EmpleadoManager()

    def __unicode__(self):
        return self.nombre

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['nombre', 'telefono']
