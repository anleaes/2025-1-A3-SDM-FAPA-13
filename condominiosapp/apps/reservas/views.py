from .models import ReservaAreaComum
from rest_framework import viewsets
from .serializer import ReservaAreaComumSerializer


class ReservaAreaComumViewSet(viewsets.ModelViewSet):
    queryset = ReservaAreaComum.objects.all()
    serializer_class = ReservaAreaComumSerializer
