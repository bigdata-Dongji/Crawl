# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class AnjukeItem(scrapy.Item):
    # define the fields for your item here like:
    title = scrapy.Field()
    guige = scrapy.Field()
    mianji = scrapy.Field()
    cengshu = scrapy.Field()
    year = scrapy.Field()
    price = scrapy.Field()
    danjia = scrapy.Field()
    xiaoqu = scrapy.Field()
    luxian = scrapy.Field()
    pass
