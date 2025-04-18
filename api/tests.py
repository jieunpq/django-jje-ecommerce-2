from django.test import TestCase
import pickle
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from store.models import Category
from api.serializers.category_serializers import CategorySerializer, CategorySimpleSerializer


# Create your tests here.
        
# def add(num1,num2):
#     return num1 + num2

# def sub(num1,num2):
#     return num1 - num2

        
# class ObjectAPITest(TestCase):
#     def setUp(self):
#         pass
    
#     def test_path(self):
        
#         dict = {
#             "add": add,
#             "sub": sub,
#         }
        
#         url = "add"
#         print(dict[url](1, 2))
        
#         url = "sub"
#         print(dict[url](1, 2))
        
class CategoriesAPI(APIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    simple_serializer_class = CategorySimpleSerializer

    def get_queryset(self):
        return self.queryset

    def get_serializer(self, *args, **kwargs):
        return self.serializer_class(*args, **kwargs)

    def get_simple_serializer(self, *args, **kwargs):
        return self.simple_serializer_class(*args, **kwargs)

    def get(self, request):
        categories = self.get_queryset()
        serializer = self.get_serializer(categories, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = self.get_simple_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        # 예: id를 request에서 받았다고 가정
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)

        serializer = self.get_simple_serializer(category, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request):
        category_id = request.data.get("id")
        try:
            category = self.get_queryset().get(id=category_id)
            category.delete()
            return Response({"message": "Category deleted"}, status=status.HTTP_204_NO_CONTENT)
        except Category.DoesNotExist:
            return Response({"error": "Category not found"}, status=status.HTTP_404_NOT_FOUND)
            