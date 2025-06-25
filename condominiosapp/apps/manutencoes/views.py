from .models import Manutencao
from rest_framework import viewsets
from .serializer import ManutencaoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
