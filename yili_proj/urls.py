
# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib import admin
from wechat import views as wechat_view
import settings
from wechat import ddbb_view
from wechat import mobile_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yili_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^wechat/$', wechat_view.main),
    url(r'^wechat/allns/$', wechat_view.all_ns),
    url(r'^wechat/morens/$', wechat_view.more_ns),
    url(r'^wechat/allnvs/$', wechat_view.all_nvs),
    url(r'^wechat/allst/$', wechat_view.all_food, {"ft": "ST"}),
    url(r'^wechat/allbx/$', wechat_view.all_food, {"ft": "BX"}),
    url(r'^wechat/alljdhg/$', wechat_view.all_voice, {"vt": "JDHG"}),
    url(r'^wechat/allbsbs/$', wechat_view.all_voice, {"vt": "BSBS"}),
    url(r'^wechat/allbfx/$', wechat_view.all_voice, {"vt": "BFX"}),
    url(r"^wechat/test/$", wechat_view.test),
    url(r'^wechat/playaudio/', wechat_view.play_audio),
    url(r'^wechat/attendkll/$', wechat_view.attend_kulala, name="attendkll"),
    url(r'^wechat/recommendfood/$', wechat_view.recommend_food, name="recommendfood"),
    url(r'^wechat/fanshow/$', wechat_view.fan_show, name="fanshow"),
    url(r"^wechat/klllist/$", wechat_view.view_kll_post),
    url(r"^wechat/klldetail/(?P<id>\d+)/$", wechat_view.view_kll_detail),
    url(r"^wechat/fanshowlist/$", wechat_view.view_bfx_post),
    url(r"^wechat/fanshowdetail/(?P<id>\d+)/$",wechat_view.view_bfx_detail),

)

# mobile web
urlpatterns += patterns("",
    url(r"^mobile/index/$", mobile_view.index),
    url(r"^mobile/klllist/(?P<type>ns|nvs)/(?P<page>\d+)/$", mobile_view.kll_list, name="kll_list"),
    url(r"^mobile/playaudio/$", mobile_view.play_audio),
    url(r"^mobile/ajaxklllist/(?P<type>ns|nvs)/(?P<page>\d+)/$", mobile_view.ajax_kll_list),
    url(r"^mobile/voicelist/(?P<type>jdhg|bsbs)/(?P<page>\d+)/$", mobile_view.voice_list, name="voicelist"),
    url(r"^mobile/ajaxvoicelist/(?P<type>jdhg|bsbs)/(?P<page>\d+)/$", mobile_view.ajax_voice_list),
    url(r"^mobile/playaudio/(?P<id>\d+)/$", mobile_view.play_audio),
    url(r"^mobile/bfxlist/bfx/(?P<page>\d+)/$", mobile_view.fanshow_list, name="bfxlist"),
    url(r"^mobile/ajaxbfxlist/bfx/(?P<page>\d+)/$", mobile_view.ajax_fanshow_list),
    url(r"^mobile/pmslist/pms/(?P<page>\d+)/$", mobile_view.fine_food_list, name="finefoodlist"),
    url(r"^mobile/ajaxpmslist/pms/(?P<page>\d+)/$", mobile_view.ajax_fine_food_list),
)

# 滴滴叭叭URL
urlpatterns += patterns("",
    url(r"^wechat/ddbb/$", ddbb_view.main),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
