# -*- coding: utf-8 -*-
import scrapy


class DatasSpider(scrapy.Spider):
    name = 'datas'
    allowed_domains = ['move.douban.com']
    start_urls = ['https://movie.douban.com/top250?start='+str(i)+'&filter=' for i in range(0,226,25)]

    def parse(self, response):
        datas = response.xpath('//div[@class="article"]/ol/li[.]')
        for i in datas:
            print(i)
            data = {}
            data['urls'] = i.xpath('./div/div[2]/div/a/@href').extract_first()
            data['daoyan'] = i.xpath('./div/div[2]/div[2]/p[1]').extract_first().replace("\n","").replace(" ","").replace("\xa0/\xa0","").replace("\xa0\xa0\xa0","")
            data['pingfeng'] = i.xpath('./div/div[2]/div[2]/div/span[@class="rating_num"]/text()').extract_first()
            data['pingjia'] = i.xpath('./div/div[2]/div[2]/div/span[4]/text()').extract_first()
            data['jianjie'] = i.xpath('./div/div[2]/div[2]/p[2]/span/text()').extract_first()
            yield (data)
