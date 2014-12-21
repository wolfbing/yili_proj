
# -*- coding: utf-8 -*-


__author__ = 'bingliu'


from django.http import HttpResponse, HttpRequest
from django.shortcuts import render_to_response
import json
from django.core.urlresolvers import reverse

from wechat.models import BoysAndGirls, FineFood, Voice, IndexSlider
from wechat.models import BFX as BFShow

from views import STATIC_BASE_URL

# setting
MAX_SLIDER_NUM = 5
LIST_NUM_PER_PAGE = 5

# const variaty
NS = u"NS"
NVS = u"NVS"
JDHG = u"JDHG"
BSBS = u"BSBS"
BFX = u"BFX"
PMS = u"PMS"


def index(request):
    res_data = {
        u"title": u"首页|有些",
        u"static_url": STATIC_BASE_URL,
        # u"articles": index_article_list(),
        u"sliders": get_sliders(),
    }
    menu_data = [
        {
            u"name": u"女神",
            u"intro": u"括拉拉档案每日女神",
            u"url": reverse(kll_list, kwargs={"page":1, "type":NVS.lower()}),
            u"img_url": STATIC_BASE_URL + "images/menu_nvs.jpg"
        },
        {
            u"name": u"男神",
            u"intro": u"括拉拉档案每日男神",
            u"url": reverse(kll_list, kwargs={"page":1, "type":NS.lower()}),
            u"img_url": STATIC_BASE_URL + "images/menu_ns.jpg"
        },
        {
            u"name": u"摆饭秀",
            u"intro": u"摆饭秀",
            u"url": reverse(fanshow_list, kwargs={"page":1} ),
            u"img_url": STATIC_BASE_URL + "images/menu_bfx.jpg"
        },
        {
            u"name": u"经典回顾",
            u"intro": u"有些声音-经典回顾",
            u"url": reverse(voice_list, kwargs={"page":1, "type":JDHG.lower()}),
            u"img_url": STATIC_BASE_URL + "images/menu_jdhg.jpg"
        },
        {
            u"name": u"不三不四",
            u"intro": u"有些声音-不三不四",
            u"url": reverse(voice_list, kwargs={"page":1, "type":BSBS.lower()}),
            u"img_url": STATIC_BASE_URL + "images/menu_bsbs.jpg"
        },
        {
            u"name": u"泡美食",
            u"intro": u"泡美食",
            u"url": reverse("finefoodlist", kwargs={"page":1} ),
            u"img_url": STATIC_BASE_URL + "images/menu_pms.jpg"
        },
        {
            u"name": u"括拉拉档案",
            u"intro": u"投稿-括拉拉档案",
            u"url": reverse("attendkll"),
            u"img_url": STATIC_BASE_URL + "images/menu_kll.png"
        },
        {
            u"name": u"美食推荐",
            u"intro": u"投稿-美食推荐",
            u"url": reverse("recommendfood"),
            u"img_url": STATIC_BASE_URL + "images/menu_mstj.png"
        },
        {
            u"name": u"我来秀",
            u"intro": u"投稿-我来秀",
            u"url": reverse("fanshow"),
            u"img_url": STATIC_BASE_URL + "images/menu_show.png"
        }
    ]
    res_data['menus'] = menu_data
    res_data.update(base_res_data())
    return render_to_response("index.html", res_data)

def kll_list(request, page, type):
    res_data = {
        u"title": u"括拉拉档案",
        u"static_url": STATIC_BASE_URL,
        u"objs": get_kll_list(type, page),
        u"sync_url": u"/mobile/ajaxklllist/"
    }
    res_data.update(base_res_data())
    num = None
    if type.upper() == NS:
        res_data[u"column_name"] = u"有些男神"
        num = BoysAndGirls.objects.ns_num()
        res_data["type"] = NS.lower()
    else:
        res_data[u"column_name"] = u"有些女神"
        num = BoysAndGirls.objects.nvs_num()
        res_data["type"] = NVS.lower()
    total_page_num = num/LIST_NUM_PER_PAGE
    if num%LIST_NUM_PER_PAGE != 0:
        total_page_num +=1
    res_data["total_page_num"] = total_page_num
    res_data["current_page_num"] = int(page)
    page_range =[p+1 for p in range(total_page_num) ]
    res_data["page_range"] = page_range
    return render_to_response("news_list.html", res_data)


