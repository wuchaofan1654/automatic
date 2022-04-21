"""application URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import re_path, include
from django.views.static import serve

from application import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    re_path(r'media/(?P<path>.*)', serve, {"document_root": settings.MEDIA_ROOT}),

    re_path(r'^api/', include('apps.api.urls')),
    re_path(r'^point/', include('apps.point.urls')),
    re_path(r'^shortcut/', include('apps.shortcut.urls')),
    re_path(r'^duplex/', include('apps.duplex.urls')),
    re_path(r'^testcase/', include('apps.testcase.urls')),
    re_path(r'^performance/', include('apps.performance.urls')),
    re_path(r'^celery/', include('apps.celery.urls')),
    re_path(r'^monitor/', include('apps.monitor.urls')),

    re_path(r'^permission/', include('apps.permission.urls')),
    re_path(r'^system/', include('apps.system.urls')),

    re_path(r'^drf/', include('frames.urls')),

    re_path(r'^project/', include('apps.project.urls')),
]
