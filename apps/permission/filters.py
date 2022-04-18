import django_filters
from django.contrib.auth import get_user_model

from apps.permission.models import Menu, Dept, Post, Role, Module
from frames.utils.model_util import get_dept

UserProfile = get_user_model()


class MenuFilter(django_filters.rest_framework.FilterSet):
    """
    菜单管理 简单序过滤器
    """
    name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Menu
        exclude = ('description', 'creator', 'modifier')


class DeptFilter(django_filters.rest_framework.FilterSet):
    """
    部门管理 简单序过滤器
    """
    deptName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Dept
        exclude = ('description', 'creator', 'modifier')


class ModuleFilter(django_filters.rest_framework.FilterSet):
    """
    模块管理 简单序过滤器
    """
    moduleName = django_filters.CharFilter(lookup_expr='icontains')
    # dept_id = django_filters.CharFilter(field_name='dept.id', lookup_expr='icontains')

    class Meta:
        model = Module
        fields = '__all__'


class PostFilter(django_filters.rest_framework.FilterSet):
    """
    岗位管理 简单序过滤器
    """
    postName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Post
        exclude = ('description', 'creator', 'modifier')


class RoleFilter(django_filters.rest_framework.FilterSet):
    """
    角色管理 简单序过滤器
    """
    roleName = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Role
        exclude = ('description', 'creator', 'modifier')


class UserProfileFilter(django_filters.rest_framework.FilterSet):
    """
    用户管理 简单序过滤器
    """
    username = django_filters.CharFilter(lookup_expr='icontains')
    mobile = django_filters.CharFilter(lookup_expr='icontains')
    deptId = django_filters.CharFilter(method='filter_deptId')

    def filter_deptId(self, queryset, name, value):
        return queryset.filter(dept__id__in=get_dept(dept_id=value))

    class Meta:
        model = UserProfile
        exclude = ('secret', 'password', 'avatar')
