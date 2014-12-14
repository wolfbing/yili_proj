
# -*- coding: utf-8 -*-

__author__ = 'bingliu'


from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
import views
import string
import hashlib

## const variant
# menu key
MR = "MR"
MRS = "MRS"
FANSHOW = "FANSHOW"

# request xml中的key
MSG_TYPE = "MsgType"

# msg type
TEXT_MSG = "text"

# answer text
welcome_text = u"Hello~亲爱的早饭，感谢您关注滴滴叭叭早上好，这里每天都会为大家发布各种有趣资讯，" \
               u"快来和我们一起互动吧！么么哒~~/呲牙"


def main(request):
    req_data = views.parse_msg(request.body)
    if req_data[MSG_TYPE] == TEXT_MSG:
        return views.text_msg(req_data, welcome_text)
    else:
        return HttpResponse("")


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




