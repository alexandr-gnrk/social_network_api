from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, permissions
from .serializers import LikesByDaySerializer
from post.models import Like


class LikesByDay(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Like.objects.\
        extra(select={'date': 'date(time)'}).\
        values('date').\
        annotate(likes=Count('time')).\
        order_by()
    serializer_class = LikesByDaySerializer
