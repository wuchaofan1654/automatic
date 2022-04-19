
from django.contrib.auth import get_user_model

from apps.permission.serializers import DeptSerializer, ModuleSerializer
from frames.serializers import CustomModelSerializer
from apps.api.models import Api, Param, Validator, Extractor, Result, Report

UserProfile = get_user_model()


class ParamSerializer(CustomModelSerializer):
    """
    简单参数序列化器
    """
    class Meta:
        model = Param
        exclude = ('description',)


class ValidatorSerializer(CustomModelSerializer):
    """
    简单验证器序列化器
    """
    class Meta:
        model = Validator
        exclude = ('description',)


class ExtractorSerializer(CustomModelSerializer):
    """
    简单提取器序列化器
    """
    class Meta:
        model = Extractor
        exclude = ('description',)


class ApiSerializer(CustomModelSerializer):
    """
    简单接口序列化器
    """
    dept = DeptSerializer(read_only=True)
    module = ModuleSerializer(read_only=True)
    params = ParamSerializer(many=True, read_only=True)
    validators = ValidatorSerializer(many=True, read_only=True)
    extractors = ExtractorSerializer(many=True, read_only=True)

    class Meta:
        model = Api
        fields = '__all__'


class UpdateApiSerializer(CustomModelSerializer):
    """
    接口器信息 简单序列化器
    """

    class Meta:
        model = Api
        fields = '__all__'


class ResultSerializer(CustomModelSerializer):
    """
    简单执行结果序列化器
    """

    api = ApiSerializer(read_only=True)

    class Meta:
        model = Result
        fields = '__all__'


class ReportSerializer(CustomModelSerializer):
    """
    简单测试报告序列化器
    """

    results = ResultSerializer(many=True, read_only=True)

    class Meta:
        model = Report
        fields = '__all__'
        depth = 1

