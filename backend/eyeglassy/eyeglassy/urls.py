from django.contrib import admin
from django.urls import include, path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path("analyze/", include("analyze.urls")),
    path("user/",include("user.urls")),
    path("",include("mypage.urls")),
    path("fitting/", include("fitting.urls")),
    # path("", include("face_detection.urls")),
    path("product/", include("product.urls")),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
