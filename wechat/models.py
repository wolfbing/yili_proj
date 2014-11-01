
# -*- coding: utf-8 -*-

from django.db import models
from django.db.models import manager

# Create your models here.
# 有些朋友
NS = 'NS'
NVS = 'NVS'
BZND = 'BZND'
BZNVD = 'BZNVD'

# 有些美食
BX = 'BX'
ST = 'ST'

#有些声音
JDHG = 'JDHG'
BSBS = 'BSBS'
BFX = 'BFX'


class BoysAndGirlsManager(models.Manager):
    # num条男神信息
    def ns(self, num):
        n = self.filter(type=NS).count()
        if num>n:
            return self.filter(type=NS).order_by('date')
        else:
            return self.filter(type=NS).order_by('date')[0:num]

    # num条女神信息
    def nvs(self, num):
        n = self.filter(type=NVS).count()
        if num>n:
            return self.filter(type=NVS).order_by('date')
        else:
            return self.filter(type=NVS).order_by('date')[0:num]

    # 本周男帝
    def new_nd(self):
        n = self.filter(type=BZND).count()
        if n > 0:
            return self.filter(type=BZND).order_by('date')[0]
        else:
            return None

    # 本周女帝
    def new_nvd(self):
        n = self.filter(type=BZNVD).count()
        if n > 0:
            return self.filter(type=BZNVD).order_by('date')[0]
        else:
            return None


class BoysAndGirls(models.Model):
    pt = (
        (NS, u'男神'),
        (NVS, u'女神'),
        (BZND, u'本周男帝'),
        (BZNVD, u'本周女帝')
    )  # person type
    title = models.CharField(max_length=100)
    type = models.CharField(choices=pt, max_length=10, help_text=u'选择人物类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='boysandgirls/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')
    url = models.URLField(max_length=500, blank=True, default='')

    objects = BoysAndGirlsManager()

    def __unicode__(self):
        return self.title


class FineFoodManager(models.Manager):

    # ‘包厢’推荐
    def bx(self, num):
        n = self.filter(type=BX).count()
        if num>n:
            return self.filter(type=BX).order_by('date')
        else:
            return self.filter(type=BX).order_by('date')[0:num]

    # ’食堂‘推荐
    def st(self, num):
        n = self.filter(type=ST).count()
        if num>n:
            return self.filter(type=ST).order_by('date')
        else:
            return self.filter(type=ST).order_by('date')[0:num]


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
    url = models.URLField(max_length=500, blank=True, default='')

    objects = FineFoodManager()

    def __unicode__(self):
        return self.title


class VoiceManager(models.Manager):

    # 经典回顾
    def jdhg(self, num):
        n = self.filter(type=JDHG).count()
        if num>n:
            return self.filter(type=JDHG).order_by('date')
        else:
            return self.filter(type=JDHG).order_by('date')[0:num]

    # 不三不四
    def bsbs(self, num):
        n = self.filter(type=BSBS).count()
        if num>n:
            return self.filter(type=BSBS).order_by('date')
        else:
            return self.filter(type=BSBS).order_by('date')[0:num]

    # 摆饭秀
    def bfx(self, num):
        n = self.filter(type=BFX).count()
        if num>n:
            return self.filter(type=BFX).order_by('date')
        else:
            return self.filter(type=BFX).order_by('date')[0:num]


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
    url = models.URLField(max_length=500, blank=True, default='')

    objects = VoiceManager()

    def __unicode__(self):
        return self.title




