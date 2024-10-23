from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include('users.urls', namespace='users')),
    path('network/', include('network.urls', namespace='network')),
    path('products/', include('products.urls', namespace='products')),
]
