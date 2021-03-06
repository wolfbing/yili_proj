
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.core.urlresolvers import reverse
from django.core.files import File

import string
import hashlib
import time
from xml.etree import ElementTree as ET
import logging
from answer import ANSWER, NEWS_ANSWER
import urllib2, urllib
import setting as wsetting
from datetime import datetime, timedelta
import json
from ddbb_answer import news_answer as db_news_answer
from yili_proj.local_settings import HOST_NAME

from models import BoysAndGirls, FineFood, Voice, \
    FansKLL, FansKLLMedia, FansMSTJ, FansMSTJMedia, \
    FanShow, FanShowMedia, AtypicalVisitor, \
    TextAnswer, NewsAnswer
from models import BFX as BFShow  #  程序中已经出现BFX变量，（表命名需要注意了）

# Create your views here.

# keys of menu
NS = 'NS'
NVS = 'NVS'
BZND = 'BZND'
BZNVD = 'BZNVD'
ST = 'ST'
BX = 'BX'
PMS = 'PMS' # 泡美食
JDHG = 'JDHG'
BSBS = 'BSBS'
BFX = 'BFX'

# media type
MEDIA_MSTJ = 'MSTJ'
MEDIA_KLL = 'KLL'

# MsgType
TEXT_MSG = "text"
EVENT_MSG = "event"
IMAGE_MSG = "image"
VOICE_MSG = "voice"

CLICK_EVENT = "CLICK"
SUBSCRIBE_EVENT = "subscribe"
UNSUBSCRIBE_EVENT = "unsubscribe"
Content = "Content"
FromUserName = "FromUserName"
MediaId = "MediaId"
PicUrl = "PicUrl"

# msg judget
MSG_TYPE = "MsgType"
EVENT = "Event"
EVENT_KEY = "EventKey"


# logger
logger = logging.getLogger('wechat')
logger2 = logging.getLogger('django')

# News num
BOYS_AND_GIRLS_NUM = 5
FINE_FOOD_NUM = 5
VOICE_NUM = 5
BFX_NUM = 5

# detail num
MORE_BOYS_AND_GIRLS_NUM = 100
MORE_FINE_FOOD_NUM = 100
MORE_VOICE_NUM = 10

# static text msg
WELCOME_MSG = u"欢迎关注 aiyouxie ！"
BYE_MSG = u'对您有些留恋，期待与您再会！'
HELP_MSG = u'您可以回复...'

# base url
#MEDIA_BASE_URL = 'http://121.199.32.77'
#STATIC_BASE_URL = 'http://121.199.32.77'
STATIC_BASE_URL = HOST_NAME + "/static/"
MEDIA_BASE_URL = HOST_NAME + "/media/"



ADMIN_EMAIL = "weixin_youxie01@126.com"



def test(request):
    res_data = {
        "static_url": STATIC_BASE_URL,
        "vedio_url": "http://121.199.32.77/media/wechat/staticmedia/2014/12/t00157jabmq.mp4",
        "audio_url": "http://121.199.32.77/media/wechat/staticmedia/2014/12/song.mp3"
    }
    return render_to_response("test.html",res_data)


