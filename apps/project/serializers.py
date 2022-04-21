
from django.contrib.auth import get_user_model
from frames.serializers import CustomModelSerializer
from apps.project.models import Project

UserProfile = get_user_model()


class ProjectSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Project
        # fields = '__all__'
        exclude = ('description',)
