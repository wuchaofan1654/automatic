import django_filters

from apps.duplex.models import WebsocketLog


class WebsocketLogFilter(django_filters.rest_framework.FilterSet):
    """
    字典管理 简单过滤器
    """
    group_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = WebsocketLog
        fields = '__all__'
