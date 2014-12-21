from django.contrib import admin

from models import BoysAndGirls, FineFood, Voice, StaticMedia, \
    FansKLLMedia, FansKLL, FansMSTJ, FansMSTJMedia, FanShowMedia, FanShow, \
    AtypicalVisitor, IndexSlider, BFX
# Register your models here.

admin.site.register(BoysAndGirls)
admin.site.register(FineFood)
admin.site.register(Voice)
admin.site.register(StaticMedia)
admin.site.register(FansKLL)
admin.site.register(FansKLLMedia)
admin.site.register(FansMSTJ)
admin.site.register(FansMSTJMedia)
admin.site.register(FanShow)
admin.site.register(FanShowMedia)
admin.site.register(AtypicalVisitor)
admin.site.register(IndexSlider)
admin.site.register(BFX)
