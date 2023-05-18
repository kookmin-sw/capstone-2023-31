from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from product.views import get_random_product
from product import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path(" /", views.RandomListProduct.as_view()),
    path("search/", views.SearchProduct.as_view()),
    path("product/", include("product.urls")),
    path("analyze/", include("analyze.urls")),
    path("user/",include("user.urls")),
    path("",include("mypage.urls")),
    path("fitting/", include("fitting.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
