from rest_framework import serializers
from .models import Car


class FindCarSerializer(serializers.Serializer):
    make = serializers.CharField()
    model_name = serializers.CharField()


class AddCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model_name', 'rates_counter', 'total_rates', 'average_rate']