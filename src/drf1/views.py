from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from drf1.models import Product
from drf1.serializers import ProductSerializers


# Create your views here.


class APIProducts(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers


class APIProductDetail(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
