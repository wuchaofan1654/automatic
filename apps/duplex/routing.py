# -*- coding: utf-8 -*-
"""
Create by sandy at 19:54 14/03/2022
Description: ToDo
"""
from django.urls import path

from apps.duplex.consumers.basicConsumer import BasicConsumer

websocket_urlpatterns = [
    path('ws/tailor/<int:uid>/<str:level>/', BasicConsumer.as_asgi()),
]
