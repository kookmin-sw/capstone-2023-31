from django.urls import path
from fitting import views
from django.views.decorators.csrf import csrf_exempt
app_name = 'fitting'

urlpatterns = [
    path('camera/<int:id>/', views.fitting_face, name='fitting_face'),
    path('get-csrf-token/', csrf_exempt(views.get_csrf_token),name='get_csrf_token'),
]
