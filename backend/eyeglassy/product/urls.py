from django.urls import path
from product import views

app_name = 'product'

urlpatterns = [
    path('load_glasses_data/', views.load_glasses_data, name='load_glasses_data'),
    # path('analyze-face/', views.analyze_face, name='analyze_face'),
]