# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.省赛备赛练习.imgs.imgs.items import ImgsItem

class TpSpider(scrapy.Spider):
    name = 'tp'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['http://sc.chinaz.com/tupian/',]

    def parse(self, response):
        div_list = response.xpath('//*[@id="container"]/div')
        for div in div_list:
            # 注意：使用伪属性
            img_src = div.xpath('./div/a/img/@src2').extract_first()
            # print(img_src)
            item = ImgsItem()
            item['img_src'] = "https:"+img_src
            # print(len(item))
            yield item
# 'https://scpic2.chinaz.net/Files/pic/pic9/202012/bpic22005_s.jpg'

from scrapy.cmdline import execute
execute(['scrapy','crawl','tp'])