# wechat 请求入口
def main(request):
    try:
        req_data = parse_msg(request.body)
        return text_msg(req_data, u"平台升级中... 敬请谅解！")
        # if req_data[MSG_TYPE] == TEXT_MSG:
        #     content = req_data[Content].strip()
        #     now = datetime.now() + timedelta(hours=8)
        #     if is_kll(content):
        #         return save_kll_intro(req_data)
        #     elif is_mstj(content):
        #         return save_recommend_food_intro(req_data)
        #     elif TextAnswer.objects.answer(content)!=None:
        #         return text_msg(req_data, TextAnswer.objects.answer(content))
        #     elif NewsAnswer.objects.answer(content) != None:
        #         return  news_msg(req_data, NewsAnswer.objects.answer(content))
        #     elif db_news_answer.get(content) != None:
        #         return news_msg(req_data, db_news_answer.get(content))
        #     elif AtypicalVisitor.objects.exist(req_data[FromUserName], now):
        #         return HttpResponse("")
        #     else:
        #         obj = AtypicalVisitor(open_id=req_data[FromUserName], year=now.year, month=now.month, day=now.day)
        #         obj.save()
        #         return text_msg(req_data, ANSWER.get("help"))
        # elif req_data[MSG_TYPE] == IMAGE_MSG:
        #     return text_msg(req_data, u'图片发送成功！.')
        # elif req_data[MSG_TYPE] == VOICE_MSG:
        #     return text_msg(req_data, u'音频发送成功！')
        # elif req_data[MSG_TYPE] == EVENT_MSG:
        #     ###  订阅与取消订阅
        #     if req_data[EVENT] == SUBSCRIBE_EVENT:
        #         return text_msg(req_data, TextAnswer.objects.answer(u'welcome'))
        #     elif req_data[EVENT] == UNSUBSCRIBE_EVENT:
        #         return text_msg(req_data, BYE_MSG)
        #     ###  菜单点击事件
        #     elif req_data[EVENT] == CLICK_EVENT:
        #         ###  有些朋友
        #         if req_data[EVENT_KEY] == NS:
        #             articles = get_ns()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == NVS:
        #             articles = get_nvs()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == BZND:
        #             articles = get_bznd()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == BZNVD:
        #             articles = get_bznvd()
        #             return news_msg(req_data, articles)
        #         ###  有些美食
        #         elif req_data[EVENT_KEY] == ST:
        #             articles = get_st()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == BX:
        #             articles = get_bx()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == PMS:
        #             articles = get_pms()
        #             return news_msg(req_data, articles)
        #         ###  有些声音
        #         elif req_data[EVENT_KEY] == JDHG:
        #             articles = get_jdhg()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == BSBS:
        #             articles = get_bsbs()
        #             return news_msg(req_data, articles)
        #         elif req_data[EVENT_KEY] == BFX:
        #             articles = get_bfx()
        #             return news_msg(req_data, articles)
        #         else:
        #             return text_msg(req_data, HELP_MSG)
        #     else:
        #         return text_msg(req_data, HELP_MSG)
        # else:
        #     now = datetime.now() + timedelta(hours=8)
        #     if AtypicalVisitor.objects.exist(req_data[FromUserName], now):
        #         return HttpResponse("")
        #     else:
        #         obj = AtypicalVisitor(open_id=req_data[FromUserName], year=now.year, month=now.month, day=now.day)
        #         obj.save()
        #         return text_msg(req_data, HELP_MSG)
    except Exception, e:
        logger.debug(e)
        print e
        return HttpResponse("error occur!")

#
def all_ns(request):
    pics = some_ns(1)
    res_data = {"pics": pics, "static_url": STATIC_BASE_URL}
    return render_to_response("image_flow.html", res_data)


def more_ns(request):
    # page_num = int(request.GET['page'])
    # pics = some_ns(page_num)
    # res_data = {"pics": pics}
    # t = get_template("image_item.htm")
    # html = t.render(Context(res_data))
    # print html
    html = '''
    <div class="box"><a href=""><img src="http://127.0.0.1:8000/media/boysandgirls/2014/11/%E5%A4%B4%E5%83%8F.jpg"></a></div>

    <div class="box"><a href="http://www.baidu.com/"><img src="http://127.0.0.1:8000/media/wechat/boysandgirls/2014/11/ns1.jpg"></a></div>

    <div class="box"><a href="http://www.baidu.com/"><img src="http://127.0.0.1:8000/media/wechat/boysandgirls/2014/11/ns2.jpg"></a></div>
    '''
    #return render_to_response("image_item.htm", res_data)
    return HttpResponse(html)


def all_nvs(request):
    pics = some_nvs(1)
    res_data = {"pics": pics, "static_url": STATIC_BASE_URL}
    return render_to_response("image_flow.html", res_data)


def all_food(request, ft=BX):
    pics = some_food(1, ft)
    res_data = {"pics": pics, "static_url": STATIC_BASE_URL}
    return render_to_response("image_flow.html", res_data)


def all_voice(request, vt=JDHG):
    vs = some_voice(1, vt)
    cn = ''
    if vt is JDHG:
        cn = u"经典回顾"
    elif vt is BSBS:
        cn = u"不三不四"
    else:
        cn = u"摆饭秀"
    res_data = {"vs": vs, "column_name": cn, "static_url": STATIC_BASE_URL}
    return render_to_response("voice_list.html", res_data)


