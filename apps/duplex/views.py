from django.shortcuts import render

# Create your views here.
from rest_framework.request import Request

from apps.duplex.filters import WebsocketLogFilter
from apps.duplex.models import WebsocketLog
from apps.duplex.serializers import WebsocketLogSerializer
from frames.response import SuccessResponse
from frames.viewsets import CustomModelViewSet


class WebsocketLogModelViewSet(CustomModelViewSet):
    """
   websocket操作日志 模型的CRUD视图
   """
    queryset = WebsocketLog.objects.all()
    serializer_class = WebsocketLogSerializer
    filter_class = WebsocketLogFilter

    # def clean_all(self, request: Request, *args, **kwargs):
    #     self.get_queryset().delete()
    #     return SuccessResponse(msg="清空成功")


