# Create your views here.
from apps.duplex.filters import WebsocketLogFilter
from apps.duplex.models import WebsocketLog
from apps.duplex.serializers import WebsocketLogSerializer
from frames.viewsets import CustomModelViewSet


class WebsocketLogModelViewSet(CustomModelViewSet):
    """
   websocket操作日志 模型的CRUD视图
   """
    queryset = WebsocketLog.objects.all()
    serializer_class = WebsocketLogSerializer
    filter_class = WebsocketLogFilter
