from django.urls import path
from product import views
from django.views.decorators.csrf import csrf_exempt
from .models import Glasses

app_name = 'product'

urlpatterns = [
    path('', views.ListProduct.as_view(), name='product_list'), # list, url 수정 필요
    path('<int:pk>/', views.DetailProduct.as_view(), name='product_detail'),
    path('get-csrf-token/', csrf_exempt(views.get_csrf_token),
         name='get_csrf_token'),
]