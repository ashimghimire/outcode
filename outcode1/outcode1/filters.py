# your_app/filters.py
import django_filters
from .models import Room

class RoomFilter (django_filters.FilterSet):
    name = django_filters.CharFilter(field_name="name", lookup_expr='icontains', label="Search by Name")
    price = django_filters.NumberFilter(field_name="price", lookup_expr='gte', label="Minimum Price")
    bed_type = django_filters.CharFilter(field_name="bed_type", lookup_expr='icontains', label="Filter by Bed type")
    status = django_filters.CharFilter(field_name="status", lookup_expr='icontains', label="Filter by Status")
    size = django_filters.NumberFilter(field_name="size", lookup_expr='gte', label="Filter by Size")

    class Meta:
        model = Room
        fields = ['name', 'price', 'bed_type', 'status', 'size']
