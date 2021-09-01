# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BooszpItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()   #职位
    position = scrapy.Field()   #地址
    site = scrapy.Field()   #发布时间
    date = scrapy.Field()   #薪资
    pay = scrapy.Field()   #工作经验
    experience = scrapy.Field()   #学历要求
    company = scrapy.Field()   #公司名称
    company_type = scrapy.Field()   #公司类型
    financing = scrapy.Field()   #融资类型
    number_of_people = scrapy.Field()  #企业规模类型
    technology = scrapy.Field()    #技术手段
    welfare = scrapy.Field()   ##员工福利
    # pass
