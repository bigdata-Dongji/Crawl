# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class WeatherPipeline(object):
    def process_item(self, item, spider):

        with open('../tianqi.csv','a',encoding='utf-8',newline='')as f:
            writer = csv.writer(f)
            writer.writerow([item['name'],item['jujin'],item['riqi'],item['tianqi'],item['wendu']])

        with open('../tianqi.json','a',encoding='utf-8')as f:
            f.write(str(item)+'\n')
        return item
