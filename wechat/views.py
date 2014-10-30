
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import HttpResponse

import string
import hashlib

# Create your views here.


# wechat 请求入口
def main(request):
    return HttpResponse("request entrance")


def check_signature(request):
    signature = request.GET['signatue']
    ts = request.GET['timestamp']
    nonce = request.GET['nonce']
    echo_str = request.GET['echostr']
    token = 'weixinsome'
    arr = [token, ts, nonce]
    arr.sort()
    tmp_str = string.join(arr, '')
    sha1_obj = hashlib.sha1(tmp_str)
    sha1_str = sha1_obj.digest()
    if sha1_str == signature:
        return HttpResponse(echo_str)
    else:
        return HttpResponse('')





