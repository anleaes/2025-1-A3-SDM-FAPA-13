from .models import ReservaAreaComum
from rest_framework import viewsets
from .serializer import ReservaAreaComumSerializer

# Filter
from django_filters.rest_framework import DjangoFilterBackend

# Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

class ReservaAreaComumViewSet(viewsets.ModelViewSet):
    queryset = ReservaAreaComum.objects.all()
    serializer_class = ReservaAreaComumSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['data_reserva', 'status', 'morador', 'area_comum']
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]