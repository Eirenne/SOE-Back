from rest_framework import serializers
from . import models


class EmotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Emotion
        fields = '__all__'


class RecordSerializer(serializers.ModelSerializer):
    date = serializers.DateField(format="%Y-%m-%d")

    class Meta:
        model = models.Record
        fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Song
        fields = '__all__'
