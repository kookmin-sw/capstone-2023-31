from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
    path('', views.ListPost.as_view(), name='product_list'), # list, url 수정 필요
    path('<int:id>/', views.DetailPost.as_view(), name='product_detail'), # 안됨
]