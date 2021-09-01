# -*- coding: utf-8 -*-
import scrapy
from gushi.items import GushiItem

class GushiciSpider(scrapy.Spider):
    name = 'gushici'
    allowed_domains = ['jingyan.baidu.com']
    start_urls = ['https://baijiahao.baidu.com/s?id=1640221965214606832&wfr=spider&for=pc']

    def parse(self, response):
        html = response.xpath('//div[@class="article-content"]/p')  #将数据进行解析
        item = GushiItem()          #调用items
        for i in html:
            # print(i.xpath('./span/text()').extract_first())
            item["data"] = i.xpath('./span/text()').extract_first() #将数据进行匹配
            yield (item)        #使用迭代器将数据返回

