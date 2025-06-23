from django.shortcuts import render
from .models import Bloco
from rest_framework import viewsets
from .serializer import BlocoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend


class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'numero', 'condominio']