# myapp/serializers.py
from rest_framework import serializers

class TimeSeriesSerializer(serializers.Serializer):
    date = serializers.DateField()
    amount_sum = serializers.FloatField()

class PieGenderSerializer(serializers.Serializer):
    gender = serializers.CharField()
    amount_sum = serializers.FloatField()

class BoxesGenderSerializer(serializers.Serializer):
    gender = serializers.CharField()
    amount = serializers.FloatField()

class TopClientsSerializer(serializers.Serializer):
    id_client = serializers.CharField()
    name = serializers.CharField()
    amount = serializers.FloatField()

class AgeRangeSerializer(serializers.Serializer):
    age_range = serializers.CharField()
    amount = serializers.FloatField()

class AgeHistogramSerializer(serializers.Serializer):
    age = serializers.IntegerField()
    amount = serializers.FloatField()



