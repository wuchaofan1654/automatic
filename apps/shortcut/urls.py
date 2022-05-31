# -*- coding: utf-8 -*-
"""
Create by sandy at 11:04 25/03/2022
Description: ToDo
"""


from django.urls import re_path

from apps.shortcut.views import ShortcutModelViewSet

urlpatterns = [
    re_path(r'result', ShortcutModelViewSet.as_view({'post': 'get_result'}))
]
