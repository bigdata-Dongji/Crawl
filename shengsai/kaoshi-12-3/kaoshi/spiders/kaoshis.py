# -*- coding: utf-8 -*-
import scrapy
import requests
import re

class KaoshisSpider(scrapy.Spider):
    name = 'kaoshis'
    allowed_domains = ['ogin2.scrape']
    start_urls = ['https://login2.scrape.center/page/'+str(i) for i in range(1,11)]

    def parse(self, response):

        # url = 'https://login2.scrape.center/login?next=/'
        data = {
            "username": "admin",
            "password": "admin"
        }
        head = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'Cookie': 'sessionid=kuablyuuszx5dtbmqguatzxkc5t4ysvy',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.183 Safari/537.36',
        }
        sess = requests.Session()
        html = sess.post(url=response.url, headers=head, data=data).text
        name = re.findall('class="m-b-sm">(.*?)</h2>', html)
        city = re.findall('<spa.*?="">(.*?国.*?)</span>', html)
        date = re.findall('>(.*?) 上映</span>', html)
        score = re.findall('class="score m-t-md m-b-n-sm">(.*?)</p>', html, re.S)
        img = re.findall('src="(https://p.*?)"', html)
        if len(date) != 10:
            date.append('None')
        for i in range(len(name)):
            item = {}
            item['name'] = name[i]
            item['city'] = city[i]
            item['date'] = date[i]
            item['score'] = score[i].strip()
            item['img'] = img[i]
            yield (item)