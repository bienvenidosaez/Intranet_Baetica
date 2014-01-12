from django.http import HttpResponse
from .models import Empleado
from utiles.models import JSONSerializer


def json_response_from(response):
    jsonSerializer = JSONSerializer()
    return HttpResponse(jsonSerializer.serialize(response, use_natural_keys=True), content_type='application/json')


# Rest Framework
from .serializers import EmpleadoSerializer
from rest_framework import viewsets


class EmpleadoViewSet(viewsets.ModelViewSet):
    queryset = Empleado.objects.all()
    serializer_class = EmpleadoSerializer


def prueba(request):
    data = []
    for e in Empleado.objects.all():
        e = {
                'id':e.pk,
                'nombre':e.nombre,
            }
        data.append(e)
    return json_response_from(data)
