from django.db import models

# Create your models here.
from frames.models import BaseModel


class Project(BaseModel):
    name = models.CharField(default='', max_length=100)
    type = models.IntegerField(default=0)

    class Meta:
        verbose_name = '项目表'
        verbose_name_plural = verbose_name



