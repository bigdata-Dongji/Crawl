# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Job51Pipeline(object):
    def process_item(self, item, spider):
        with open('51job.json','a',encoding='utf-8',newline='')as f:
            f.write(str(item))
            f.write('\n')
        return item
