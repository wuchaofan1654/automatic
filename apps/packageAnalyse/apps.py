from django.apps import AppConfig


class PackageAnalyseConfig(AppConfig):
    name = 'apps.packageAnalyse'

    def ready(self):
        pass
        # from .signals import publish_saved_callback
