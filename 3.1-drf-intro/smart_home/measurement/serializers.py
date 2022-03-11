from rest_framework import serializers
from .models import Measurement, Sensor


class MeasurementSerializer(serializers.ModelSerializer):

    # тут не знаю как быть. Без 'sensor' корректно не сохраняется
    # Measurement в запросе POST {{baseUrl}}/measurements/ .
    # А если уберу 'sensor', то SensorDetailSerializer(measurements)
    # выдает данные с id
    
    class Meta:
        model = Measurement
        fields = ['temperature', 'created_at', 'sensor']

           


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description']


class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeasurementSerializer(read_only=True, many=True)

    class Meta:
        model = Sensor
        fields = ['id', 'name', 'description', 'measurements']