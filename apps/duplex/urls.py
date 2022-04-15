from django.urls import re_path
from rest_framework.routers import DefaultRouter

from apps.duplex.views import WebsocketLogModelViewSet

router = DefaultRouter()
router.register(r'duplex', WebsocketLogModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls
