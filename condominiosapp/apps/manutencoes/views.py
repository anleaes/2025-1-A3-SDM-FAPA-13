from .models import Manutencao
from rest_framework import viewsets
from .serializer import ManutencaoSerializer

class ManutencaoViewSet(viewsets.ModelViewSet):
    queryset = Manutencao.objects.all()
    serializer_class = ManutencaoSerializer
