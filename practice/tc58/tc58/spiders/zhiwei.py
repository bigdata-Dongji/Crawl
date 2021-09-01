# -*- coding: utf-8 -*-
import scrapy


class ZhiweiSpider(scrapy.Spider):
    name = 'zhiwei'
    allowed_domains = ['zhuzhou.58.com']
    start_urls = ['https://zhuzhou.58.com/chengxuyuan/?PGTID=0d202408-0043-e6f3-7fba-feae542ff4bc&ClickID=2']

    def parse(self, response):
        print(response.text)
