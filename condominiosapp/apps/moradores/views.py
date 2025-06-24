from .models import Morador
from rest_framework import viewsets
from .serializer import MoradorSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend


class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer