from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/<str:jam_session_name>/', consumers.ChatConsumer),
    path('ws/grid/<str:jam_session_name>/', consumers.GridConsumer),
]
