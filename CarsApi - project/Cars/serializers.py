from rest_framework import serializers
from .models import Car


class FindCarSerializer(serializers.Serializer):
    make = serializers.CharField()
    model_name = serializers.CharField()


class AddCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model_name', 'rates_counter', 'total_rates', 'average_rate']


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model_name', 'average_rate']


class CarPopularSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['make', 'model_name', 'rates_counter', 'average_rate']


class AddRateSerializer(serializers.Serializer):
    make = serializers.CharField()
    model_name = serializers.CharField()
    rate = serializers.IntegerField(min_value=1, max_value=5)
