import django_filters
from post.models import Like


class LikesByDayFilter(django_filters.FilterSet):
    date_from = django_filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = django_filters.DateFilter(field_name='date', lookup_expr='lte')
    
    class Meta:
        model = Like
        fields = ('date_from', 'date_to',)