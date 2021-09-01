# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import pymysql
class MeinvPipeline(object):
    def process_item(self, item, spider):
        html = requests.get(item['url'])
        with open("./meinv/meinv/"+item['name']+".jpg",'ab')as f:
            f.write(html.content)
        print(item)
        return item
