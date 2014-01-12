from django.http import HttpResponse
from .models import Proyecto


def home(request):
    html = "<html><body>Hola</body></html>"
    return HttpResponse(html)


from .serializers import ProyectoSerializer
from rest_framework import viewsets

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

