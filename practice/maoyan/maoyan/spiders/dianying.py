# -*- coding: utf-8 -*-
import scrapy


class DianyingSpider(scrapy.Spider):
    name = 'dianying'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']       #将猫眼电影的连接传给方法parse

    def parse(self, response):
        html = response.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd') #获取猫眼的详情数据连接
        for i in html:
            item = {}
            item["url"] = i.xpath('./div/a/@href').extract()
            print(item)
