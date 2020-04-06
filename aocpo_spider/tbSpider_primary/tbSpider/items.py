# -*- coding: utf-8 -*-
import scrapy

class postDataItem(scrapy.Item):
    school = scrapy.Field()
    tid = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    date = scrapy.Field()
    reply_num = scrapy.Field()
    author_name = scrapy.Field()
    reply_content = scrapy.Field()
    device = scrapy.Field()
    sentiment = scrapy.Field()
    classify = scrapy.Field()

class authorDataItem(scrapy.Item):
    school = scrapy.Field()
    user_name = scrapy.Field()
    name_show = scrapy.Field()
    sex = scrapy.Field()
    tb_age = scrapy.Field()
    post_num = scrapy.Field()
    tb_vip = scrapy.Field()
    fans = scrapy.Field()



