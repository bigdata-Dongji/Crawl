# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class CsdnItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    yuanchuang = scrapy.Field()
    date = scrapy.Field()
    yuedu = scrapy.Field()
    type = scrapy.Field()
    biaoqian = scrapy.Field()
    url = scrapy.Field()


