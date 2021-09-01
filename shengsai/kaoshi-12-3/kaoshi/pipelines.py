# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import csv
import requests

class KaoshiPipeline(object):
    def process_item(self, item, spider):
        #写入csv
        with open('movies.csv','a',encoding='utf-8',newline='')as f:
            write = csv.writer(f)
            write.writerow([item['name'],item['city'],item['date'],item['score'],item['img']])
        #写入图片

        name = 'imgs/'+item['name']+'.jpg'
        url = item['img']

        head = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'sessionid=kuablyuuszx5dtbmqguatzxkc5t4ysvy',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        }

        sess = requests.Session()
        html = sess.post(url=url, headers=head)
        with open(name,'wb')as f:
            f.write(html.content)

        return item
