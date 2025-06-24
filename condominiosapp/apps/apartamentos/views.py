from django.shortcuts import render
from .models import Apartamento
from rest_framework import viewsets
from .serializer import  ApartamentoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['numero', 'andar', 'bloco']