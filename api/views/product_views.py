from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from store.models import Product, Category
from django.shortcuts import get_object_or_404

# dev_32
from api.serializers.product_serializers import ProductSerializer

# http://127.0.0.1:8000/api/products/
# 방식   url         기능
# GET   products/    list
# POST  products/    create

# 단일 상품 GET, PUT(수정), DELETE
@api_view(["GET", "POST"])
def products_api(request):
    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    if request.method == "POST":
        
        data = request.data.copy()

        category_data = data.pop("category")
        
        # 리스트 형태로 들어올 경우 첫 번째 dict만 사용
        if isinstance(category_data, list):
            category_data = category_data[0]

        # category_data는 반드시 dict여야 함
        category, _ = Category.objects.get_or_create(**category_data)

        # 남은 데이터로 product 생성
        serializer = ProductSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save(category=category)

        return Response(serializer.data)
