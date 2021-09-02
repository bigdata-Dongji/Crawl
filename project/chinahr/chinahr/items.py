# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class ChinahrItem(scrapy.Item):
    name=scrapy.Field()# 职位名称
    salary=scrapy.Field()#薪水
    edu=scrapy.Field()#学历
    exp=scrapy.Field()  #经验
    demand=scrapy.Field() # 招聘人数
    classification=scrapy.Field() #分类
    treatment=scrapy.Field() # 福利待遇
    time=scrapy.Field()# 更新时间
    detail=scrapy.Field()# 职位描述

    com_name=scrapy.Field() # 公司名字
    industry=scrapy.Field() # 公司所属行业
    people_num=scrapy.Field() # 公司人数
    address=scrapy.Field() # 公司的地址
    introduce=scrapy.Field() # 公司介绍

    city=scrapy.Field() # 来源城市

