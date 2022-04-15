from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView

from frames.filters import DataLevelPermissionsFilter
from frames.response import SuccessResponse
from frames.viewsets import CustomModelViewSet
from apps.point.filters import PointFilter
from apps.point.models import Point
from apps.point.serializers import PointSerializer


class PointModelViewSet(CustomModelViewSet):
    """
    埋点管理 的CRUD视图
    """
    queryset = Point.objects.all()
    serializer_class = PointSerializer
    filter_class = PointFilter
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    search_fields = ('name',)
    ordering = ['key_yn', 'create_datetime']  # 默认排序
