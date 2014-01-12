from django.http import HttpResponse
from django.core import serializers
from django.utils import timezone

from simple_rest import Resource

from empleados.models import Empleado

import json


class EmpleadoApi(Resource):

    def get(self, request, pk=None, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        if pk:
            empleados = serializers.serialize("json", Empleado.objects.filter(pk=pk))
        else:
            empleados = serializers.serialize("json", Empleado.objects.all())
        return HttpResponse(empleados, content_type='application/json', status=200)

    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        p_hora = request.POST.get('p_hora')
        password = request.POST.get('password')
        staff = request.POST.get('staff')
        e = Empleado.objects.create(
			nombre   =nombre,
			email    =email,
			telefono = telefono,
			p_hora   = p_hora,
			is_staff = staff
        )
        e.set_password(password)
        e.save()
        return HttpResponse(status=201)

    def put(self, request, pk, *args, **kwargs):
    	empleado = Empleado.objects.get(pk=pk)
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        p_hora = request.POST.get('p_hora')
        staff = request.POST.get('staff')

    	empleado.nombre = nombre
    	empleado.email = email
    	empleado.telefono = telefono
    	empleado.p_hora = p_hora
    	empleado.p_staff = staff

    	empleado.save()

        return HttpResponse(status=200)
        

    def delete(self, request, pk):
        empleado = Empleado.objects.get(pk=pk)
        empleado.delete()
        return HttpResponse(status=200)

empleado_api = EmpleadoApi.as_view()