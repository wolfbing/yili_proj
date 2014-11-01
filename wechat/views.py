
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse

import string
import hashlib
import time
from xml.etree import ElementTree as ET
import logging

from models import BoysAndGirls, FineFood, Voice

# Create your views here.

# keys of menu
NS = 'NS'
NVS = 'NVS'
BZND = 'BZND'
BZNVD = 'BZNVD'
ST = 'ST'
BX = 'BX'
JDHG = 'JDHG'
BSBS = 'BSBS'
BFX = 'BFX'

# MsgType
TEXT_MSG = "text"
EVENT_MSG = "event"
CLICK_EVENT = "CLICK"
SUBSCRIBE_EVENT = "subscribe"
UNSUBSCRIBE_EVENT = "unsubscribe"

# msg judget
MSG_TYPE = "MsgType"
EVENT = "Event"
EVENT_KEY = "EventKey"


# logger
logger = logging.getLogger('wechat')

# News num
BOYS_AND_GIRLS_NUM = 5
FINE_FOOD_NUM = 5
VOICE_NUM = 5

# static text msg
WELCOME_MSG = u"欢迎关注 aiyouxie ！"
BYE_MSG = u'对您有些留恋，期待与您再会！'
HELP_MSG = u'您可以回复...'

# base url
MEDIA_BASE_URL = 'http://121.199.32.77'
STATIC_BASE_URL = 'http://121.199.32.77'

# wechat 请求入口
def main(request):
    try:
        req_data = parse_msg(request.body)
        if req_data[MSG_TYPE] == TEXT_MSG:
            return text_msg(req_data, HELP_MSG)
        elif req_data[MSG_TYPE] == EVENT_MSG:
            ###  订阅与取消订阅
            if req_data[EVENT] == SUBSCRIBE_EVENT:
                return text_msg(req_data, WELCOME_MSG)
            elif req_data[EVENT] == UNSUBSCRIBE_EVENT:
                return text_msg(req_data, BYE_MSG)
            ###  菜单点击事件
            elif req_data[EVENT] == CLICK_EVENT:
                ###  有些朋友
                if req_data[EVENT_KEY] == NS:
                    articles = get_ns()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == NVS:
                    articles = get_nvs()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == BZND:
                    articles = get_bznd()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == BZNVD:
                    articles = get_bznvd()
                    return news_msg(req_data, articles)
                ###  有些美食
                elif req_data[EVENT_KEY] == ST:
                    articles = get_st()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == BX:
                    articles = get_bx()
                    return news_msg(req_data, articles)
                ###  有些声音
                elif req_data[EVENT_KEY] == JDHG:
                    articles = get_jdhg()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == BSBS:
                    articles = get_bsbs()
                    return news_msg(req_data, articles)
                elif req_data[EVENT_KEY] == BFX:
                    articles = get_bfx()
                    return news_msg(req_data, articles)
                else:
                    return text_msg(req_data, HELP_MSG)
            else:
                return text_msg(req_data, HELP_MSG)
        else:
            return text_msg(req_data, HELP_MSG)
    except Exception, e:
        logger.debug(e)
        return HttpResponse("error occur!")


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
        ns['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        ns['url'] = obj.url
        nsl.append(ns)
    more = {
        "title": u"点击欣赏更多男神！！",
        "description": u"点击欣赏更多男神！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
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
        nvs['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        nvs['url'] = obj.url
        nvsl.append(nvs)
    more = {
        "title": u"点击欣赏更多女神！！",
        "description": u"点击欣赏更多女神！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
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
        nd['pic_url'] = MEDIA_BASE_URL + obj.photo.url
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
        nd['pic_url'] = MEDIA_BASE_URL + obj.photo.url
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
        st['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        st['url'] = obj.url
        stl.append(st)
    more = {
        "title": u"点击查看更多美食小吃！！",
        "description": u"点击查看更多美食小吃！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
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
        bx['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        bx['url'] = obj.url
        bxl.append(bx)
    more = {
        "title": u"点击查看更多丰盛大餐！！",
        "description": u"点击查看更多丰盛大餐！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
    }
    bxl.append(more)
    return bxl


# 经典回顾
def get_jdhg():
    objs = Voice.objects.jdhg(VOICE_NUM)
    jdl = []
    for obj in objs:
        jd = {}
        jd['title'] = obj.title
        jd['description'] = obj.intro
        jd['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        jd['url'] = obj.url
        jdl.append(jd)
    more = {
        "title": u"点击查看更多经典回顾！！",
        "description": u"点击查看更多经典回顾！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
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
        bs['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        bs['url'] = obj.url
        bsl.append(bs)
    more = {
        "title": u"点击查看更多不三不四！！",
        "description": u"点击查看更多不三不四！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
    }
    bsl.append(more)
    return bsl


# 摆饭秀
def get_bfx():
    objs = Voice.objects.bfx(VOICE_NUM)
    bfl = []
    for obj in objs:
        bf = {}
        bf['title'] = obj.title
        bf['description'] = obj.intro
        bf['pic_url'] = MEDIA_BASE_URL + obj.photo.url
        bf['url'] = obj.url
        bfl.append(bf)
    more = {
        "title": u"点击查看更多摆饭秀！！",
        "description": u"点击查看更多摆饭秀！！",
        "pic_url": "",
        "url": "http:www.baidu.com"
    }
    bfl.append(more)
    return bfl





