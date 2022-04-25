# -*- coding: utf-8 -*-
"""
Create by sandy at 19:53 30/03/2022
Description: ToDo
"""

from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import PublishModelViewSet, ModuleModelViewSet

router = DefaultRouter()
router.register(r'publish', PublishModelViewSet)
router.register(r'module', ModuleModelViewSet)

urlpatterns = [
    re_path('publish/compare/(?P<pk1>.*)/(?P<pk2>.*)/', PublishModelViewSet.as_view({'get': 'compareByPk'})),
    re_path('publish/options/build', PublishModelViewSet.as_view({'get': 'buildOptions'})),
    re_path('publish/sync/(?P<pk>.*)/', PublishModelViewSet.as_view({'get': 'syncModules'})),
    re_path('module/options/name', ModuleModelViewSet.as_view({'get': 'nameOptions'})),
    re_path('module/stat/', ModuleModelViewSet.as_view({'get': 'moduleStat'})),
]
urlpatterns += router.urls
