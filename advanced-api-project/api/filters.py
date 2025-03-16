import django_filters
from .models import Book

class BookFilter(django_filters.FilterSet):
    """
    Custom filter for Book model that provides advanced filtering options.
    """
    # Filter by exact match (case-insensitive)
    title = django_filters.CharFilter(lookup_expr='icontains')
    
    # Filter for publication year with range options
    min_year = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte')
    max_year = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte')
    
    # Filter by author name (not just ID)
    author_name = django_filters.CharFilter(field_name='author__name', lookup_expr='icontains')
    
    class Meta:
        model = Book
        fields = ['title', 'publication_year', 'author', 'min_year', 'max_year', 'author_name']