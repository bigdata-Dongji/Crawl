# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Lianjia1Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    structure = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    price = scrapy.Field()
    # pass
