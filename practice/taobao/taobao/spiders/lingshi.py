# -*- coding: utf-8 -*-
import scrapy


class LingshiSpider(scrapy.Spider):
    name = 'lingshi'
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://detail.tmall.com/item.htm?id=588339707188&ali_refid=a3_430583_1006:1103221025:N:LO74Bc2EWLnfvdjOI7AADg==:c202abff1faf4968a38bf870ca04fab6&ali_trackid=1_c202abff1faf4968a38bf870ca04fab6&spm=a230r.1.14.1']

    def parse(self, response):
        print(response.text)
