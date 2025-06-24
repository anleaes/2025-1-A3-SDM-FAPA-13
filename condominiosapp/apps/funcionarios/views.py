from .models import Funcionario
from rest_framework import viewsets
from .serializer import FuncionarioSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend


class FuncionarioViewSet(viewsets.ModelViewSet):
    queryset = Funcionario.objects.all()
    serializer_class = FuncionarioSerializer