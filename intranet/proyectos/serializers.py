from .models import Proyecto
from rest_framework import serializers


class ProyectoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Proyecto
        fields = ('nombre', 'f_inicio', 'descripcion', 'cliente',)