def play_audio(request):
    id_str = request.GET['audio']
    id = int(id_str)
    v = get_voice(id)
    if v is None:
        return render_to_response(u'音频不存在')
    else:
        res_data = {
            'audio_url': v['url'],
            'audio_title': v['title']
        }
        return render_to_response('play_voice.html', res_data)


def attend_kulala(request):
    if request.method == "GET":
        res_data = {
            "static_url": STATIC_BASE_URL,
            'action_url': reverse(attend_kulala)
        }
        return render_to_response('signup_kuolala.html', res_data)
    elif request.method == 'POST':
        res_data = {}
        try:
            try:
                age = int(request.POST['age'])
            except:
                age = None
            place = request.POST['place']
            try:
                weight = int(request.POST['weight'])
            except:
                weight = None
            hometown = request.POST['hometown']
            try:
                height = float(request.POST['height'])
            except:
                height = None
            occupation = request.POST['occupation']
            personality = request.POST['personality']
            hobby = request.POST['hobby']
            weixin = request.POST['weixin']
            try:
                qq = int(request.POST['qq'])
            except:
                qq = None
            email = request.POST['email']
            mobile = int(request.POST['mobile'])
            open_mobile = (request.POST.get('openmobile') == u'open')
            introduction = request.POST['intro']
            file_ids = []
            files = []
            for f in request.FILES:
                uf = request.FILES[f]
                uf.name = unicode(mobile) + uf.name
                item = FansKLLMedia(media=uf)
                item.save()
                file_ids.append(str(item.id))
                files.append(item)
            kll = FansKLL(intro=introduction, files=','.join(file_ids),
                          age=age, place=place, weight=weight, hometown=hometown, height=height,
                          occupation=occupation, personality=personality, hobby=hobby, weixin=weixin,
                          qq=qq, email=email, mobile=mobile, open_mobile=open_mobile, fan=str(mobile)
                          )
            kll.save()
            for i in files:
                i.belong=kll
                i.save()
            res_data = {
                'result_title': u'提交成功',
                'result': u'您的括拉拉档案提交成功！'
            }
        except Exception, e:
            logger.debug(e)
            print e
            res_data = {
                'result_title': u'提交失败',
                'result': u'您的括拉拉档案提交失败了- -#, '
                          u'检查下您的输入吧，您也可以向我们提交个人档案或者反馈意见：' + ADMIN_EMAIL
            }

        return render_to_response('post_result.html', res_data)


def recommend_food(request):
    if request.method == 'GET':
        res_data = {
            'static_url': STATIC_BASE_URL,
            'action_url': reverse(recommend_food)
        }
        return render_to_response('recommend_food.html', res_data)
    elif request.method == 'POST':
        res_data = {}
        try:
            introduction = request.POST['intro']
            file_ids = []
            files = []
            tmp = datetime.now().strftime("%Y%m%d%H%M%S")
            for f in request.FILES:
                uf = request.FILES[f]
                uf.name = tmp + uf.name
                item = FansMSTJMedia(media=uf)
                item.save()
                file_ids.append(str(item.id))
                files.append(item)
            food = FansMSTJ(intro=introduction, files=','.join(file_ids), fan=tmp)
            food.save()
            for i in files:
                i.belong = food
                i.save()

            res_data = {
                'result_title': u'推荐成功',
                'result': u'推荐成功！感谢您的推荐！'
            }

        except Exception,e:
            logger.debug(e)
            res_data = {
                'result_title': u'推荐失败',
                'result': u'推荐失败了 - -#, 检查下您的输入吧~ 您也可以通过邮箱向我们推荐美食或者反馈意见: '+ADMIN_EMAIL
            }
        return render_to_response('post_result.html', res_data)


