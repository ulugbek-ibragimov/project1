from django.shortcuts import render
from rest_framework.generics import ListAPIView, RetrieveAPIView
from apps.products.models import Product
from apps.products.serializers import *

class ProductListAPIView(ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveAPIView(RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