def ajax_kll_list(request, page, type):
    klls = get_kll_list(type, page)
    return HttpResponse(json.dumps(klls, ensure_ascii=False))


def voice_list(request, type, page):
    res_data = {
        u"title": u"有些声音",
        u"static_url": STATIC_BASE_URL,
        u"objs": get_voice_list(type, page),
        u"sync_url": u"/mobile/ajaxvoicelist/"
    }
    res_data.update(base_res_data())
    num = None
    if type.upper() == JDHG:
        res_data[u"column_name"] = u"经典回顾"
        num = Voice.objects.jdhg_num()
        res_data["type"] = JDHG.lower()
    else:
        res_data[u"column_name"] = u"不三不四"
        num = Voice.objects.bsbs_num()
        res_data["type"] = BSBS.lower()
    total_page_num = num/LIST_NUM_PER_PAGE
    if num%LIST_NUM_PER_PAGE != 0:
        total_page_num +=1
    res_data["total_page_num"] = total_page_num
    res_data["current_page_num"] = int(page)
    page_range =[p+1 for p in range(total_page_num) ]
    res_data["page_range"] = page_range
    return render_to_response("news_list.html", res_data)


def ajax_voice_list(request, page, type):
    vs = get_voice_list(type, page)
    return HttpResponse(json.dumps(vs, ensure_ascii=False))


def fine_food_list(request, page):
    res_data = {
        u"title": u"泡美食",
        u"static_url": STATIC_BASE_URL,
        u"objs": get_pms_list(page),
        u"sync_url": u"/mobile/ajaxpmslist/"
    }
    res_data.update(base_res_data())
    res_data[u"column_name"] = u"泡美食"
    num = FineFood.objects.pms_num()
    res_data["type"] = PMS.lower()
    total_page_num = num/LIST_NUM_PER_PAGE
    if num%LIST_NUM_PER_PAGE != 0:
        total_page_num += 1
    res_data["total_page_num"] = total_page_num
    res_data["current_page_num"] = int(page)
    page_range =[p+1 for p in range(total_page_num) ]
    res_data["page_range"] = page_range
    return render_to_response("news_list.html", res_data)


def ajax_fine_food_list(request, page):
    pms = get_pms_list(page)
    return HttpResponse(json.dumps(pms, ensure_ascii=False))


def fanshow_list(request, page):
    res_data = {
        u"title": u"摆饭秀",
        u"static_url": STATIC_BASE_URL,
        u"objs": get_bfx_list(page),
        u"sync_url": u"/mobile/ajaxbfxlist/"
    }
    res_data.update(base_res_data())
    res_data[u"column_name"] = u"摆饭秀"
    num = BFShow.objects.bfx_num()
    res_data["type"] = BFX.lower()
    total_page_num = num/LIST_NUM_PER_PAGE
    if num%LIST_NUM_PER_PAGE != 0:
        total_page_num += 1
    res_data["total_page_num"] = total_page_num
    res_data["current_page_num"] = int(page)
    page_range =[p+1 for p in range(total_page_num) ]
    res_data["page_range"] = page_range
    return render_to_response("news_list.html", res_data)


def ajax_fanshow_list(request, page):
    shows = get_bfx_list(page)
    return HttpResponse(json.dumps(shows, ensure_ascii=False))


def play_audio(request, id):
    v = Voice.objects.get_voice_by_id(id)
    res_data = {
        u"title": v.title,
        u"author": v.author,
        u"audio_url": v.audio.url,
        u"img_url": v.player_pic.url,
        u"static_url": STATIC_BASE_URL
    }
    res_data.update(base_res_data())
    return render_to_response("audio_player.html", res_data)


