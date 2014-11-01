
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import loader, Context

import string
import hashlib
import time
from xml.etree import ElementTree as ET
import logging

# Create your views here.

# keys of menu
NS = 'NS'
NVS = 'NVS'
BZNS = 'BZNS'
BZNVS = 'BZNVS'
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
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == NVS:
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == BZNS:
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == BZNVS:
                    return news_msg(req_data)
                ###  有些美食
                elif req_data[EVENT_KEY] == ST:
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == BX:
                    return news_msg(req_data)
                ###  有些声音
                elif req_data[EVENT_KEY] == JDHG:
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == BSBS:
                    return news_msg(req_data)
                elif req_data[EVENT_KEY] == BFX:
                    return news_msg(req_data)
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


def news_msg(req_data):
    create_time = int(time.time())
    article_count = 1
    articles = [
        {
            "title": u"欢迎关注 ‘有些’ ！",
            "description": u"早饭们，欢迎关注有些！",
            "pic_url": "http://121.199.32.77/media/avatar.jpg",
            "url": "http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=200725485&idx=1&sn=26061f0bc214aa445e00e81264b9908c#rd"
        }
    ]
    res_data = {
        "to_user": req_data['FromUserName'],
        "from_user": req_data['ToUserName'],
        "create_time": create_time,
        "article_count": article_count,
        "articles": articles
    }
    return render_to_response('news_msg.xml', res_data)





