from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.models import Product, Category
from api.serializers import ProductSerializer, CategorySerializer

@api_view(["GET", "POST"])
def categories_api(request):
    if request.method == "GET":
        categories = Category.objects.all()
        serializer = CategorySerializer(categories, many=True)
        return Response(serializer.data)
