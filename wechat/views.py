
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

# msg judget
EVENT = "Event"
EVENT_KEY = "EventKey"
MSG_TYPE = "MsgType"

logger = logging.getLogger('wechat')

# wechat 请求入口
def main(request):
    try:
        req_data = parse_msg(request.body)
        if req_data[MSG_TYPE] == EVENT_MSG:
            if req_data[EVENT_KEY] == NS:
                return news_msg(req_data)
            else:
                return text_msg(req_data)
        else:
            return text_msg(req_data)
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


def text_msg(request_data):
    create_time = int(time.time())
    content = "this is text msg"
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





