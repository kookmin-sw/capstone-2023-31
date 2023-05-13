
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views


urlpatterns = [  # 메인페이지는 url 구현 x, mypage 구현
    path("setprofile/", views.setprofile, name="setprofile"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
