from .models import AreaComum
from rest_framework import viewsets
from .serializer import AreaComumSerializer

# Create your views here.

class AreaComumViewSet(viewsets.ModelViewSet):
    queryset = AreaComum.objects.all()
    serializer_class = AreaComumSerializer