def fan_show(request):
    try:
        if request.method == "GET":
            res_data = {
                "static_url": STATIC_BASE_URL,
                "action_url": reverse(fan_show)
            }
            return render_to_response("fan_show.html", res_data)
        else:
            introduction = request.POST['intro']
            mobile_phone = request.POST['mobile']
            file_ids = []
            files = []
            tmp = datetime.now().strftime("%Y%m%d%H%M%S")
            for f in request.FILES:
                uf = request.FILES[f]
                uf.name = tmp + uf.name
                item = FanShowMedia(media=uf)
                item.save()
                file_ids.append(str(item.id))
                files.append(item)
            show = FanShow(intro=introduction, files=','.join(file_ids), fan=mobile_phone, mobile=mobile_phone)
            show.save()
            for i in files:
                i.belong = show
                i.save()
            res_data = {
                'result_title': u'提交成功',
                'result': u'提交成功！欢迎再次来秀！'
            }
            return render_to_response('post_result.html', res_data)
    except Exception,e:
        print e
        logger.debug(e)
        res_data = {
            'result_title': u'提交失败',
            'result': u"提交失败 - -! ,重新试试吧~, 或者向我们反馈一下吧~"
        }
        return render_to_response('post_result.html', res_data)



def view_kll_post(request):
    res_data = {
        "static_url": STATIC_BASE_URL
    }
    objs = FansKLL.objects.all().order_by("-date")
    klls = []
    for obj in objs:
        kll = {
            "detail_url": reverse(view_kll_detail, kwargs={"id":obj.id}),
            "name": obj.fan,
            "intro": obj.intro[0:30] + u"...",
            "date": obj.date.strftime("%Y-%m-%d %H:%M")
        }
        klls.append(kll)
    res_data["klls"] = klls
    return render_to_response("kll_list.html", res_data)


def view_kll_detail(request, id):
    kll = FansKLL.objects.get(id=id)
    res_data = {
        "static_url": STATIC_BASE_URL,
        "age": kll.age,
        "place": kll.place,
        "hometown": kll.hometown,
        "weight": kll.weight,
        "height": kll.height,
        "occupation": kll.occupation,
        "personality": kll.personality,
        "hobby": kll.hobby,
        "weixin": kll.weixin,
        "qq": kll.qq,
        "mobile": kll.mobile,
        "intro": kll.intro,
        "open_mobile": (kll.open_mobile and u"是") or u"否",
        "title": kll.fan,
        "date": kll.date.strftime("%Y-%m-%d %H:%M")
    }
    f_ids = kll.files.split(u",")
    files = []
    for id in f_ids:
        file = FansKLLMedia.objects.get(id=int(id))
        files.append(file)
    imgs = []
    other_medias = []
    for f in files:
        s = f.media.url
        suffix = [u".png", u".jpg", u".gif", u".bmp", u".jpeg"]
        is_img = False
        for su in suffix:
            if s.endswith(su) or s.endswith(su.upper()):
                is_img = True
                imgs.append(s)
                break
        if not is_img:
            other_medias.append(s)
    res_data["imgs"] = imgs
    res_data['files'] = other_medias
    return render_to_response("kll_detail.html", res_data)


def view_bfx_post(request):
    res_data = {
        "static_url": STATIC_BASE_URL
    }
    objs = FanShow.objects.all().order_by("-date")
    fans = []
    for obj in objs:
        fan = {
            "name": obj.fan,
            "intro": obj.intro[0:30]+u"...",
            "date": obj.date.strftime("%Y-%m-%d %H:%M"),
            "detail_url": reverse(view_bfx_detail, kwargs={"id": obj.id})
        }
        fans.append(fan)
    res_data["fans"] = fans
    return render_to_response("fanshow_list.html", res_data)


def view_bfx_detail(request, id):
    res_data = {
        "static_url": STATIC_BASE_URL
    }
    obj = FanShow.objects.get(id=id)
    fan = {
        "title": obj.fan,
        "date": obj.date.strftime("%Y-%m-%d %H:%M"),
        "intro": obj.intro
    }
    res_data.update(fan)
    f_ids = obj.files.split(u",")
    files = []
    for id in f_ids:
        file = FanShowMedia.objects.get(id=int(id))
        files.append(file)
    imgs = []
    other_medias = []
    for f in files:
        s = f.media.url
        suffix = [u".png", u".jpg", u".gif", u".bmp", u".jpeg"]
        is_img = False
        for su in suffix:
            if s.endswith(su) or s.endswith(su.upper()):
                is_img = True
                imgs.append(s)
                break
        if not is_img:
            other_medias.append(s)
    res_data["imgs"] = imgs
    res_data['files'] = other_medias

    return render_to_response("fanshow_detail.html", res_data)


