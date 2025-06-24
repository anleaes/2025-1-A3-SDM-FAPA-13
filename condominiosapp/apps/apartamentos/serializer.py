from rest_framework import serializers
from .models import Apartamento

class ApartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartamento
        fields = '__all__'