from .models import Morador
from rest_framework import viewsets
from .serializers import MoradorSerializer


class MoradorViewSet(viewsets.ModelViewSet):
    pass