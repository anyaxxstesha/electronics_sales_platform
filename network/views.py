from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from network.models import NetworkElement
from network.serializers import NetworkElementSerializer


class NetworkElementCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NetworkElementSerializer


class NetworkElementListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()
    filter_backends = (filters.OrderingFilter, DjangoFilterBackend)
    filterset_fields = ('city',)
    ordering_fields = ('city',)


class NetworkElementRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()


class NetworkElementUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = NetworkElementSerializer
    queryset = NetworkElement.objects.all()


class NetworkElementDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = NetworkElement.objects.all()
