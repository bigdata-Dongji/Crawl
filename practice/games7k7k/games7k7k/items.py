# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Games7K7KItem(scrapy.Item):
    # define the fields for your item here like:
    game_name = scrapy.Field()
    game_type = scrapy.Field()
    game_url = scrapy.Field()
    game_size = scrapy.Field()
    game_date = scrapy.Field()
    game_score = scrapy.Field()
    game_biaoqian = scrapy.Field()
    # pass
