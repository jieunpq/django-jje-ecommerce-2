from django.urls import path
# dev_28
# from api.views import hello_world, hello_world_json, hello_world_drf
from .views import base_views, product_views

urlpatterns = [
    path("hello-world/", base_views.hello_world),
    path("hello-world-json/", base_views.hello_world_json),
    path("hello-world-drf/", base_views.hello_world_drf),

    # 전체 목록
    path("products/", product_views.products_api, name="products_api"),

    # 단일 조회 및 수정
    path("products/<int:pk>/", product_views.product_detail_api, name="product_api"),
]
