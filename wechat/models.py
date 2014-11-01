
# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.


class BoysAndGirls(models.Model):
    pt = (
        ('NS', u'男神'),
        ('NVS', u'女神'),
        ('BZNS', u'本周男神'),
        ('BZNVS', u'本周女神')
    )  # person type
    title = models.CharField(max_length=100)
    type = models.CharField(choices=pt, max_length=10, help_text=u'选择人物类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='boysandgirls/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')

    def __unicode__(self):
        return self.title


class FineFood(models.Model):
    ft = (
        ('ST', u'食堂'),
        ('BX', u'包厢')
    )  # 美食类型

    title = models.CharField(max_length=100)
    type = models.CharField(choices=ft, max_length=10, help_text=u'选择美食类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='findfood/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')

    def __unicode__(self):
        return self.title


class Voice(models.Model):
    vt = (
        ('JDHG', u'经典回顾'),
        ('BSBS', u'不三不四'),
        ('BFX', u'摆饭秀')
    )  # 声音类型

    title = models.CharField(max_length=100)
    type = models.CharField(choices=vt, max_length=10, help_text=u'选择节目类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    audio = models.FileField(upload_to='voice/%Y/%m', max_length=255)

    def __unicode__(self):
        return self.title




