
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
PMS = 'PMS'

#有些声音
JDHG = 'JDHG'
BSBS = 'BSBS'
BFX = 'BFX'


class BoysAndGirlsManager(models.Manager):
    # num条男神信息
    def ns(self, num):
        n = self.filter(type=NS).count()
        if num>n:
            return self.filter(type=NS).order_by('-date')
        else:
            return self.filter(type=NS).order_by('-date')[0:num]

    # num条女神信息
    def nvs(self, num):
        n = self.filter(type=NVS).count()
        if num>n:
            return self.filter(type=NVS).order_by('-date')
        else:
            return self.filter(type=NVS).order_by('-date')[0:num]

    # 本周男帝
    def new_nd(self):
        n = self.filter(type=BZND).count()
        if n > 0:
            return self.filter(type=BZND).order_by('-date')[0]
        else:
            return None

    # 本周女帝
    def new_nvd(self):
        n = self.filter(type=BZNVD).count()
        if n > 0:
            return self.filter(type=BZNVD).order_by('-date')[0]
        else:
            return None

    # 一些男神
    def some_ns(self, start, end):
        n = self.filter(type=NS).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=NS).order_by('-date')[start:n]
        else:
            return self.filter(type=NS).order_by('-date')[start:end]

    # 一些女神
    def some_nvs(self, start, end):
        n = self.filter(type=NVS).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=NVS).order_by('-date')[start:n]
        else:
            return self.filter(type=NVS).order_by('-date')[start:end]


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
    photo = models.ImageField(upload_to='wechat/boysandgirls/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')
    url = models.URLField(max_length=500, blank=True, default='')

    objects = BoysAndGirlsManager()

    def __unicode__(self):
        return self.title


class FineFoodManager(models.Manager):

    # ‘包厢’推荐
    def bx(self, num):
        n = self.filter(type=BX).count()
        if num>n:
            return self.filter(type=BX).order_by('-date')
        else:
            return self.filter(type=BX).order_by('-date')[0:num]

    # ’食堂‘推荐
    def st(self, num):
        n = self.filter(type=ST).count()
        if num>n:
            return self.filter(type=ST).order_by('-date')
        else:
            return self.filter(type=ST).order_by('-date')[0:num]

    # '泡美食'
    def pms(self, num):
        n = self.filter(type=PMS).count()
        if num>n:
            return self.filter(type=PMS).order_by('-date')
        else:
            return self.filter(type=PMS).order_by('-date')[0:num]

    # 一些‘包厢’
    def some_bx(self, start, end):
        n = self.filter(type=BX).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=BX).order_by('-date')[start:n]
        else:
            return self.filter(type=BX).order_by('-date')[start:end]

    # 一些‘食堂’
    def some_st(self, start, end):
        n = self.filter(type=ST).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=ST).order_by('-date')[start:n]
        else:
            return self.filter(type=ST).order_by('-date')[start:end]

    def some_pms(self, start, end):
        n = self.filter(type=PMS).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=PMS).order_by('-date')[start:n]
        else:
            return self.filter(type=PMS).order_by('-date')[start:end]


class FineFood(models.Model):
    ft = (
        ('ST', u'食堂'),
        ('BX', u'包厢'),
        ('PMS', u'泡美食')
    )  # 美食类型

    title = models.CharField(max_length=100)
    type = models.CharField(choices=ft, max_length=10, help_text=u'选择美食类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    photo = models.ImageField(upload_to='wechat/findfood/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')
    url = models.URLField(max_length=500, blank=True, default='')

    objects = FineFoodManager()

    def __unicode__(self):
        return self.title


class VoiceManager(models.Manager):

    # 经典回顾
    def jdhg(self, num):
        n = self.filter(type=JDHG).count()
        if num>n:
            return self.filter(type=JDHG).order_by('-date')
        else:
            return self.filter(type=JDHG).order_by('-date')[0:num]

    # 不三不四
    def bsbs(self, num):
        n = self.filter(type=BSBS).count()
        if num>n:
            return self.filter(type=BSBS).order_by('-date')
        else:
            return self.filter(type=BSBS).order_by('-date')[0:num]

    # 摆饭秀
    def bfx(self, num):
        n = self.filter(type=BFX).count()
        if num>n:
            return self.filter(type=BFX).order_by('-date')
        else:
            return self.filter(type=BFX).order_by('-date')[0:num]

    # 一些 经典回顾
    def some_jdhg(self, start, end):
        n = self.filter(type=JDHG).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=JDHG).order_by('-date')[start:n]
        else:
            return self.filter(type=JDHG).order_by('-date')[start:end]

    # 一些BSBS
    def some_bsbs(self, start, end):
        n = self.filter(type=BSBS).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=BSBS).order_by('-date')[start:n]
        else:
            return self.filter(type=BSBS).order_by('-date')[start:end]

    # 一些摆饭秀
    def some_bfx(self, start, end):
        n = self.filter(type=BFX).count()
        if n<=start:
            return []
        elif n<end:
            return self.filter(type=BFX).order_by('-date')[start:n]
        else:
            return self.filter(type=BFX).order_by('-date')[start:end]

    # 通过ID获取voice
    def get_voice_by_id(self, v_id):
        try:
            obj = self.get(id=v_id)
            return obj
        except Exception, e:
            return None


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
    pic = models.ImageField(upload_to='wechat/voice_pic/%Y/%m', max_length=255, help_text=u'建议尺寸：大图360*200，小图200*200')
    audio = models.FileField(upload_to='wechat/voice/%Y/%m', max_length=255, help_text=u'请上传音频文件')

    objects = VoiceManager()

    def __unicode__(self):
        return self.title


class StaticMedia(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/staticmedia/%Y/%m', max_length=255, help_text=u'请上传多媒体文件')

    def __unicode__(self):
        return self.title


class FansKLL(models.Model):
    age = models.IntegerField(max_length=3, null=True)
    place = models.CharField(max_length=50, null=True)
    weight = models.IntegerField(max_length=4, null=True)
    hometown = models.CharField(max_length=50, null=True)
    height = models.FloatField(max_length=4, null=True)
    occupation = models.CharField(max_length=50, null=True)
    personality = models.CharField(max_length=50, null=True)
    hobby = models.CharField(max_length=50, null=True)
    weixin = models.CharField(max_length=50, null=True)
    qq = models.IntegerField(max_length=50, null=True)
    email = models.CharField(max_length=100, null=True)
    mobile = models.IntegerField(max_length=50, default=11111111111)
    open_mobile = models.BooleanField(default=True, verbose_name=u"公开手机号码")

    date = models.DateTimeField(auto_now_add=True)
    fan = models.CharField(max_length=600, blank=True)
    intro = models.TextField(max_length=5000, null=True)
    files = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.intro[0:10]


class FansKLLMedia(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/fanskllmedia/%Y/%m/%d', max_length=500)
    belong = models.ForeignKey(FansKLL, null=True)

    def __unicode__(self):
        return str(self.id)


class FansMSTJ(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fan = models.CharField(max_length=600, blank=True)
    intro = models.CharField(max_length=5000, null=True)
    files = models.CharField(max_length=100, null=True)

    def __unicode__(self):
        return self.intro[0:10]


class FansMSTJMedia(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/fansmstjmedia/%Y/%m/%d', max_length=500)
    belong = models.ForeignKey(FansMSTJ, null=True)

    def __unicode__(self):
        return str(self.id)















