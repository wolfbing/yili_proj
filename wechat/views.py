
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.http import HttpResponse

import string
import hashlib
import time
from xml.etree import ElementTree as ET

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

# msg type
TEXT_MSG = "text"


# wechat 请求入口
def main(request):
    data = parse_msg(request.body)
    return text_msg(data)


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






