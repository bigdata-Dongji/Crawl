# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import requests

class BianzhuomianPipeline(object):
    def process_item(self, item, spider):
        # print(type(item))
        #将图片写入本地文件夹

        return item
