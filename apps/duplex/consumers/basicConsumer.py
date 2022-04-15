# -*- coding: utf-8 -*-
"""
Create by sandy at 11:25 25/03/2022
Description: ToDo
"""

from channels.generic.websocket import AsyncWebsocketConsumer

import json

from apps.duplex.models import WebsocketLog


class BasicConsumer(AsyncWebsocketConsumer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    async def connect(self):
        await self.channel_layer.group_add(
            self.scope['group_name'],
            self.channel_name
        )
        await self.accept()

        # 连接成功后的操作
        WebsocketLog.objects.create(
            group_name=self.scope['group_name'],
            url=self.scope['path'],
            kwargs=self.scope['url_route']['kwargs']
        ).save()

        await self.do_after_connect()

    async def do_after_connect(self):
        # 重写连接成功后的操作
        pass

    async def do_before_disconnect(self):
        # 重写关闭连接前的操作
        pass

    async def disconnect(self, close_code):
        # 关闭前执行操作
        await self.do_before_disconnect()

        await self.channel_layer.group_discard(
            self.scope['group_name'],
            self.channel_name
        )

    async def receive(self, text_data=None, bytes_data=None):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        await self.channel_layer.group_send(
            self.scope['group_name'],
            {
                'type': 'send.message',
                'message': message
            }
        )

    async def send_message(self, event):
        await self.send(text_data=json.dumps({
            'message': event['message']
        }))


