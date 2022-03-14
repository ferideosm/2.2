from re import search
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter

from logistic.models import Product, Stock, StockProduct
from logistic.serializers import ProductSerializer, StockSerializer
from .filters import ProductsFilter


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', ]


class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer
    filter_backends = (DjangoFilterBackend,)
    
    filterset_fields = ['products', ]
    filterset_class= ProductsFilter
