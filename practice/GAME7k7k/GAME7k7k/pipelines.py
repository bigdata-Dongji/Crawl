# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class Game7K7KPipeline(object):
    def process_item(self, item, spider):
        print(item)
        with open('xiaoyouxi7k7k.csv','a',encoding="utf-8",newline="")as f:
            wri = csv.writer(f)
            wri.writerows([[item['name'],item['url'],item['jianjie']]])
        # return item
