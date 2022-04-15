# -*- coding: utf-8 -*-
"""
Create by sandy at 17:29 07/12/2021
Description: ToDo
"""

import django_filters

from apps.point.models import Point


class PointFilter(django_filters.FilterSet):
    zh_name = django_filters.CharFilter(field_name='zh_name', lookup_expr='icontains')
    point_type = django_filters.CharFilter(field_name='point_type', lookup_expr='icontains')
    key_yn = django_filters.CharFilter(field_name='key_yn', lookup_expr='icontains')
    status = django_filters.CharFilter(field_name='status', lookup_expr='icontains')
    creator = django_filters.CharFilter(field_name='creator', lookup_expr='id')
    start = django_filters.CharFilter(field_name='create_datetime', lookup_expr='gt')
    end = django_filters.CharFilter(field_name='create_datetime', lookup_expr='lt')

    class Meta:
        model = Point
        fields = ('zh_name', 'point_type', 'key_yn', 'creator', 'status', 'create_datetime')
