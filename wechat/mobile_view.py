
# -*- coding: utf-8 -*-


__author__ = 'bingliu'


from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response

from views import STATIC_BASE_URL

def index(request):
    res_data = {
        u"title": u"首页|有些",
        u"static_url": STATIC_BASE_URL
    }
    return render_to_response("index.html", res_data)

def kll_list(request):
    res_data = {
        u"title": u"括拉拉档案",
        u"static_url": STATIC_BASE_URL
    }
    return render_to_response("news_list.html", res_data)

def play_audio(request):
    res_data = {
        u"title": u"经典回顾",
        u"static_url": STATIC_BASE_URL
    }
    return render_to_response("audio_player.html", res_data)
