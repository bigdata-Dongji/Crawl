# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class LianxiPipeline(object):
    ziduanming = ['名字', '规格', '面积', '地址', '路段', '价格', '单价']
    with open("./anjuke.csv", 'a', encoding="utf-8", newline="")as f:
        wri = csv.writer(f)
        wri.writerow(ziduanming)
    def process_item(self, item, spider):
        datas = []
        for i in item.values():
            datas.append(i)
        with open("./anjuke.csv", 'a', encoding="utf-8", newline="")as f:
            wri = csv.writer(f)
            wri.writerow(datas)
        print(item)
        return item
