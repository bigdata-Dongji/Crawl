# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import requests
import logging
logger = logging.getLogger(__name__)

class FengniaoPipeline(object):
    def process_item(self, item, spider):
        logger.warning(item)
        html = requests.get(item['image'])
        with open('G:/Python文件/scrapy框架/fengniao/fengniao/cunfang/'+item['name']+'.jpg','wb')as f:
            f.write(html.content)
        return item
