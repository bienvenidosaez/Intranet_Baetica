from .models import Cliente

# Rest Framework
from .serializers import ClienteSerializer
from rest_framework import viewsets


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
