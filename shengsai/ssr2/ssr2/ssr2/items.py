# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ssr2Item_1(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    duration = scrapy.Field()
    release_time = scrapy.Field()
    score = scrapy.Field()
    detail = scrapy.Field()


class Ssr2Item_2(scrapy.Item):
    url = scrapy.Field()
    tags = scrapy.Field()
    plot = scrapy.Field()
    directors = scrapy.Field()
