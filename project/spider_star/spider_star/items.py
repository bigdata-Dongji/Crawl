# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SpiderStarItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 目录页
    name=scrapy.Field()
    images_url=scrapy.Field() # 明星图片大全链接

    # 详情页
    introduction=scrapy.Field() # 明星简介
    images=scrapy.Field()
    image_res=scrapy.Field()
