"""allergypang URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include import path
from searchfood import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.test_main, name='test_main'),
    #path('scanmain/', views.get_barcode_img, name="scan_main"),
    #path("scan/",views.barcode_scan,name="scan"),
    path("search/", views.search_product_by_barcode, name="search"),
    path("detail/", views.search_detail_by_name, name="detail"),
    path("result/",views.search_nutrition_by_name,name="result"),
    path('record/', include('record.urls')),

]
