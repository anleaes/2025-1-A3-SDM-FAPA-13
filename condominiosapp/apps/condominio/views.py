from .models import Condominio
from rest_framework import viewsets
from .serializer import CondominioSerializer

# Filters
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'cnpj']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]