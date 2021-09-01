# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class KkgameItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    game_name=scrapy.Field()
    game_url=scrapy.Field()
    pinlunnum=scrapy.Field()
    game_type=scrapy.Field()
    game_size=scrapy.Field()
    game_date=scrapy.Field()
    game_score=scrapy.Field()
    game_title=scrapy.Field()
    game_ms=scrapy.Field()