# 接入微信服务器
def connect_to_wechat_server(request):
    signature = request.GET['signature']
    ts = request.GET['timestamp']
    nonce = request.GET['nonce']
    echo_str = request.GET['echostr']
    token = 'weixinsome'
    arr = [token, ts, nonce]
    arr.sort()
    tmp_str = string.join(arr, '')
    sha1_obj = hashlib.sha1(tmp_str)
    sha1_str = sha1_obj.hexdigest()
    if sha1_str == signature:
        return HttpResponse(echo_str)
    else:
        return HttpResponse('')


def text_msg(request_data, content):
    create_time = int(time.time())
    res_data = {
        "to_user": request_data['FromUserName'],
        "from_user": request_data['ToUserName'],
        "create_time": create_time,
        "content": content
    }
    return render_to_response('text_msg.xml', res_data)


def parse_msg(msg):
    dict = {}
    root = ET.fromstring(msg)
    child_list = root.getchildren()
    for child in child_list:
        dict[child.tag] = child.text
    return dict


def news_msg(req_data, articles):
    create_time = int(time.time())
    res_data = {
        "to_user": req_data['FromUserName'],
        "from_user": req_data['ToUserName'],
        "create_time": create_time,
        "article_count": len(articles),
        "articles": articles
    }
    return render_to_response('news_msg.xml', res_data)


#### get data
# 男神
def get_ns():
    objs = BoysAndGirls.objects.ns(BOYS_AND_GIRLS_NUM)
    nsl = []
    for obj in objs:
        ns = {}
        ns['title'] = obj.title
        ns['description'] = obj.intro
        ns['pic_url'] = HOST_NAME + obj.photo.url
        ns['url'] = obj.url
        nsl.append(ns)
    more = {
        "title": u"点击欣赏更多男神！！",
        "description": u"点击欣赏更多男神！！",
        "pic_url": STATIC_BASE_URL + "images/ns.jpg",
        "url": HOST_NAME + reverse("kll_list", kwargs={"page":1, "type":"ns"})
    }
    nsl.append(more)
    return nsl


# 男神
def get_nvs():
    objs = BoysAndGirls.objects.nvs(BOYS_AND_GIRLS_NUM)
    nvsl = []
    for obj in objs:
        nvs = {}
        nvs['title'] = obj.title
        nvs['description'] = obj.intro
        nvs['pic_url'] = HOST_NAME + obj.photo.url
        nvs['url'] = obj.url
        nvsl.append(nvs)
    more = {
        "title": u"点击欣赏更多女神！！",
        "description": u"点击欣赏更多女神！！",
        "pic_url": STATIC_BASE_URL + "images/nvs.jpg",
        "url": HOST_NAME + reverse("kll_list", kwargs={"type":"nvs", "page":1})
    }
    nvsl.append(more)
    return nvsl


# 本周男帝
def get_bznd():
    obj = BoysAndGirls.objects.new_nd()
    ndl = []
    nd = {}
    if obj is not None:
        nd['title'] = obj.title
        nd['description'] = obj.intro
        nd['pic_url'] = HOST_NAME + obj.photo.url
        nd['url'] = obj.url
    else:
        nd['title'] = u"男帝还没产生呢~"
        nd['description'] = ""
        nd['pic_url'] = ""
        nd['url'] = ""
    ndl.append(nd)
    return ndl


# 本周女帝
def get_bznvd():
    obj = BoysAndGirls.objects.new_nvd()
    ndl = []
    nd = {}
    if obj is not None:
        nd['title'] = obj.title
        nd['description'] = obj.intro
        nd['pic_url'] = HOST_NAME + obj.photo.url
        nd['url'] = obj.url
    else:
        nd['title'] = u"女帝还没产生呢~"
        nd['description'] = ""
        nd['pic_url'] = ""
        nd['url'] = ""
    ndl.append(nd)
    return ndl


