# -*- coding: utf-8 -*-
import scrapy
from GAME7k7k.items import Game7K7KItem

class GamekkSpider(scrapy.Spider):
    name = 'gamekk'
    allowed_domains = ['7k7k.com']
    # start_urls = ['https://maoyan.com/board/4?offset='+str(i) for i in range(0,91,10)]
    start_urls = ['http://www.7k7k.com/tag/134/index_1.htm#p-anchor']
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko",
    }

    def parse(self, response):
        html = response.xpath('//*[@id="theme-blue"]/div[3]/div[3]/div[1]/div/ul')
        item = Game7K7KItem()
        for i in html:
            url = i.xpath('./li/a/@href')
            print(url)
            for j in url:
                item['url'] = j
                yield scrapy.Request(
                    url = item['url'],
                    callback = self.getdata,
                    meta={'item':item},
                    headers=self.head
                )
                break
    #
    # #
    def getdata(self,response):
        item = response.meta['item']
        item['name'] = response.xpath('//*[@id="theme-blue"]/div[2]/div[3]/div[1]/div[1]/div[1]/div[2]/a/h1/text()').extract()[0]
        item['jianjie'] = response.xpath('//*[@id="theme-blue"]/div[2]/div[3]/div[1]/div[1]/div[2]/text()').extract()[0].replace('\n','').strip()
        yield (item)



