from django.http import HttpResponse
from django.core import serializers

from simple_rest import Resource
from clientes.models import Cliente

class ClienteApi(Resource):

    def get(self, request, pk=None, **kwargs):
        json_serializer = serializers.get_serializer('json')()
        if pk:
            clientes = serializers.serialize("json", Cliente.objects.filter(pk=pk))
        else:
            clientes = serializers.serialize("json", Cliente.objects.all())
        return HttpResponse(clientes, content_type='application/json', status=200)


    def post(self, request, *args, **kwargs):
        empresa = request.POST.get('empresa')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono')
        Cliente.objects.create(
        	empresa=empresa,
        	email=email,
        	telefono=telefono
        )
        return HttpResponse(status=201)

    def put(self, request, pk, *args, **kwargs):
    	cliente = Cliente.objects.get(pk=pk)
        empresa = request.PUT.get('empresa')
        email = request.PUT.get('email')
        telefono = request.PUT.get('telefono')

    	cliente.empresa = empresa
    	cliente.email = email
    	cliente.telefono = telefono

    	cliente.save()

        return HttpResponse(status=200)
        

    def delete(self, request, pk):
        cliente = Cliente.objects.get(pk=pk)
        cliente.delete()
        return HttpResponse(status=200)

cliente_api = ClienteApi.as_view()