from .models import Condominio
from rest_framework import viewsets
from .serializer import CondominioSerializer

class CondominioViewSet(viewsets.ModelViewSet):
    queryset = Condominio.objects.all()
    serializer_class = CondominioSerializer 