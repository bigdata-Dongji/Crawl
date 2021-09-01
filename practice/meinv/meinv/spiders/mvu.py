# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.meinv.meinv.items import MeinvItem,MItem

class MvuSpider(scrapy.Spider):
    name = 'mvu'
    allowed_domains = ['plmm.com.cn']
    start_urls = ['https://www.plmm.com.cn/xinggan/']

    def parse(self, response):
        # print(response.text)
        html = response.xpath('/html/body/div[5]/div/div[2]/div[.]/div[.]/div/a')
        for i in html:
            item = {}
            item["url"]='https:'+i.xpath('img/@src').extract_first()
            item["name"] = i.xpath('img/@alt').extract_first()
            MeinvItem.name=item["name"]
            MeinvItem.url=item["url"]

            yield (item)

        fanye = response.xpath('//*[@id="npage"]/a/@href').extract_first()
        if fanye :
            yield scrapy.Request('https://www.plmm.com.cn'+fanye,callback=self.parse)
