from django.shortcuts import render
from django.db.models import Count
from rest_framework import generics, permissions
from .serializers import LikesByDaySerializer
from .filters import LikesByDayFilter
from post.models import Like


class LikesByDay(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    serializer_class = LikesByDaySerializer
    filter_class = LikesByDayFilter

    def get_queryset(self):
        return Like.objects.\
            values('date').\
            annotate(likes=Count('date')).\
            order_by()


