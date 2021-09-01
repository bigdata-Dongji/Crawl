# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy框架.shengsai.qichezhijia.qichezhijia.items import QichezhijiaItem

class QcSpider(scrapy.Spider):
    name = 'qc'
    allowed_domains = ['car.autohome.com.cn']
    start_urls = [f'https://car.autohome.com.cn/diandongche/list-25_35-0-0-1-0-0-0-0-{i}.html' for i in range(1,4)]

    def parse(self, response):
        html = (response.text)
        # print(html)
        name = re.findall('<div id=.*?ass="main-title"><a href=.*?get="_self" class="font-bold">(.*?)</a>',html)
        km = re.findall('<li>续航里程：<span class="info-gray">(.*?)</span></li>',html)
        price = re.findall('<span class="lever-price red"><span class="font-arial">(.*?)</span>',html)
        colors = response.xpath('//*[@id="brandtab-1"]/div/div/div[2]')
        a = 0
        for i in colors:
            item = QichezhijiaItem()
            item['name'] = (name[a])
            item['scorce'] = (i.xpath('./div/div/a/span/text()').get())
            item['km'] = (km[a])
            item['price'] = (price[a])
            item['color'] = "，".join(i.xpath('./div[2]/div[1]/ul/li[5]/div[2]/a/div/div/text()').getall())
            a +=1
            yield item



from scrapy.cmdline import execute
execute(['scrapy','crawl','qc','-o','FEED_EXPORT_FILEDS_cars.csv'])

