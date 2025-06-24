from .models import Morador
from rest_framework import viewsets
from .serializer import MoradorSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class MoradorViewSet(viewsets.ModelViewSet):
    queryset = Morador.objects.all()
    serializer_class = MoradorSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'cpf', 'apartamento']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]