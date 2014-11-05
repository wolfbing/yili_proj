from django.conf.urls import patterns, include, url
from django.contrib import admin
from wechat import views as wechat_view
import settings

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

)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    )
