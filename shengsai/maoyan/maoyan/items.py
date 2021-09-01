# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    movieName = scrapy.Field()
    movieInfo = scrapy.Field()
    releaseInfo = scrapy.Field()
    boxSplitUnit = scrapy.Field()
    sumBoxDesc = scrapy.Field()
    showCount = scrapy.Field()
    boxRate = scrapy.Field()
    avgSeatView = scrapy.Field()
    avgShowView = scrapy.Field()

