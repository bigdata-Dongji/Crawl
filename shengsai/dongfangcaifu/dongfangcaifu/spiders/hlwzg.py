# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy框架.shengsai.dongfangcaifu.dongfangcaifu.items import HLWZGItem

class HlwzgSpider(scrapy.Spider):
    name = 'hlwzg'
    allowed_domains = ['eastmoney.com']
    start_urls = [f'http://51.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112409968066107539744_1608693243313&pn={i}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=b:MK0202&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152&_=1608693243314' for i in range(1,3)]

    def parse(self, response):
        html = response.text.replace('jQuery112409968066107539744_1608693243313(', '').replace(');', '')
        htmls = json.loads(html)
        id = 1
        for i in htmls['data']['diff']:
            # print(i)
            item = HLWZGItem()
            item['id'] = id
            item['name'] = str(i['f14'])
            item['zxj'] = str(i['f2'])
            item['zde'] = str(i['f4'])
            item['zdf'] = str(i['f3'])+'%'
            item['kpj'] = str(i['f17'])
            item['zgj'] = str(i['f15'])
            item['zdj'] = str(i['f16'])
            item['zsj'] = str(i['f18'])
            item['zsz'] = str(i['f20'])+'亿'
            item['syl'] = str(i['f115'])
            id += 1
            # print(item)
            yield item
            # print(str(i['f17']),str(i['f15']),str(i['f16']),str(i['f18']),str(i['f20'])+'亿',str(i['f115']))


from scrapy.cmdline import execute
execute(['scrapy','crawl','hlwzg','-o','hlwzg.json','-s','FEED_EXPORT_ENCODING=utf-8'])
# execute(['scrapy','crawl','hlwzg'])
