from api.serializers import ProductSerializer
from api.models import Product
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters



class ProductListView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status',]
    search_fields = ['name', 'article']


class ProductDetailtView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer