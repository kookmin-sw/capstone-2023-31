from django.urls import path
from analyze import views

app_name = "analyze"

urlpatterns = [
    path("", views.main, name="main"),
    path("upload/", views.upload, name="upload"),
    path("result/", views.show_result, name="result"),
]
