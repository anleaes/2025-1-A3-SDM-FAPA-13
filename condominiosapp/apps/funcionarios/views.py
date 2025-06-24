from .models import Funcionario
from rest_framework import viewsets
from .serializer import FuncionarioSerializer

class FuncionarioViewSet(viewsets.ModelViewSet):
    pass