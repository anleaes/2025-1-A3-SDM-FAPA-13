from django.shortcuts import render
from .models import Bloco
from rest_framework import viewsets
from .serializer import BlocoSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BlocoViewSet(viewsets.ModelViewSet):
    queryset = Bloco.objects.all()
    serializer_class = BlocoSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'numero', 'qtd_apartamentos', 'condominio']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]