from rest_framework.viewsets import ModelViewSet

from drf1.models import Product
from drf1.serializers import ProductSerializers


# Create your views here.


class APIProducts(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
