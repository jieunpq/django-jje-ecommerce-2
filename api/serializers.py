from rest_framework import serializers
from store.models import Product, Category

# 2. Serilaizer 객체의 주요 기능
# 1) serialization
# 2) deserialiaztion
# 3) validation
# 4) create(), update()
# 5) request / response 데이터 핸들링 ( to_internal_value() / to_representation() )
# 6) nested serialization

# dev_33
# 주의할 점
# dept는 읽기 전용 출력
# POST, PUT 요청에서 중렵된 객체를 직접 생성하거나 수정 불가
# 만약 쓰기도 원한다면 category_id 같은 별도 필드와 create() 오버라이드가 필요함


# dev_29
# class ProductSerializer(serializers.Serializer):
#     id = serializers.IntegerField()
#     name = serializers.CharField(max_length=100)
#     price = serializers.ImageField()
#     category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
#     description = serializers.CharField(
#         max_length=250, required=False, allow_blank=True, allow_null=True
#     )
#     image = serializers.ImageField()
#     is_sale = serializers.BooleanField()
#     sale_price = serializers.IntegerField()


# dev_32
class CategorySerializer(serializers.ModelSerializer):
    # dev_32 역방향 참조
    # products = ProductSerializer(many=True, read_only=True) # related_name=products
    
    class Meta:
        model = Category
        fields = "__all__"
        


# 객체를 => 딕셔너리로 만드는게 목적
class ProductSerializer(serializers.ModelSerializer):
    
    category = CategorySerializer(read_only=True) # write를 할려면 read only를 지우기
    
    class Meta:
        model = Product
        fields = "__all__"
        
    # def create(self, validated_data):
    #     category_data = validated_data.pop("category")
        
    #     # 카테고리 저장/조회
    #     category, _ = Category.objects.get_or_create(**category_data)
    #     product = Product.objects.create(**validated_data,category=category)

    #     return product
            
