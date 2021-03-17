from drf1.models import Product
from drf1.serializers import ProductSerializers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializers(products, many=True)
        return Response(serializers.data)
    elif request.method == 'POST':
        serializers = ProductSerializers(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def api_products_one(request, pk):
    if request.method == 'GET':
        products = Product.objects.get(pk=pk)
        serializers = ProductSerializers(products)
        return Response(serializers.data)
