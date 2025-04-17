from rest_framework import serializers
from store.models import Product, Category
from api.serializers.product_serializers import ProductSimpleSerializer


# dev_34
class CategorySimpleSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Category
        fields = ["id", "name"]
        
class CategorySerializer(serializers.ModelSerializer):
    
    products = ProductSimpleSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"