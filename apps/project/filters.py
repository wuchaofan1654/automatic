# -*- coding: utf-8 -*-
"""
Create by sandy at 17:29 07/12/2021
Description: ToDo
"""

import django_filters

from apps.project.models import Project


class ProjectFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains')

    class Meta:
        model = Project
        fields = ('name', 'type')
