# -*- coding: utf-8 -*-
import scrapy


class HuxiuzixunSpider(scrapy.Spider):
    name = 'huxiuzixun'
    allowed_domains = ['huxiu.com']
    start_urls = ['http://huxiu.com/']

    def parse(self, response):
        # print(response.text)
        xp = response.xpath('//*[@id="topLeft"]/div[3]/div[2]')
        for i in xp:
            print(i)