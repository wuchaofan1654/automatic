
from django.contrib.auth import get_user_model
from frames.serializers import CustomModelSerializer
from apps.point.models import Point

UserProfile = get_user_model()


class PointSerializer(CustomModelSerializer):
    """
    简单菜单序列化器
    """
    class Meta:
        model = Point
        # fields = '__all__'
        exclude = ('description',)
