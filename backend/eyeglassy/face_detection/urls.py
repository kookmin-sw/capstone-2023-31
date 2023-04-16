
from django.urls import re_path
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from face_detection import views


urlpatterns = [
    path("",views.main,name="main"),
    #path("detect/", views.faceDetect, name="facedetect"),
    path('camera/', views.video_feed, name='video_feed'),  # 수정된 부분
    # path('video_feed/', views.video_feed, name='video_feed'),
    path('eye_info/', views.eye_info, name='eye_info'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
websocket_urlpatterns = [
    re_path(r'ws/video_feed/$', consumers.VideoFeedConsumer.as_asgi()),
    re_path(r'ws/face_detection/$', consumers.FaceDetectionConsumer.as_asgi()),
]
'''
