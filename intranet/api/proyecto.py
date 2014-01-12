from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource
from proyectos.models import Proyecto
from simple_rest.auth.decorators import login_required, admin_required


class ProyectoApi(Resource):

    def get(self, request, pk=None, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        if pk:
            proyectos = serializers.serialize("json", Proyecto.objects.filter(pk=pk))
        else:
            proyectos = serializers.serialize("json", Proyecto.objects.all())
        return HttpResponse(proyectos, content_type='application/json', status=200)

    # @login_required
    def post(self, request, *args, **kwargs):
        nombre = request.POST.get('nombre')
        f_inicio = request.POST.get('f_inicio')
        descripcion = request.POST.get('descripcion')
        cliente = request.POST.get('cliente')
        Proyecto.objects.create(
        	nombre      = nombre,
        	f_inicio    = f_inicio,
        	descripcion = descripcion,
        	cliente     = cliente,
        )
        return HttpResponse(status=201)

    # @login_required
    def put(self, request, pk, *args, **kwargs):
    	Proyecto = Proyecto.objects.get(pk=pk)
        nombre = request.POST.get('nombre')
        f_inicio = request.POST.get('f_inicio')
        descripcion = request.POST.get('descripcion')
        cliente = request.POST.get('cliente')

    	Proyecto.nombre = nombre
    	Proyecto.f_inicio = f_inicio
    	Proyecto.descripcion = descripcion
    	Proyecto.cliente = cliente

    	Proyecto.save()

        return HttpResponse(status=200)
        
    # @login_required
    def delete(self, request, pk):
        Proyecto = Proyecto.objects.get(pk=pk)
        Proyecto.delete()
        return HttpResponse(status=200)

proyecto_api = ProyectoApi.as_view()