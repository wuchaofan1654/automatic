
from frames.serializers import CustomModelSerializer
from apps.duplex.models import WebsocketLog


class WebsocketLogSerializer(CustomModelSerializer):
    """
    字典管理 简单序列化器
    """

    class Meta:
        model = WebsocketLog
        exclude = ('description', 'creator', 'modifier')
