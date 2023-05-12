from django.urls import path
from fitting import views
from django.views.decorators.csrf import csrf_exempt
app_name = 'fitting'

urlpatterns = [
    path('', views.main, name='main'),
    path('camera/', views.fitting_camera, name='fitting_camera'), # /fitting/camera
    path('result/', views.fitting_result, name='fitting_result'), # /fitting/result
    # path('get-csrf-token/', csrf_exempt(views.get_csrf_token),
    #     name='get_csrf_token'),
]
