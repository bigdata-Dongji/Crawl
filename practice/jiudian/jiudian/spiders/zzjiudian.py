# -*- coding: utf-8 -*-
import scrapy
import json

class ZzjiudianSpider(scrapy.Spider):
    name = 'zzjiudian'
    allowed_domains = ['zhuzhou.meituan.com']
    start_urls = ['https://ihotel.meituan.com/hbsearch/HotelSearch?utm_medium=pc&version_name=999.9&cateId=20&attr_28=129&cityId=59&offset=0&limit=20&startDay=20191216&endDay=20191216']

    def parse(self, response):
        html = json.loads(response.text)
        for i in html['data']['searchresult']:
            print(i)
