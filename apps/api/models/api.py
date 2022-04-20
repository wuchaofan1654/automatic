# -*- coding: utf-8 -*-
"""
Create by sandy at 16:55 18/04/2022
Description: ToDo
"""
from django.db import models

from frames.models import CoreModel


EXPRESSION_TYPE_CHOICES = (
    (1, 'Json 路径'),
    (2, '正则表达式'),
    (3, 'Mysql表达式')
)


class Api(CoreModel):
    METHOD_CHOICES = (
        (1, 'GET'),
        (2, 'POST'),
        (3, 'PUT'),
        (4, 'DELETE'),
    )
    KEY_YN_CHOICES = (
        (1, '是'),
        (0, '否')
    )
    name = models.CharField(default='', max_length=255, verbose_name='接口名称(unique)', unique=True)
    url = models.CharField(default='', max_length=255, verbose_name='接口路径(不带host)')
    method = models.IntegerField(default=1, choices=METHOD_CHOICES, verbose_name='请求方式')
    key_yn = models.IntegerField(default=0, choices=KEY_YN_CHOICES, verbose_name='是否核心接口')
    dept = models.ForeignKey(to='permission.Dept', on_delete=models.CASCADE, default=0, verbose_name='所属团队')
    module = models.ForeignKey(to='permission.Module', on_delete=models.CASCADE, default=0, verbose_name='关联模块')
    status = models.IntegerField(default=1, verbose_name='状态')
    params = models.ManyToManyField(to='Param', verbose_name='关联参数')
    validators = models.ManyToManyField(to='Validator', verbose_name='关联验证器')
    extractors = models.ManyToManyField(to='Extractor', verbose_name='关联提取器')

    class Meta:
        verbose_name = '接口主表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Param(CoreModel):
    PARAM_TYPE_CHOICES = (
        (1, 'str'),
        (2, 'int'),
        (3, 'list'),
        (4, 'dict'),
        (5, 'file'),
    )

    REQUIRE_CHOICES = (
        (1, '必填'),
        (2, '非必填'),
    )

    key = models.CharField(default='', max_length=255, verbose_name='参数名称')
    value = models.CharField(default='', max_length=255, verbose_name='参数值')
    type = models.IntegerField(default=1, choices=PARAM_TYPE_CHOICES, verbose_name='参数类型')
    require = models.IntegerField(default=0, choices=REQUIRE_CHOICES, verbose_name='是否必填')

    class Meta:
        verbose_name = '请求参数表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.key} = {self.value}'


class Validator(CoreModel):
    SYMBOL_CHOICES = (
        ('=', 'equals'),
        ('str=', 'equals as str'),
        ('int=', 'equals as int'),
        ('in', 'in'),
        ('not in', 'not in'),
        ('contains', 'contains'),
        ('not contains', 'not contains'),
        ('is null', 'is null'),
        ('not null', 'not null'),
    )
    expression = models.CharField(default='', max_length=255, verbose_name='验证表达式')
    expression_type = models.IntegerField(default=1, choices=EXPRESSION_TYPE_CHOICES, verbose_name='表达式类型')
    excepted = models.CharField(default='', max_length=255, verbose_name='期望值', blank=True, null=True)
    symbol = models.CharField(default='=', max_length=50, choices=SYMBOL_CHOICES, verbose_name='比较符')

    class Meta:
        verbose_name = '验证器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.expression}[{self.expression_type}]'


class Extractor(CoreModel):
    expression = models.CharField(default='', max_length=255, verbose_name='提取表达式')
    expression_type = models.IntegerField(default=1, choices=EXPRESSION_TYPE_CHOICES,  verbose_name='表达式类型')
    variable = models.CharField(default='', max_length=255, verbose_name='赋值变量名')

    class Meta:
        verbose_name = '提取器'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.expression}[{self.expression_type}]'


class Result(CoreModel):
    api = models.ForeignKey(default=0, on_delete=models.CASCADE, to='Api', verbose_name='关联接口')
    message = models.TextField(default='succeed', verbose_name='执行结果')

    class Meta:
        verbose_name = '接口执行结果'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.api.name}执行结果'


class Report(CoreModel):
    name = models.CharField(default='接口测试报告', max_length=80)
    results = models.ManyToManyField(to='Result', verbose_name='关联结果')

    class Meta:
        verbose_name = '执行报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Project(CoreModel):
    name = models.CharField(default='', max_length=255, verbose_name='项目名称(unique)', unique=True)
    apis = models.ManyToManyField(to='Api', verbose_name='接口列表')

    class Meta:
        verbose_name = '项目列表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

