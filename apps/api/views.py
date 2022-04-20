from apps.api.filters import ApiFilter, ReportFilter, ProjectFilter
from apps.api.models import Api, Report, Project
from apps.api.serializers import ApiSerializer, ReportSerializer, ProjectSerializer
from apps.api.serializers import UpdateApiSerializer
from frames.viewsets import CustomModelViewSet
from apps.permission.permissions import CommonPermission


class ApiModelViewSet(CustomModelViewSet):
    """
    接口器信息 模型的CRUD视图
    """
    queryset = Api.objects.all()
    serializer_class = ApiSerializer
    update_serializer_class = UpdateApiSerializer
    # extra_filter_backends = [DataLevelPermissionsFilter]
    filter_class = ApiFilter
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = '-create_datetime'  # 默认排序


class ReportModelViewSet(CustomModelViewSet):
    """
    接口执行报告器信息 模型的CRUD视图
    """
    queryset = Report.objects.all()
    serializer_class = ReportSerializer
    # extra_filter_backends = [DataLevelPermissionsFilter]
    filter_class = ReportFilter
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = '-create_datetime'  # 默认排序


class ProjectModelViewSet(CustomModelViewSet):
    """
    项目信息 模型的CRUD视图
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    # extra_filter_backends = [DataLevelPermissionsFilter]
    filter_class = ProjectFilter
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    ordering = '-create_datetime'  # 默认排序
