
# -*- coding: utf-8 -*-

__author__ = 'bingliu'

from datetime import datetime, timedelta

AppID = "wxc3b4309f72da3250"
AppSecret = "0d6f40b8e7a478b8efb43e1e027c39aa"

GetAccessTokenUrl = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential" \
                    "&appid=%s&secret=%s" % (AppID, AppSecret)

LastTokenTime = datetime.fromtimestamp(0)
TokenExpire = timedelta(seconds=2000)
AccessToken = ""

DownloadMediaUrl = "http://file.api.weixin.qq.com/cgi-bin/media/get" \
                   "?access_token=%s&media_id=%s"

