from drf1.models import Product
from drf1.serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.


@api_view(['GET'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializers(products, many=True)
        return Response(serializers.data)