# 食堂
def get_st():
    objs = FineFood.objects.st(FINE_FOOD_NUM)
    stl = []
    for obj in objs:
        st = {}
        st['title'] = obj.title
        st['description'] = obj.intro
        st['pic_url'] = HOST_NAME + obj.photo.url
        st['url'] = obj.url
        stl.append(st)
    more = {
        "title": u"点击查看更多美食小吃！！",
        "description": u"点击查看更多美食小吃！！",
        "pic_url": STATIC_BASE_URL + "images/st.jpg",
        "url": HOST_NAME + reverse("wechat.views.all_food", kwargs={"ft": ST})
    }
    stl.append(more)
    return stl


# 包厢
def get_bx():
    objs = FineFood.objects.bx(FINE_FOOD_NUM)
    bxl = []
    for obj in objs:
        bx = {}
        bx['title'] = obj.title
        bx['description'] = obj.intro
        bx['pic_url'] = HOST_NAME + obj.photo.url
        bx['url'] = obj.url
        bxl.append(bx)
    more = {
        "title": u"点击查看更多丰盛大餐！！",
        "description": u"点击查看更多丰盛大餐！！",
        "pic_url": STATIC_BASE_URL + "images/bx.jpg",
        "url": HOST_NAME + reverse("wechat.views.all_food", kwargs={"ft": BX})
    }
    bxl.append(more)
    return bxl

def get_pms():
    objs = FineFood.objects.pms(FINE_FOOD_NUM)
    msl = []
    for obj in objs:
        ms = {}
        ms['title'] = obj.title
        ms['description'] = obj.intro
        ms['pic_url'] = HOST_NAME + obj.photo.url
        ms['url'] = obj.url
        msl.append(ms)
    more = {
        "title": u"点击查看更多丰盛大餐！！",
        "description": u"点击查看更多丰盛大餐！！",
        "pic_url": STATIC_BASE_URL + "images/bx.jpg",
        "url": HOST_NAME + reverse("finefoodlist", kwargs={"page":1})
    }
    msl.append(more)
    return msl


# 经典回顾
def get_jdhg():
    objs = Voice.objects.jdhg(VOICE_NUM)
    jdl = []
    for obj in objs:
        jd = {}
        jd['title'] = obj.title
        jd['description'] = obj.intro
        jd['pic_url'] = HOST_NAME + obj.pic.url
        if obj.url==u'':
            jd['url'] = HOST_NAME + reverse("mobile_audioplayer", kwargs={"id":obj.id})
        else:
            jd['url'] = obj.url
        jdl.append(jd)
    more = {
        "title": u"点击查看更多经典回顾！！",
        "description": u"点击查看更多经典回顾！！",
        "pic_url": STATIC_BASE_URL + "images/voice.jpg",
        "url": HOST_NAME + reverse("voicelist", kwargs={"page":1, "type":"jdhg"})
    }
    jdl.append(more)
    return jdl


# 不三不四
def get_bsbs():
    objs = Voice.objects.bsbs(VOICE_NUM)
    bsl = []
    for obj in objs:
        bs = {}
        bs['title'] = obj.title
        bs['description'] = obj.intro
        bs['pic_url'] = HOST_NAME + obj.pic.url
        if obj.url==u'':
            bs['url'] = HOST_NAME + reverse("mobile_audioplayer", kwargs={"id":obj.id})
        else:
            bs['url'] = obj.url
        bsl.append(bs)
    more = {
        "title": u"点击查看更多不三不四！！",
        "description": u"点击查看更多不三不四！！",
        "pic_url": STATIC_BASE_URL + "images/voice.jpg",
        "url":  HOST_NAME + reverse("voicelist", kwargs={"type":"bsbs", "page":1})
    }
    bsl.append(more)
    return bsl


# 用于自动回复的摆饭秀article－list
def get_bfx():
    objs = BFShow.objects.bfx(BFX_NUM)
    bfl = []
    for obj in objs:
        bf = {}
        bf['title'] = obj.title
        bf['description'] = obj.intro
        bf['pic_url'] = HOST_NAME + obj.pic.url
        bf['url'] = obj.url
        bfl.append(bf)
    more = {
        "title": u"点击查看更多摆饭秀！！",
        "description": u"点击查看更多摆饭秀！！",
        "pic_url": STATIC_BASE_URL + "images/voice.jpg",
        "url": HOST_NAME + reverse("bfxlist", kwargs={"page":1})
    }
    bfl.append(more)
    return bfl

