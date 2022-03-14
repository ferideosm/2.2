import django_filters
from .models import Stock

class ProductsFilter(django_filters.FilterSet):
    products = django_filters.NumberFilter(
        field_name='products__id',
        lookup_expr='exact',
    )

    class Meta:
        model = Stock
        fields = ['address', 'products']