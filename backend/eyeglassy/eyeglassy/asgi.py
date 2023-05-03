"""
ASGI config for eyeglassy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/asgi/
"""

from channels.http import AsgiHandler
from channels.auth import AuthMiddlewareStack
from channels.middleware import BaseMiddleware, MiddlewareMixin
import yourapp.routing
from django.urls import re_path
from channels.routing import ProtocolTypeRouter, URLRouter
import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eyeglassy.settings')

application = get_asgi_application()

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'yourproject.settings')
'''
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(
        face_detection.routing.websocket_urlpatterns
    ),
})


class CustomMiddleware(BaseMiddleware):
    ...




class CustomMiddleware(BaseMiddleware):
    ...


application = ProtocolTypeRouter({
    "http": SessionMiddleware(AsgiHandler()),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            your_routing
        )
    ),
    "websocket.http": AsgiHandler(),  # 추가
    "websocket.websocket": AuthMiddlewareStack(  # 추가
        URLRouter(
            your_routing
        )
    ),
})
'''