# 第page_num页的男神
def some_ns(page_num):
    start = (page_num-1) * MORE_BOYS_AND_GIRLS_NUM
    end = page_num * MORE_BOYS_AND_GIRLS_NUM # 不包括第end个
    objs = BoysAndGirls.objects.some_ns(start, end)
    pics = []
    for obj in objs:
        pic = {}
        pic['url'] = obj.url
        pic['src'] = HOST_NAME + obj.photo.url
        pics.append(pic)
    return pics


def some_nvs(page_num):
    start = (page_num-1) * MORE_BOYS_AND_GIRLS_NUM
    end = page_num * MORE_BOYS_AND_GIRLS_NUM
    objs = BoysAndGirls.objects.some_nvs(start, end)
    pics = []
    for obj in objs:
        pic = {}
        pic['url'] = obj.url
        pic['src'] = HOST_NAME + obj.photo.url
        pics.append(pic)
    return pics


def some_food(page_num, type):
    start = (page_num-1) * MORE_FINE_FOOD_NUM
    end = page_num * MORE_FINE_FOOD_NUM
    objs = []
    if type is BX:
        objs = FineFood.objects.some_bx(start, end)

    elif type is ST:
        objs = FineFood.objects.some_st(start, end)
    else:
        objs = FineFood.objects.some_pms(start, end)
    pics = []
    for obj in objs:
        pic = {}
        pic['url'] = obj.url
        pic['src'] = HOST_NAME + obj.photo.url
        pics.append(pic)
    return pics


def some_voice(page_num, type):
    start = (page_num-1) * MORE_VOICE_NUM
    end = page_num * MORE_VOICE_NUM
    objs = []
    if type is JDHG:
        objs = Voice.objects.some_jdhg(start, end)
    elif type is BSBS:
        objs = Voice.objects.some_bsbs(start, end)
    else:
        objs = Voice.objects.some_bfx(start, end)
    vs = []
    for obj in objs:
        v = {}
        if obj.url==u'' or obj.url==None:
            v['url'] = HOST_NAME + reverse("wechat.views.play_audio") + "?audio=" + str(obj.id)
        else:
            v['url'] = obj.url
        v['title'] = obj.title
        vs.append(v)
    return vs


def get_voice(id):
    obj = Voice.objects.get_voice_by_id(id)
    if obj is None:
        return None
    else:
        v = {}
        if obj.url==u'':
            v['url'] = HOST_NAME + obj.audio.url
        else:
            v['url'] = obj.url
        v['title'] = obj.title
        return v

def is_kll(content):
    return content.startswith(u'#括拉拉档案#')

def is_mstj(content):
    return content.startswith(u'#美食推荐#')


def save_kll_intro(req_data):
    content = req_data[Content]
    openid = req_data[FromUserName]
    utcnow = datetime.utcnow()
    now = datetime.now()
    klls = FansKLL.objects.filter(fan=openid).order_by("-date")
    if len(klls)>0:
        kll = klls[0]
        d = kll.date + timedelta(hours=8)
        if now.year==d.year and now.month==d.month and now.day==d.day:
            kll.intro = kll.intro + "\n" + content[7:]
            kll.save()
        else:
            kll2 = FansKLL(fan=openid, intro = content[7:])
            kll2.save()
    else:
        kll = FansKLL(fan=openid, intro = content[7:])
        kll.save()
    return text_msg(req_data, u"括拉拉档案文字介绍发送成功! 继续发送您的靓照或者语音吧~")


