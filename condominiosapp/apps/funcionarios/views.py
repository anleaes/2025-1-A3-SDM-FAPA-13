from .models import Funcionario
from rest_framework import viewsets
from .serializer import FuncionarioSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nome', 'funcao', 'turno', 'condominio']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]