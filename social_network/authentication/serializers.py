from rest_framework import serializers


class UserActivitySerializer(serializers.Serializer):
    last_login = serializers.DateTimeField()
    last_seen = serializers.DateTimeField()
