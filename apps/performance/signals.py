# -*- coding: utf-8 -*-
"""
Create by sandy at 20:02 07/04/2022
Description: ToDo
"""
from django.db.models.signals import post_save
from django.dispatch import receiver

from application.settings import BASE_DIR
from .models import Publish, Module
from .serializers import PublishSerializer
import json
import re

import logging

logger = logging.getLogger(__name__)

import random


def sync_modules_by_publish(publish: Publish):
    try:
        serialized = PublishSerializer(publish).data
        json_file_path = BASE_DIR + re.findall(r'/media.*', serialized.get('filepath'))[0]
        modules = json.loads(open(json_file_path).read()).get('module_list')

        [Module.objects.create(
            module_name=module.get('module_name'),
            module_size=module.get('module_size') + random.randint(1, 1000),
            publish=publish
        ).save() for module in modules]

    except Exception as error:
        logger.exception(error)


@receiver(post_save, sender=Publish)
def publish_saved_callback(sender, **kwargs):
    instance = kwargs.get('instance')
    logger.info(f"{instance}: 同步modules...")
    sync_modules_by_publish(instance)
    logger.info(f"同步modules完成...")





