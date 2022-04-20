# -*- coding: utf-8 -*-
"""
Create by sandy at 17:29 07/12/2021
Description: ToDo
"""

import django_filters

from apps.api.models import Api, Report, Project


class ApiFilter(django_filters.FilterSet):
    url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    key_yn = django_filters.CharFilter(field_name='key_yn', lookup_expr='icontains')
    dept = django_filters.CharFilter(field_name='dept.deptName', lookup_expr='icontains')
    module = django_filters.CharFilter(field_name='module.moduleName', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = Api
        fields = ('url', 'name', 'key_yn', 'dept', 'module', 'status', 'creator', 'create_datetime')


class ReportFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = Report
        fields = ('name', 'creator', 'create_datetime')


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = Project
        fields = ('name', 'creator', 'create_datetime')
