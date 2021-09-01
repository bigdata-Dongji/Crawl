# -*- coding: utf-8 -*-
import scrapy


class BaidutiebaSpider(scrapy.Spider):
    name = 'baidutieba'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://search.dangdang.com/?key2=%B6%AB%D2%B0%B9%E7%CE%E1&medium=01&category_path=01.00.00.00.00.00']

    def parse(self, response):
        # css获取这个网页这个层的所有数据
        html = response.css('#component_59')
        for i in html:
            print(i.css('.pic ::attr(title)').extract(),end="     ")
            print(i.css('.pic ::attr(href)').extract())
        htmls = response.xpath('//ul[@class="bigimg"]/li[.]')
        for i in htmls:
            print(i.xpath('./a/@title').extract_first())
            print(i.xpath('./a/@href').extract_first())