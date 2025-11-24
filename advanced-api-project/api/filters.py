# =========================================================================================================================================
# =========================================================================================================================================
import django_filters
from .models import Book
# =========================================================================================================================================


# =========================================================================================================================================
# =========================================================================================================================================
class BookFilter(django_filters.FilterSet):

    # Performs a case-insensitive substring search on the 'title' field,
    # returning all entries whose names contain the provided text.
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    
    # Performs a case-insensitive substring search on the 'author' field,
    # returning all entries whose names contain the provided text.
    author = django_filters.CharFilter(field_name='author', lookup_expr='icontains')
    
    # Matches books published in the exact given year.
    publication_year = django_filters.NumberFilter()
    # Returns books published in years strictly greater than the provided value. (valuefilter >  value in database)
    publication_year__gt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gt') 
    # Returns books published in years strictly less than the provided value.  (valuefilter <  value in database)
    publication_year__lt = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lt')  
    # Returns books published in the given year or any year after it. (valuefilter >=  value in database)
    publication_year__gte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='gte') 
    # Returns books published in the given year or any year before it. (valuefilter <=  value in database)
    publication_year__lte = django_filters.NumberFilter(field_name='publication_year', lookup_expr='lte') 
    
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_year', 'publication_year__gt', 'publication_year__lt', 'publication_year__gte', 'publication_year__lte'] 
# =========================================================================================================================================
