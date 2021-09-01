# -*- coding: utf-8 -*-
import scrapy
import re
from lianxi.items import LianxiItem
class FangziSpider(scrapy.Spider):
    name = 'fangzi'
    allowed_domains = ['zhuzhou.anjuke.com']

    start_urls = ['https://zhuzhou.anjuke.com/sale/p%s/?pi=baidu-cpc-zhuzhou-tyong2&kwid=90923917378#filtersort'%i for i in range(1,51)]

    def parse(self, response):
        html = (response.text)
        dizhi = re.compile('<a data-from="" data-company=""  title="(.*?)" href=".*?".*?ss="details-item.*?an>(.*?)</spa.*?pan>(.*?)</span.*?le="(.*?)".*?src=".*?trong>(.*?)</strong>(.*?)</span><span class="unit-price">(.*?)</span>',re.S)
        data = re.findall(dizhi, html)
        for i in data:
            item = {}
            item["name"] = i[0]
            item['guige'] = i[1]
            item['mainji'] = i[2]
            datas = i[3].split('&nbsp;&nbsp;')
            item['dizhi'] = datas[0]
            item['luduan'] = datas[1]
            item['jiage'] = i[-3] + i[-2]
            item['danjia'] = i[-1]
            yield (item)
            # print(item)