# -*- coding: utf-8 -*-
import scrapy


class StarSpider(scrapy.Spider):
    name = 'star'
    allowed_domains = ['spa11.scrape']
    start_urls = ['https://spa11.scrape.center/']

    # def start_requests(self):
    #
    #     yield scrapy.Request(
    #         url=self.start_urls[0],
    #         callback=self.parse,
    #         cookies=
    #     )


    def parse(self, response):
        pass
