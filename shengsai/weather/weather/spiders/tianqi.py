# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.省赛备赛练习.weather.weather.items import WeatherItem
import re

class TianqiSpider(scrapy.Spider):
    name = 'tianqi'
    allowed_domains = ['tianqi.com']
    start_urls = ['http://tianqi.com/']

    def parse(self, response):
        # print(response.text)
        #获取每个省份的链接
        data = response.xpath('//div[@class="tqqgsf"]/p/a/@href').getall()
        for i in data:
            # print(i)
            yield scrapy.Request(
                url=i,
                callback=self.get_city
            )
            # break

    def get_city(self,response):
        # print(response.url)
        # 获取省份每个市区30天天气的链接
        urls = response.xpath('//div[@class="mainWeather"]/ul/li')
        if urls == []:
            urls = response.xpath('//ul[@class="raweather760"]/li')
        for i in urls:
            item = WeatherItem()
            item['url'] = response.urljoin(i.xpath('./a/@href').get())+'30/'
            item['name'] = i.xpath('./a/h5/text()').get()
            if item['name'] is None :
                item['name'] = re.findall("var cityname = '(.*?)';",response.text)[0]
            # print(item)
            yield scrapy.Request(
                url=item['url'],
                callback=self.get_weather,
                meta={'item':item}
            )
            # break

    def get_weather(self,response):
        # print(item)
        datas = response.xpath('//div[@class="inleft"]/ul/li')
        for i in datas:
            itemss = response.meta['item']
            itemss['riqi'] = i.xpath('./a/div/span/text()').get()
            itemss['jujin'] = i.xpath('./a/div/span[2]/text()').get()
            itemss['tianqi'] = i.xpath('./a/div[3]/text()').get()
            wendu1 = i.xpath('./a/div[4]/span/text()').get()
            wendu2 = i.xpath('./a/div[4]/span[2]/text()').get()
            itemss['wendu'] = str(wendu1)+'~'+str(wendu2)+'℃'
            if itemss['jujin'] == None:
                continue
            print(itemss)
            yield (itemss)

            # break
