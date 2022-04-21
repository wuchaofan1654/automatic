from apps.project.models import Project
from apps.project.filters import ProjectFilter
from apps.project.serializers import ProjectSerializer
from frames.filters import DataLevelPermissionsFilter
from frames.viewsets import CustomModelViewSet


class ProjectModelViewSet(CustomModelViewSet):
    """
    项目管理 的CRUD视图
    """
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_class = ProjectFilter
    # 权限控制
    extra_filter_backends = [DataLevelPermissionsFilter]
    search_fields = ('name', 'type')
    ordering = ['create_datetime']  # 默认排序