# index页面article-list
def index_article_list():
    ns = BoysAndGirls.objects.ns(1)
    nvs = BoysAndGirls.objects.nvs(1)
    food = FineFood.objects.pms(1)
    fan_show = Voice.objects.bfx(1)
    article_list = []
    if len(ns)>0:
        ns = ns[0]
        article1 = {
            "title": ns.title,
            "intro": ns.intro,
            "url": ns.url,
            "pic_url": ns.photo.url
        }
        article_list.append(article1)
    if len(nvs)>0:
        nvs = nvs[0]
        article2 = {
            "title": nvs.title,
            "intro": nvs.intro,
            "url": nvs.url,
            "pic_url": nvs.photo.url
        }
        article_list.append(article2)
    if len(food)>0:
        food = food[0]
        article3 = {
            "title": food.title,
            "intro": food.intro,
            "url": food.url,
            "pic_url": food.photo.url
        }
        article_list.append(article3)
    if len(fan_show)>0:
        fan_show = fan_show[0]
        article4 = {
            "title": fan_show.title,
            "intro": fan_show.intro,
            "url": fan_show.url,
            "pic_url": fan_show.pic.url
        }
        article_list.append(article4)
    return article_list


def get_sliders():
    objs = IndexSlider.objects.new_slider(MAX_SLIDER_NUM)
    sliders = []
    for obj in objs:
        slider = {
            "pic_url": obj.pic.url,
            "intro": obj.intro
        }
        sliders.append(slider)
    return sliders


# 从括拉拉档案中选一些
def get_kll_list(type, page):
    objs = None
    start = (int(page)-1)*LIST_NUM_PER_PAGE
    end = int(page)*LIST_NUM_PER_PAGE
    if type.upper() == NS:
        objs = BoysAndGirls.objects.some_ns(start, end)
    else:
        objs = BoysAndGirls.objects.some_nvs(start, end)
    klls = []
    for obj in objs:
        kll = {
            "title": obj.title,
            "intro": obj.intro,
            "pic_url": obj.photo.url,
            "url": obj.url
        }
        klls.append(kll)
    return klls


def get_voice_list(type, page):
    objs = None
    start = (int(page)-1)*LIST_NUM_PER_PAGE
    end = int(page)*LIST_NUM_PER_PAGE
    if type.upper() == JDHG:
        objs = Voice.objects.some_jdhg(start, end)
    else:
        objs = Voice.objects.some_bsbs(start, end)
    vs = []
    for obj in objs:
        v = {
            "title": obj.title,
            "intro": obj.intro,
            "pic_url": obj.pic.url
        }
        if obj.url != u"":
            v["url"] = obj.url
        else:
            v["url"] = reverse(play_audio, kwargs={"id": obj.id})
        vs.append(v)
    return vs

def get_bfx_list(page):
    start = (int(page)-1)*LIST_NUM_PER_PAGE
    end = int(page)*LIST_NUM_PER_PAGE
    objs = BFShow.objects.some_bfx(start, end)
    vs = []
    for obj in objs:
        v = {
            "title": obj.title,
            "intro": obj.intro,
            "pic_url": obj.pic.url,
            "url": obj.url
        }
        vs.append(v)
    return vs


def base_res_data():
    data = {
        u"index_url": reverse(index),
        u"nvs_url": reverse(kll_list, kwargs={"type":"nvs", "page":1}),
        u"ns_url": reverse(kll_list, kwargs={"type":"ns", "page":1}),
        u"jdhg_url": reverse(voice_list, kwargs={"type":"jdhg", "page":1}),
        u"bsbs_url": reverse(voice_list, kwargs={"type":"bsbs", "page":1}),
        u"kll_url": reverse("attendkll"),
        u"mstj_url": reverse("recommendfood"),
        u"show_url": reverse("fanshow"),
        u"bfx_url": reverse(fanshow_list, kwargs={"page":1}),
        u"pms_url": reverse(fine_food_list, kwargs={"page":1})
    }
    return data


def get_pms_list(page):
    start = (int(page)-1)*LIST_NUM_PER_PAGE
    end = int(page)*LIST_NUM_PER_PAGE
    objs = FineFood.objects.some_pms(start, end)
    msl = []
    for obj in objs:
        ms = {
            "title": obj.title,
            "intro": obj.intro,
            "pic_url": obj.photo.url
        }
        ms["url"] = obj.url
        msl.append(ms)
    return msl

