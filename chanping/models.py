# coding: utf-8
from django.db import models

class BaseModel(models.Model):
    createTime = models.DateTimeField(verbose_name=u'创建时间', auto_now_add=True)

    class Meta:
        abstract = True

# Create your models here.

class Happy(BaseModel):
    man = models.CharField(verbose_name=u'姓名（男）', max_length=100)
    human = models.CharField(verbose_name=u'姓名（女）', max_length=100)
    mettingtime = models.DateTimeField(verbose_name=u'遇见时间')
    pwd = models.CharField(verbose_name=u'秘钥', max_length=100)