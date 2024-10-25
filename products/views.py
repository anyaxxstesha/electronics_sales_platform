from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.permissions import IsAuthenticated

from products.models import Product
from products.serializers import ProductSerializer


class ProductCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer


class ProductListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductRetrieveAPIView(RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductUpdateAPIView(UpdateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDestroyAPIView(DestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
