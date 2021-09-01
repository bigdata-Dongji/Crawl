# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class GushiPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # with open('./guhsi.csv','a',encoding="utf-8",newline='')as f:
        #     f.write((item,)+'\n')
        return item
