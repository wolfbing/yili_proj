
# -*- coding: utf-8 -*-

__author__ = 'bingliu'

str_welcome = u"欢迎关注有些！真诚交友、分享美食、一起聆听有趣的声音，和磊磊娜娜一起关注【有些】，快乐与你同在! " \
              u"\n点击下方菜单，发现更多精彩！\n如需帮助，回复‘帮助’"

str_help = u'''亲爱的有些粉丝! 您可以回复以下关键字获取相关帮助:
    1. 括拉拉档案
    2. 推荐美食
    3. 我来秀
    4. 女神
    5. 男神
    6. 摆饭秀

    点点下方菜单，发现更多精彩！

    如果您在和小编沟通，就忽略这条消息吧～
    '''

str_history = u"点击右上角，在进入的页面中就能看到‘查看历史消息’按钮了！\n还不清楚的话，点击下面连接吧：" \
              u"\nhttp://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201606432&idx=1&sn=43fb0317b7bd6f8a96c8a550bb0658ef#rd"

str1 = u"点击下面链接了解报名括拉拉档案详情, 很简单的哦~\n" + u"http://121.199.32.77/wechat/attendkll/"
str2 = u"点击下面链接了解推荐美食的方法, 很简单的, 期待着您的推荐哦~\n" + u"http://121.199.32.77/wechat/recommendfood/"
str3 = u"点击下面链接了解参加摆饭秀的方法，很简单的~ 舞台很宽敞，期待你来秀！\n" + u"http://127.0.0.1:8000/wechat/fanshow/"
str4 = u"点击下面链接，欣赏更多女神！\n" + u"http://121.199.32.77/mobile/klllist/nvs/1/"
str5 = u"点击下面链接，欣赏更多男神！\n" + u"http://121.199.32.77/mobile/klllist/ns/1/"
str6 = u"点击下面链接，欣赏更多摆饭秀！\n" + u"http://121.199.32.77/mobile/bfxlist/bfx/1/"


str_suancaiyu = u"店名：天府渔歌；\n地址：南京市洋珠巷玉带园彩霞街菜市场门口"
str_huntun = u"店名：味真馄饨；\n地址：南京市茶南大街茶南兆园13栋44号103（茶南大街建设银行旁巷内）"
str_yuyangxian = u'''鱼羊一锅鲜做法:
    将羊肉切块，焯水后洗净。加入水、枸杞、当归、黄芪、陈皮、红枣大火烧开小火慢炖两至三个小时，捞出炖烂的羊肉备用。
    另起一锅放入葱姜以两条鲫鱼炖汤备用。
    取鱼汤加入炖好的羊肉、红枣，以火锅方式上桌。准备萝卜、金针菇或其他蔬菜作为火锅配料。食用时根据各人口味准备蘸料食用。
    简单美味，喜欢羊肉的朋友不妨一试！
    '''
str_daroumian = u"店名：刘记大肉面，地址：南京市三牌楼小区1号门"


ANSWER = {

    u"welcome": str_welcome,

    u"帮助": str_help,
    u"help": str_help,
    u"历史消息": str_history,


    u"1": str1,
    u"括拉拉档案": str1,
    u"2": str2,
    u"推荐美食": str2,
    u"3": str3,
    u"我来秀": str3,
    u"4": str4,
    u"女神": str4,
    u"5": str5,
    u"男神": str5,
    u"6": str6,
    u"摆饭秀": str6,

    u"common": u"",
    u"酸菜鱼": str_suancaiyu,
    u"超火酸菜鱼": str_suancaiyu,
    u"馄饨": str_huntun,
    u"鱼羊鲜": str_yuyangxian,
    u"大肉面": str_daroumian

}

news_katong = {
    u"title": u"磊磊娜娜圣诞卡通形象新鲜出炉喽！",
    u"description": u"圣诞节来了，小编也不知道送大家啥礼物好。想来想去还是把磊磊娜娜送给大家吧，特意制作了他们的圣诞卡通形象，大家看看，喜欢吗？",
    u"pic_url": u"http://121.199.32.77/media/wechat/staticmedia/2014/12/640_13.jpeg",
    u"url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201914089&idx=4&sn=8514beb63664b1acaed982236a6077b5#rd"
}

news_yinweiaiqing = {
    u"title": u"磊磊娜娜年度深情演绎，《因为爱情》！",
    u"description": u"给你一张过去的CD，听听那时我们的爱情，有时会突然忘了我还在爱着你，再唱不出那样的歌曲",
    u"pic_url": u"http://121.199.32.77/media/wechat/staticmedia/2014/12/640_16.jpeg",
    u"url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201947522&idx=3&sn=744262ec5ce54699a2d2c5f6f7808e28#rd"
}

news_nanjing = {
    u"title": u"人生就像南京",
    u"description": u"人生像新街口地下广场，总能找到一个出口",
    u"pic_url": u"http://121.199.32.77/media/wechat/staticmedia/2014/12/640_19.jpeg",
    u"url": u"http://mp.weixin.qq.com/s?__biz=MjM5NzY3NjU3MA==&mid=201984001&idx=2&sn=4b206a35d7a6c038ee9ecc9d0276d3e8#rd"
}

NEWS_ANSWER = {
    u"卡通": [news_katong],
    u"圣诞": [news_katong],
    u"磊磊娜娜": [news_katong],
    u"因为爱情": [news_yinweiaiqing],
    u"人生": [news_nanjing],
    u"南京": [news_nanjing]
}




