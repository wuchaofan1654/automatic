from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from .models import Module, Publish


class PublishSerializer(ModelSerializer):
    """
    简单发布记录序列化器
    """
    create_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)

    class Meta:
        model = Publish
        fields = '__all__'


class PublishCreateUpdateSerializer(ModelSerializer):
    """
    发布记录管理 创建/更新时的列化器
    """
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Publish
        fields = '__all__'


class ModuleSerializer(ModelSerializer):
    """
    简单模块序列化器
    """
    create_datetime = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    publish = PublishSerializer(read_only=True)

    class Meta:
        model = Module
        fields = '__all__'


class ModuleStatSerializer(ModelSerializer):
    """
    简单模块序列化器
    """
    publish = PublishSerializer(read_only=True)

    class Meta:
        model = Module
        fields = ('publish', 'module_size')



