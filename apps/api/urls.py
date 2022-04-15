# -*- coding: utf-8 -*-
"""
Create by sandy at 11:04 25/03/2022
Description: ToDo
"""


from django.urls import re_path
from .views import test_view


urlpatterns = [
    re_path(r'^(?P<api_id>\d+)', test_view),
    re_path(r'^suite', test_view)
]
