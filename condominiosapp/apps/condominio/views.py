from .models import Condominio
from rest_framework import viewsets
from .serializer import CondominioSerializer
from django_filters.rest_framework import DjangoFilterBackend

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'cnpj']