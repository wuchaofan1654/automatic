# -*- coding: utf-8 -*-
"""
Create by sandy at 11:04 25/03/2022
Description: ToDo
"""
# from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.point.views import PointModelViewSet

router = DefaultRouter()
router.register(r'point', PointModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls
