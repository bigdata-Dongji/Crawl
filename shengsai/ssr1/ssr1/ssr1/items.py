# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Ssr1Item(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    location = scrapy.Field()
    duration = scrapy.Field()
    release_time = scrapy.Field()
    score = scrapy.Field()
    tags = scrapy.Field()
    plot = scrapy.Field()
    directors = scrapy.Field()
