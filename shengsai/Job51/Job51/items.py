# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Job51Item(scrapy.Item):
    # define the fields for your item here like:
    job_name = scrapy.Field()       #职位
    job_href = scrapy.Field()       #职位链接
    company_name = scrapy.Field()       #公司名称
    company_href = scrapy.Field()       #公司链接
    providesalary_text = scrapy.Field()       #工资
    workarea_text = scrapy.Field()       #地址
    updatedate = scrapy.Field()       #更新时间
    companytype_text = scrapy.Field()       #公司类型
    jobwelf = scrapy.Field()       #福利待遇
    attribute_text = scrapy.Field()       #学历要求
    # name = scrapy.Field()
