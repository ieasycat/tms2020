from rest_framework.serializers import ModelSerializer
from drf1.models import Product


class ProductSerializers(ModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'name', 'price', 'counter', 'comment')
