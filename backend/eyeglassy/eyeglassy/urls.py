from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings
from product.views import get_random_product

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_random_product),
    path("product/", include("product.urls")),
    path("analyze/", include("analyze.urls")),
    path("user/",include("user.urls")),
    # path("",include("mypage.urls")),
    path("fitting/", include("fitting.urls")),
    # path("", include("face_detection.urls")),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
