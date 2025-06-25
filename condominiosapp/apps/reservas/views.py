from .models import ReservaAreaComum
from rest_framework import viewsets
from .serializer import ReservaAreaComumSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

class ReservaAreaComumViewSet(viewsets.ModelViewSet):
    queryset = ReservaAreaComum.objects.all()
    serializer_class = ReservaAreaComumSerializer
