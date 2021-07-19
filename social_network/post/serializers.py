from rest_framework import serializers
from .models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta():
        model = Post
        fields = ('id', 'author', 'title', 'text', 'likes', 'created',)
        read_only_fields = ('author', 'likes')