def judget_media_type(req_data):
    try:
        open_id = req_data[FromUserName]
        now = datetime.now()
        ms = FansMSTJ.objects.filter(fan=open_id).order_by('-date')
        kll = FansKLL.objects.filter(fan=open_id).order_by('-date')
        if len(ms) and len(kll):
            mst = ms[0].date + timedelta(hours=8)
            kllt = kll[0].date + timedelta(hours=8)
            if (mst.year==now.year and mst.month==now.month and mst.day==now.day) \
                and (kllt.year==now.year and kllt.month==now.month and kllt.day==now.day):
                if mst>kllt:
                    return MEDIA_MSTJ
                else:
                    return MEDIA_KLL
            elif (mst.year==now.year and mst.month==now.month and mst.day==now.day):
                return MEDIA_MSTJ
            elif (kllt.year==now.year and kllt.month==now.month and kllt.day==now.day):
                return MEDIA_KLL
            else:
                return None
        elif len(ms):
            mst = ms[0].date + timedelta(hours=8)
            if (mst.year==now.year and mst.month==now.month and mst.day==now.day):
                return MEDIA_MSTJ
            else:
                return None
        elif len(kll):
            kllt = kll[0].date + timedelta(hours=8)
            if (kllt.year==now.year and kllt.month==now.month and kllt.day==now.day):
                return MEDIA_KLL
            else:
                return None
        else:
            return None
    except Exception, e:
        logger.debug(e)
        return None



def save_media(req_data, type, success_info=u"发送成功！"):
    try:
        logger2.info("pos1")
        media_id = req_data[MediaId]
        open_id = req_data[FromUserName]
        now = datetime.now()
        delta = now - wsetting.LastTokenTime
        logger2.info('pos2')
        if delta>=wsetting.TokenExpire:
            logger2.info('pos2-1')
            res_str = urllib2.urlopen(wsetting.GetAccessTokenUrl).read()
            logger2.info('pos2-2')
            json_res_data = json.loads(res_str)
            logger2.info('pos2-3')
            if json_res_data.get('access_token') is None:
                return HttpResponse(text_msg(req_data), u'微信服务器请求出错')
            else:
                wsetting.LastTokenTime = datetime.now()
                wsetting.AccessToken = json_res_data['access_token']
                wsetting.TokenExpire = timedelta(seconds=int(json_res_data['expires_in']))
        logger2.info('pos3')
        down_url = wsetting.DownloadMediaUrl % (wsetting.AccessToken, media_id)
        logger2.info('pos3-1')
        res = urllib2.urlopen(down_url)
        f = res.read()
        logger2.info(down_url)
        uf = File(f)
        uf.name = open_id
        logger2.info('pos3-2')
        media = None
        if type == MEDIA_KLL:
            media = FansKLLMedia(media=uf)
        else:
            media == FansMSTJMedia(media=uf)
        media.save()
        logger2.info('pos4')
        tmp_entries = None
        now = datetime.now()
        if type=="KLL":
            tmp_entries = FansKLL.objects.filter(fan=open_id).order_by('-date')
        else:
            tmp_entries = FansMSTJ.objects.filter(fan=open_id).order_by('-date')
        entries = []
        for e in tmp_entries:
            en  = e + timedelta(hours=8)
            if en.year==now.year and en.month==now.month and en.day==now.day:
                entries.append(en)
        entry = None
        logger2.info('pos5')
        if len(entries)>0:
            entry = entries[0]
            fs = entry.files
            entry.files = fs+","+str(media.id)
            entry.save()
        else:
            if type==MEDIA_KLL:
                entry = FansKLL(files=str(media.id))
            else:
                entry = FansMSTJ(files=str(media.id))
            entry.save()
        logger2.info('pos6')
        media.belong = entry.id
        media.save()
        return text_msg(req_data, success_info)
    except Exception, e:
        logger.debug(e)
        return text_msg(req_data, str(e))


def save_recommend_food_intro(req_data):
    content = req_data[Content]
    openid = req_data[FromUserName]
    utcnow = datetime.utcnow()
    now = datetime.now()
    mstjs = FansMSTJ.objects.filter(fan=openid).order_by('-date')
    if len(mstjs)>0:
        ms = mstjs[0].date + timedelta(hours=8)
        if ms.year==now.year and ms.month==now.month and ms.day==now.day:
            ms.intro = ms.intro + "\n" + content[6:]
            ms.save()
        else:
            ms = FansMSTJ(fan=openid, intro = content[6:])
            ms.save()
    else:
        ms = FansMSTJ(fan=openid, intro = content[6:])
        ms.save()
    return text_msg(req_data, u"美食推荐文字介绍发送成功！")





