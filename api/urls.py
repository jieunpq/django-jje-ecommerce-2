from django.urls import path
# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views, category_views

urlpatterns = [
    # path("hello-world/", base_views.hello_world),
    # path("hello-world-json/", base_views.hello_world_json),
    # path("hello-world-drf/", base_views.hello_world_drf),
    
    # 방식      URL             기능
    # GET      /products/      전체 상품 목록 조회 (List)
    # POST     /products/      새로운 상품 등록 (Create)
    # GET      /products/<pk>/ 단일 상품 상세 조회 (Retrieve)
    # PUT      /products/<pk>/ 단일 상품 정보 수정 (Update)
    # DELETE   /products/<pk>/ 단일 상품 삭제 (Delete)

    path("products/", product_views.products_api,), # 전체 목록
    path("product/<int:pk>/", product_views.products_api), # 단일 조회 및 수정
    
    # dev_32
    # 방식      url             기능
    # GET      categories/     list
    
    # path("categories/", category_views.categories_api),
 
    # dev_35
    path("categories/", category_views.CategoriesAPI.as_view()),
    
]
