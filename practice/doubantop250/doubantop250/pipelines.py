# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json

class Doubantop250Pipeline(object):
    def process_item(self, item, spider):
        print(item["urls"])
        with open('./doubantop250.json','a',encoding="utf-8",newline='')as f:
            f.write(json.dumps(item,ensure_ascii=False)+'\n')
        return item
