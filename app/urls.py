from django.urls import path
from .views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView,ProductDetailAPIView,ProductListAPIView


urlpatterns = [
    path('', ProductListView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailView.as_view(), name='product-detail'),
    path('products/create/', ProductCreateView.as_view(), name='product-create'),
    path('products/<int:pk>/update/', ProductUpdateView.as_view(), name='product-update'),
    path('products/<int:pk>/delete/', ProductDeleteView.as_view(), name='product-delete'),
    path('api/products/', ProductListAPIView.as_view(), name='api-product-list'),
    path('api/products/<int:pk>/', ProductDetailAPIView.as_view(), name='api-product-detail'),
]
