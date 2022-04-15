import logging

from django.apps import AppConfig

logger = logging.getLogger(__name__)


class OpDrfConfig(AppConfig):
    name = 'frames'
    verbose_name = "OP DRF"

    def ready(self):
        logging.info("OP DRF框架检测完成: success")
