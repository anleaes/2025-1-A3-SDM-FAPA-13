from django.shortcuts import render
from .models import Apartamento
from rest_framework import viewsets
from .serializer import  ApartamentoSerializer

class ApartamentoViewSet(viewsets.ModelViewSet):
    queryset = Apartamento.objects.all()
    serializer_class = ApartamentoSerializer  