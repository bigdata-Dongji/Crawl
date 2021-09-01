# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class LianjiaPipeline(object):
    def process_item(self, item, spider):
        with open('lianjia.json','a',encoding='utf-8',newline='')as f:
            f.write(str(item)+'\n')

        with open('lianjia.csv', 'a', encoding='utf-8', newline='')as f:
            wri = csv.writer(f)
            wri.writerow([item['name'],item['xiaoqu'],item['biaoqian'],item['danjia'],item['fabu'],item['guige'],item['price'],item['url']])

        return item
