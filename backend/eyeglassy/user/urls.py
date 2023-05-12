from django.urls import path
from analyze import views
from django.views.decorators.csrf import csrf_exempt
app_name = "user"

urlpatterns = [
    path("", views.main, name="main"),#삭제 후, 배포
    path('signup/', views.analyze_face, name='analyze_face'),
    path('get-csrf-token/', csrf_exempt(views.get_csrf_token),
         name='get_csrf_token'),

]
