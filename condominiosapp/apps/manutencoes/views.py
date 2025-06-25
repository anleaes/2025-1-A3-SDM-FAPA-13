from .models import Manutencao
from rest_framework import viewsets
from .serializer import ManutencaoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['descricao', 'data', 'status', 'condominio']
