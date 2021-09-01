# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import logging

logger = logging.getLogger(__name__)

class DangdangPipeline(object):
    def process_item(self, item, spider):
        print(item)
        logger.warning(item)
        with open("./东野圭吾书籍.json",'a',encoding="utf-8",newline="")as f:     #将接收到的数据进行写入
            f.write(json.dumps(item,ensure_ascii=False)+'\n')       #将字典型数据转为字符串进行写入
        return item
