from .models import AreaComum
from rest_framework import serializers

class AreaComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = AreaComum
        fields = '__all__'