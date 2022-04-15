from django.apps import AppConfig


class PointConfig(AppConfig):
    name = 'apps.point'

    def ready(self):
        from .signals import model_pre_save_callback

