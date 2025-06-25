from .models import Manutencao
from rest_framework import serializers

class ManutencaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manutencao
        fields = '__all__'
