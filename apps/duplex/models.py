from django.db import models

# Create your models here.
from django.db.models import CharField, TextField, BooleanField

from frames.models import CoreModel


class WebsocketLog(CoreModel):
    group_name = CharField(max_length=256, verbose_name='分组名称', help_text='分组名称')
    url = CharField(max_length=256, verbose_name='连接url', help_text='请求链接')
    kwargs = TextField(max_length=1024, verbose_name='执行参数', help_text='运行参数')
    status = BooleanField(default=True, verbose_name='运行状态')

    class Meta:
        verbose_name = 'websocket日志'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.creator and self.creator.name}"
