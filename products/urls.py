from django.urls import path

from products.apps import ProductsConfig
from products.views import ProductCreateAPIView, ProductRetrieveAPIView, ProductListAPIView, ProductUpdateAPIView, \
    ProductDestroyAPIView

app_name = ProductsConfig.name

urlpatterns = [
    path('create/', ProductCreateAPIView.as_view(), name='product_create'),
    path('<int:pk>/', ProductRetrieveAPIView.as_view(), name='product_retrieve'),
    path('', ProductListAPIView.as_view(), name='product_list'),
    path('update/<int:pk>/', ProductUpdateAPIView.as_view(), name='product_update'),
    path('delete/<int:pk>/', ProductDestroyAPIView.as_view(), name='product_delete'),
]
