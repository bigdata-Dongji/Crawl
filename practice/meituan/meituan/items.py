# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MeituanItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    addr = scrapy.Field()
    commentsCountDesc = scrapy.Field()
    scoreIntro = scrapy.Field()
    hotelStar = scrapy.Field()
    historySaleCount = scrapy.Field()
    # pass
