from django.db import models

# Create your models here.
from django.db.models import CharField, IntegerField, ForeignKey, CASCADE

from frames.models import BaseModel, CoreModel


class Shortcut(CoreModel):
    name = models.CharField(default='', max_length=100)
    desc = models.IntegerField(default=1)
    module = models.IntegerField(default=1)
    cmd = models.CharField(default='', max_length=100)

    class Meta:
        verbose_name = '标准埋点表'
        verbose_name_plural = verbose_name


class Module(CoreModel):
    moduleName = CharField(max_length=64, verbose_name="部门名称")
    orderNum = IntegerField(verbose_name="显示排序")
    owner = CharField(max_length=32, verbose_name="负责人", null=True, blank=True)
    status = CharField(max_length=8, verbose_name="模块状态", null=True, blank=True)
    parentId = ForeignKey(to='Module', on_delete=CASCADE, default=False, verbose_name="上级模块",
                          db_constraint=False, null=True, blank=True)

    class Meta:
        verbose_name = '标准埋点表'
        verbose_name_plural = verbose_name



