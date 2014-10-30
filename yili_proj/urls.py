from django.conf.urls import patterns, include, url
from django.contrib import admin
from wechat import views as wechat_view

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'yili_proj.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^wechat/$', wechat_view.main),
)
