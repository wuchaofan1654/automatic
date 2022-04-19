# from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.api.views import ApiModelViewSet, ReportModelViewSet


router = DefaultRouter()
router.register(r'api', ApiModelViewSet)
router.register(r'report', ReportModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls
