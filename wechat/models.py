
# -*- coding: utf-8 -*-

from django.db import models
from yili_proj.local_settings import HOST_NAME
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
    # 最新的num条男神信息
    def ns(self, num):
        n = self.filter(type=NS).count()
        if num>n:
            return self.filter(type=NS).order_by('-date')
        else:
            return self.filter(type=NS).order_by('-date')[0:num]

    # 最新的num条女神信息
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

    # 男神数量
    def ns_num(self):
        return self.filter(type=NS).count()

    # 女神数量
    def nvs_num(self):
        return self.filter(type=NVS).count()

# 男神女神发布
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

    class Meta:
        verbose_name = u"男神女神(发布)"


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

    # 最新num个'泡美食'
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

    def pms_num(self):
        return self.filter(type=PMS).count()

# 美食发布
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

    class Meta:
        verbose_name = u"美食推荐(发布)"


class VoiceManager(models.Manager):

    # 最新num个经典回顾
    def jdhg(self, num):
        n = self.filter(type=JDHG).count()
        if num>n:
            return self.filter(type=JDHG).order_by('-date')
        else:
            return self.filter(type=JDHG).order_by('-date')[0:num]

    # 最新num个不三不四
    def bsbs(self, num):
        n = self.filter(type=BSBS).count()
        if num>n:
            return self.filter(type=BSBS).order_by('-date')
        else:
            return self.filter(type=BSBS).order_by('-date')[0:num]

    # 最新num个摆饭秀
    # 返回list
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

    # 经典回顾的数量
    def jdhg_num(self):
        return self.filter(type=JDHG).count()

    # 不三不四的数量
    def bsbs_num(self):
        return self.filter(type=BSBS).count()

    # 摆饭秀的数量
    def bfx_num(self):
        return self.filter(type=BFX).count()

# 音频发布
class Voice(models.Model):
    vt = (
        ('JDHG', u'经典回顾'),
        ('BSBS', u'不三不四'),
        ('BFX', u'摆饭秀')
    )  # 声音类型

    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, null=True, blank=True, default=u"")
    type = models.CharField(choices=vt, max_length=10, help_text=u'选择节目类型')
    intro = models.TextField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    pic = models.ImageField(upload_to='wechat/voice_pic/%Y/%m', max_length=255, help_text=u'要求尺寸：360：200')
    player_pic = models.ImageField(upload_to='wechat/voice_pic/%Y/%m', null=True,max_length=255, help_text=u"要求尺寸：1：1，最小200*200")
    audio = models.FileField(upload_to='wechat/voice/%Y/%m', max_length=255, null=True, blank=True, help_text=u'请上传音频文件, audio与URL至少填一个哦！！')
    url = models.URLField(max_length=500, null=True, blank=True, default=u'', help_text=u'填写需要指定的页面链接，audio与URL至少选一个哦！！')

    objects = VoiceManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"音频(发布)"

# 媒体文件
class StaticMedia(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/staticmedia/%Y/%m', max_length=255, help_text=u'请上传多媒体文件')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"媒体文件"


# 括拉拉档案-投稿
class FansKLL(models.Model):
    age = models.IntegerField(max_length=3, null=True, default=0)
    place = models.CharField(max_length=50, null=True, blank=True)
    weight = models.IntegerField(max_length=4, null=True, default=0)
    hometown = models.CharField(max_length=50, null=True, blank=True)
    height = models.FloatField(max_length=4, null=True, default=0)
    occupation = models.CharField(max_length=50, null=True, blank=True)
    personality = models.CharField(max_length=50, null=True, blank=True)
    hobby = models.CharField(max_length=50, null=True, blank=True)
    weixin = models.CharField(max_length=50, null=True, blank=True)
    qq = models.IntegerField(max_length=50, null=True, default=0)
    email = models.EmailField(max_length=100, null=True, blank=True)
    mobile = models.CharField(max_length=50, default="00000000000")
    open_mobile = models.BooleanField(default=True, verbose_name=u"公开手机号码")

    date = models.DateTimeField(auto_now_add=True)
    fan = models.CharField(max_length=600,null=True, blank=True)
    intro = models.TextField(max_length=5000, null=True, blank=True)
    files = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.intro[0:10]

    class Meta:
        verbose_name = u"男神女神(投稿)"


class FansKLLMedia(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/fanskllmedia/%Y/%m/%d', max_length=500)
    belong = models.ForeignKey(FansKLL, null=True)

    def __unicode__(self):
        return str(self.id)

# 美食推荐(投稿)
class FansMSTJ(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fan = models.CharField(max_length=600, null=True, blank=True)
    intro = models.CharField(max_length=5000, null=True, blank=True)
    files = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.intro[0:10]

    class Meta:
        verbose_name = u"美食推荐(投稿)"


class FansMSTJMedia(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to='wechat/fansmstjmedia/%Y/%m/%d', max_length=500)
    belong = models.ForeignKey(FansMSTJ, null=True)

    def __unicode__(self):
        return str(self.id)


# 用户上传的摆饭秀材料
class FanShow(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    fan = models.CharField(max_length=600, null=True, blank=True)
    intro = models.TextField(max_length=5000)
    mobile = models.CharField(max_length=50, default="00000000000")
    files = models.CharField(max_length=100, null=True, blank=True)

    def __unicode__(self):
        return self.fan

    class Meta:
        verbose_name = u"摆饭秀(投稿)"


class FanShowMedia(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    media = models.FileField(upload_to="wechat/fanshowmedia/%Y/%m/%d", max_length=500)
    belong = models.ForeignKey(FanShow, null=True)

    def __unicode__(self):
        return str(self.id)


class AtypicalVisitorManager(models.Manager):
    def exist(self, openid, d):
        try:
            obj = self.get(open_id=openid, year=d.year, month=d.month, day=d.day)
            return True
        except:
            return False

# 发消息的粉丝，（用于判断是不是今天第一次发消息）
class AtypicalVisitor(models.Model):
    open_id = models.CharField(max_length=1000)
    year = models.IntegerField(max_length=4)
    month = models.IntegerField(max_length=2)
    day = models.IntegerField(max_length=2)

    objects = AtypicalVisitorManager()

    def __unicode__(self):
        return self.open_id


class IndexSliderManager(models.Manager):
    def new_slider(self, num):
        objs = self.filter(on=True).order_by("-date")[0:num]
        return objs

# mobile 首页的几张图片
class IndexSlider(models.Model):
    pic = models.ImageField(max_length=500, upload_to="mobile/index_slider/")
    intro = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    on = models.BooleanField(default=True)

    objects = IndexSliderManager()

    def __unicode__(self):
        return self.intro


class BFXManager(models.Manager):
    #  获取最新的num个摆饭秀
    def bfx(self, num):
        return self.all().order_by("-date")[0:num]

    # range: start - (end-1)
    def some_bfx(self, start, end):
        return self.all().order_by("-date")[start: end]

    # 摆饭秀数量
    def bfx_num(self):
        return self.all().count()

# 摆饭秀的article
class BFX(models.Model):
    title = models.CharField(max_length=200)
    intro = models.TextField(max_length=200)
    pic = models.ImageField(upload_to="wechat/bfx/")
    url = models.URLField(max_length=1000)
    date = models.DateTimeField(auto_now_add=True)

    objects = BFXManager()

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = u"摆饭秀(发布)"


class TextAnswerManager(models.Manager):
    # 获取key对应的answer，无则返回None
    def answer(self, key):
        try:
            return self.get(keyword = key).answer
        except:
            return None

# 自动回复-文本答案
class TextAnswer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=50, unique=True) # 关键词不能重复
    answer = models.TextField(max_length=500)

    objects = TextAnswerManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = u"自动回复(文本)"


class NewsAnswerManager(models.Manager):
    # 获取key对应的article，没有则返回None
    def answer(self, key):
        try:
            obj = self.get(keyword = key)
            article = {
                u"title": obj.title,
                u"description": obj.intro,
                u"pic_url": HOST_NAME + obj.img.url,
                u"url": obj.url
            }
            return [article]
        except:
            return None


# 自动回复-图文答案
class NewsAnswer(models.Model):
    date = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    intro = models.TextField(max_length=500)
    img = models.ImageField(upload_to="wechat/answer/%Y/%m/")
    url = models.URLField(max_length=1000)

    objects = NewsAnswerManager()

    def __unicode__(self):
        return self.keyword

    class Meta:
        verbose_name = u"自动回复(图文)"


class DDBBKllManager(models.Manager):
    # type 只能是xs, gn，即先生、姑娘
    def kll(self, tp, num):
        objs = self.filter(type=tp).order_by("-date")[0:num]
        return objs

    def some_kll(self, tp, start, end):
        return self.filter(type=tp).order_by("-date")[start:end]

    def kll_num(self, tp):
        return self.filter(type=tp).count()


# 滴滴叭叭的-括拉拉档案发布
class DDBBKll(models.Model):
    t = (
        (u"xs", u"孤单先森"),
        (u"gn", u"独身菇凉")
    )
    date = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, verbose_name=u"标题")
    type = models.CharField(max_length=20, verbose_name=u"类型", choices=t)
    intro = models.TextField(max_length=500, verbose_name=u"简介")
    img = models.ImageField(upload_to="wechat/ddbb/kll/%Y/%m/", verbose_name=u"封面图片")
    url = models.URLField(max_length=1000, verbose_name=u"详情页面链接")

    objects = DDBBKllManager()

    class Meta:
        verbose_name = u"滴滴叭叭-括拉拉档案"

    def __unicode__(self):
        return self.title
