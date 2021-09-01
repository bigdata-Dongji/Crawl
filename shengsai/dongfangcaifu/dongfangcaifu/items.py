# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DongfangcaifuItem(scrapy.Item):
    # define the fields for your item here like:
    id = scrapy.Field()
    dm = scrapy.Field()
    name = scrapy.Field()
    zxj = scrapy.Field()
    zde = scrapy.Field()
    zdf = scrapy.Field()
    cjl = scrapy.Field()
    cje = scrapy.Field()
    zs = scrapy.Field()
    jk = scrapy.Field()
    zg = scrapy.Field()
    zd = scrapy.Field()
    wb = scrapy.Field()
    # pass

class HLWZGItem(scrapy.Item):
    id = scrapy.Field()
    name = scrapy.Field()
    zxj = scrapy.Field()
    zde = scrapy.Field()
    zdf = scrapy.Field()
    kpj = scrapy.Field()
    zgj = scrapy.Field()
    zdj = scrapy.Field()
    zsj = scrapy.Field()
    zsz = scrapy.Field()
    syl = scrapy.Field()