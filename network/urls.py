from django.urls import path

from network.apps import NetworkConfig
from network.views import NetworkElementCreateAPIView, NetworkElementRetrieveAPIView, NetworkElementListAPIView, \
    NetworkElementUpdateAPIView, NetworkElementDestroyAPIView

app_name = NetworkConfig.name

urlpatterns = [
    path('create/', NetworkElementCreateAPIView.as_view(), name='network_create'),
    path('<int:pk>/', NetworkElementRetrieveAPIView.as_view(), name='network_retrieve'),
    path('', NetworkElementListAPIView.as_view(), name='network_list'),
    path('update/<int:pk>/', NetworkElementUpdateAPIView.as_view(), name='network_update'),
    path('delete/<int:pk>/', NetworkElementDestroyAPIView.as_view(), name='network_delete'),
]
