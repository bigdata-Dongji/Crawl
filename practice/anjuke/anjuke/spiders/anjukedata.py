# -*- coding: utf-8 -*-
import scrapy
from anjuke.items import AnjukeItem

class AnjukedataSpider(scrapy.Spider):
    name = 'anjukedata'
    allowed_domains = ['guangzhou.anjuke.com']
    start_urls = ['http://movie.douban.com/top250']

    def parse(self, response):
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        # hous_data = response.xpath('//*[@id="houselist-mod-new"]/li/div[2]/div[1]/a/text()')
        # print(hous_data)
        for i in movie_list:
            print(i)
            # anjuke_items = AnjukeItem()
            # anjuke_items["title"] = i.xpath('./div[2]/div/a/text()').extract.first()
        # pass
        #     yield scrapy.FormRequest(
        #         url=i,
        #         headers=head,
        #         formdata=lsd,
        #         meta=meta,
        #         callback=self.parse,
        #         cookies=cookies,
        #
        #     )
