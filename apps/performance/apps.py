from django.apps import AppConfig


class PerformanceConfig(AppConfig):
    name = 'apps.performance'

    def ready(self):
        from .signals import publish_saved_callback
