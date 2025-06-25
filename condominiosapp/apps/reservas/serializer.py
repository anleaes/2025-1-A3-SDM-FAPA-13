from .models import ReservaAreaComum
from rest_framework import serializers

class ReservaAreaComumSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservaAreaComum
        fields = '__all__'
