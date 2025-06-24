from .models import Morador
from rest_framework import viewsets
from .serializers import MoradorSerializer


class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer