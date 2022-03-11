from django.db import models
from datetime import datetime

class Sensor(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=100, null=True, blank=True)
    
    class Meta:
        verbose_name = 'Sensor'
        verbose_name_plural = 'Sensors'

    def __str__(self) -> str:
        return f"{self.name} - {self.description}"


class Measurement(models.Model):
    sensor = models.ForeignKey(Sensor, on_delete=models.CASCADE, null=True, blank=True, related_name='measurements')
    temperature = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Measurement'
        verbose_name_plural = 'Measurements'
    
    def __str__(self):
        return self.temperature


