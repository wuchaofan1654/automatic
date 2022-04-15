from django.db import models

# Create your models here.
from frames.models import BaseModel


class Point(BaseModel):
    zh_name = models.CharField(default='', max_length=100)
    sys = models.IntegerField(default=1)
    point_type = models.IntegerField(default=1)
    key_yn = models.IntegerField(default=1)
    from_page = models.CharField(default='', max_length=100)
    from_page_ext = models.TextField(default='')
    curr_page = models.CharField(default='', max_length=100)
    curr_page_ext = models.TextField(default='')
    from_action = models.CharField(default='', max_length=100)
    from_action_ext = models.TextField(default='')

    class Meta:
        verbose_name = '标准埋点表'
        verbose_name_plural = verbose_name


class PointExtend(BaseModel):
    ctime = models.IntegerField(default=0)
    point_type = models.IntegerField(default=1)
    from_page = models.CharField(default='', max_length=100)
    from_page_ext = models.TextField(default='')
    curr_page = models.CharField(default='', max_length=100)
    curr_page_ext = models.TextField(default='')
    from_action = models.CharField(default='', max_length=100)
    from_action_ext = models.TextField(default='')
    details = models.TextField(default='')

    class Meta:
        verbose_name = '拦截埋点记录表'
        verbose_name_plural = verbose_name




