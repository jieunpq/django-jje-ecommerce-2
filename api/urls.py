from django.urls import path
# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views, category_views

urlpatterns = [
    path("hello-world/", base_views.hello_world),
    path("hello-world-json/", base_views.hello_world_json),
    path("hello-world-drf/", base_views.hello_world_drf),
    path("products/", product_views.products_api,), # 전체 목록
    path("product/<int:pk>/", product_views.products_api), # 단일 조회 및 수정
    # dev_32
    path("categories/", category_views.categories_api),
    
]
