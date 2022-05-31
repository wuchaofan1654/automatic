from django.db import models

# Create your models here.
from django.db.models import SET_NULL

from application import settings
from frames.models import CoreModel, BaseModel


class Version(BaseModel):
    name = models.CharField(verbose_name='版本名称', max_length=50, default='')
    sys = models.IntegerField(verbose_name='系统', default=1, choices=((1, 'iOS'), (2, 'Android')))

    class Meta:
        verbose_name = '发布版本表'
        verbose_name_plural = verbose_name
        ordering = ['-id']

    def __str__(self):
        return f'{self.name}'


class Publish(CoreModel):
    version = models.ForeignKey(to='Version', on_delete=models.CASCADE)
    build_no = models.CharField(default='', max_length=50)
    branch = models.CharField(default='', max_length=255)
    filepath = models.CharField(default='', max_length=255)

    class Meta:
        verbose_name = '发布记录表'
        verbose_name_plural = '发布记录表'
        ordering = ['-id']

    def __str__(self):
        return f'{self.version}-{self.build_no}【{self.branch}】'


class Module(CoreModel):
    publish = models.ForeignKey(to='Publish', on_delete=models.CASCADE, default=0)
    module_name = models.CharField(default='', max_length=50)
    module_size = models.IntegerField(default=0)
    module_type = models.IntegerField(default=1)
    creator = models.ForeignKey(to=settings.AUTH_USER_MODEL, related_query_name='Module.creator', null=True,
                                verbose_name='创建者', on_delete=SET_NULL, db_constraint=False)  # 创建者

    class Meta:
        verbose_name = '模块大小表'
        verbose_name_plural = '模块大小表'
        ordering = ['-id']
        unique_together = [['publish', 'module_name']]

    def __str__(self):
        return self.module_name

