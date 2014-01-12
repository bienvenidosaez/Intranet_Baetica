from .models import Empleado
from rest_framework import serializers


class EmpleadoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Empleado
        fields = ('id', 'nombre', 'email', 'telefono',)
