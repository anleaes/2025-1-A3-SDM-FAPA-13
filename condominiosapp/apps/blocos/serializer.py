from rest_framework import serializers
from .models import Bloco

class BlocoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bloco
        fields = '__all__'