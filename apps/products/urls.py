from django.urls import path
from apps.products.views import ProductListAPIView, ProductRetrieveAPIView

urlpatterns = [
    path('products/', ProductListAPIView.as_view()),
    path('products/<int:pk>/', ProductRetrieveAPIView.as_view()),


]