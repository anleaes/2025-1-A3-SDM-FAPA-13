from django.shortcuts import render
from .models import Apartamento
from rest_framework import viewsets
from .serializer import  ApartamentoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'andar', 'bloco']