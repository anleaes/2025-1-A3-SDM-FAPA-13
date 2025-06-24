from .models import Morador
from rest_framework import viewsets
from .serializer import MoradorSerializer


class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer