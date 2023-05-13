from django.urls import path
from analyze import views
from django.views.decorators.csrf import csrf_exempt
app_name = "analyze"

urlpatterns = [
    path("", views.main, name="main"),
    path('analyze-face/', views.analyze_face, name='analyze_face'),
    path('get-csrf-token/', csrf_exempt(views.get_csrf_token),
         name='get_csrf_token'),
    path('save-face-shape/',views.save_faceshape, name="save_faceshape"),

]
