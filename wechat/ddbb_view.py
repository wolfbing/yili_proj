
# -*- coding: utf-8 -*-

__author__ = 'bingliu'


from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
import views
import string
import hashlib
from wechat.models import BoysAndGirls, Voice
from django.core.urlresolvers import reverse

## const variant
# menu key
MR = "MR"
MRS = "MRS"
FANSHOW = "FANSHOW"

# request xml中的key
MSG_TYPE = "MsgType"
EVENT = "Event"
EVENT_KEY = "EventKey"

# event type
CLICK_EVENT = "CLICK"
SUBSCRIBE_EVENT = "subscribe"


# msg type
TEXT_MSG = "text"
EVENT_MSG = "event"

# const variaty
BOYS_AND_GIRLS_NUM = 5
FANSHOW_NUM = 5

# answer text
welcome_text = u"Hello~亲爱的早饭，感谢您关注滴滴叭叭早上好，这里每天都会为大家发布各种有趣资讯，" \
               u"快来和我们一起互动吧！么么哒~~/呲牙"
common_res_text = u"Hello~亲爱的早饭，感谢您关注滴滴叭叭早上好，这里每天都会为大家发布各种有趣资讯，" \
               u"快来和我们一起互动吧！么么哒~~/呲牙"


def main(request):
    req_data = views.parse_msg(request.body)
    if req_data[MSG_TYPE] == TEXT_MSG:
        return views.text_msg(req_data, common_res_text)
    elif req_data[MSG_TYPE] == EVENT_MSG:
        if req_data[EVENT] == SUBSCRIBE_EVENT:
            return views.text_msg(req_data, welcome_text)
        elif req_data[EVENT] == CLICK_EVENT:
            if req_data[EVENT_KEY] == MR:
                articles = get_ns()
                return views.news_msg(req_data, articles)
            elif req_data[EVENT_KEY] == MRS:
                articles = get_nvs()
                return views.news_msg(req_data, articles)
            elif req_data[EVENT_KEY] == FANSHOW:
                articles = get_bfx()
                return views.news_msg(req_data, articles)
            else:
                return HttpResponse("error")
        else:
            return HttpResponse('error')

    else:
        return HttpResponse("error")


# 接入微信服务器
def connect_to_wechat_server(request):
    signature = request.GET['signature']
    ts = request.GET['timestamp']
    nonce = request.GET['nonce']
    echo_str = request.GET['echostr']
    token = 'weixinddbb'
    arr = [token, ts, nonce]
    arr.sort()
    tmp_str = string.join(arr, '')
    sha1_obj = hashlib.sha1(tmp_str)
    sha1_str = sha1_obj.hexdigest()
    if sha1_str == signature:
        return HttpResponse(echo_str)
    else:
        return HttpResponse('')


#### get data
# 男神
def get_ns():
    objs = BoysAndGirls.objects.ns(BOYS_AND_GIRLS_NUM)
    nsl = []
    for obj in objs:
        ns = {}
        ns['title'] = obj.title
        ns['description'] = obj.intro
        ns['pic_url'] = views.HOST_NAME + obj.photo.url
        ns['url'] = obj.url
        nsl.append(ns)
    more = {
        "title": u"关注线下平台‘有些’，发现更多孤单先森！！",
        "description": u"关注线下平台‘有些’，发现更多孤单先森！",
        "pic_url": views.STATIC_BASE_URL + "images/logo.png",
        "url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201658145&idx=1&"
               u"sn=694355939e215435794798bb6dfd755a#rd"
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
        nvs['pic_url'] = views.HOST_NAME + obj.photo.url
        nvs['url'] = obj.url
        nvsl.append(nvs)
    more = {
        "title": u"关注线下平台‘有些’，了解更多独身菇凉",
        "description": u"关注线下平台‘有些’，了解更多独身菇凉",
        "pic_url": views.STATIC_BASE_URL + "images/logo.png",
        "url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201658145&idx=1&"
               u"sn=694355939e215435794798bb6dfd755a#rd"
    }
    nvsl.append(more)
    return nvsl


# 摆饭秀
def get_bfx():
    objs = Voice.objects.bfx(FANSHOW_NUM)
    bfl = []
    for obj in objs:
        bf = {}
        bf['title'] = obj.title
        bf['description'] = obj.intro
        bf['pic_url'] = views.HOST_NAME + obj.pic.url
        if obj.url==u'':
            bf['url'] = views.HOST_NAME + reverse("wechat.views.play_audio") + "?audio=" + str(obj.id)
        else:
            bf['url'] = obj.url
        bfl.append(bf)
    more = {
        "title": u"关注线下平台‘有些’，欣赏更多精彩的摆饭秀！！",
        "description": u"关注线下平台‘有些’，欣赏更多精彩的摆饭秀！！",
        "pic_url": views.STATIC_BASE_URL + "images/logo.png",
        "url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201658145&idx=1&"
               u"sn=694355939e215435794798bb6dfd755a#rd"
    }
    bfl.append(more)
    return bfl


