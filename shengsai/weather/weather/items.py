# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class WeatherItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    riqi = scrapy.Field()
    jujin = scrapy.Field()
    tianqi = scrapy.Field()
    wendu = scrapy.Field()
    url = scrapy.Field()
#