# -*- coding: utf-8 -*-
import scrapy


class ShumaSpider(scrapy.Spider):
    name = 'shuma'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/']

    def parse(self, response):
        pass
