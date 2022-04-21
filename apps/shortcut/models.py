from django.db import models

from frames.models import BaseModel, CoreModel


class Shortcut(CoreModel):
    name = models.CharField(default='', max_length=100)
    desc = models.IntegerField(default=1)
    module = models.IntegerField(default=1)
    cmd = models.CharField(default='', max_length=100)

    class Meta:
        verbose_name = '标准埋点表'
        verbose_name_plural = verbose_name



