from rest_framework import serializers


class LikesByDaySerializer(serializers.Serializer):
    date = serializers.DateField()
    likes = serializers.IntegerField()
