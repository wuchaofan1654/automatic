# -*- coding: utf-8 -*-
"""
Create by sandy at 11:04 25/03/2022
Description: ToDo
"""
from rest_framework.routers import DefaultRouter

from apps.project.views import ProjectModelViewSet

router = DefaultRouter()
router.register(r'project', ProjectModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls
