from .models import Condominio
from rest_framework import serializers

class CondominioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Condominio
        fields = '__all__'