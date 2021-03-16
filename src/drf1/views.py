from drf1.models import Product
from drf1.serializers import ProductSerializers
from django.http import JsonResponse

# Create your views here.


def api_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializers = ProductSerializers(products, many=True)
        return JsonResponse(serializers.data, safe=False)
