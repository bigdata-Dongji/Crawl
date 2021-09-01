# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import json

class Maoyantop100Pipeline(object):
    def process_item(self, item, spider):
        print(item)     #将接受到的数据进行输出查看数据是否完整
        with open("./maoyan.json",'a',newline='',encoding="utf-8")as f:     #定义一个写入
            f.write(json.dumps(item,ensure_ascii=False))        #将数据写入文件
            f.write('\n')       #自定义写入换行
        return item
