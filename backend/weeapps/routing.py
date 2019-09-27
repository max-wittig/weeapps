from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from playground.consumers import WeeappsWebsocketConsumer
from django.conf.urls import re_path


application = ProtocolTypeRouter(
    {
        "websocket": AuthMiddlewareStack(
            URLRouter([re_path(r"ws", WeeappsWebsocketConsumer)])
        )
    }
)
