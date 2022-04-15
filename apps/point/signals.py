# -*- coding: utf-8 -*-
"""
Create by sandy at 11:35 28/03/2022
Description: ToDo
"""
from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(signal=pre_save)
def model_pre_save_callback(sender, **kwargs):
    pass

