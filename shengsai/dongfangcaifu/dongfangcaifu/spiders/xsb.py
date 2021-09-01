# -*- coding: utf-8 -*-
import scrapy
import json
from scrapy框架.shengsai.dongfangcaifu.dongfangcaifu.items import DongfangcaifuItem


class XsbSpider(scrapy.Spider):
    name = 'xsb'
    allowed_domains = ['eastmoney.com']
    start_urls = [
        f'http://59.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403962123528009196_1608690160254&pn={i}&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111&_=1608690160255' for i in range(1,3)]

    def parse(self, response):
        html = response.text.replace('jQuery112403962123528009196_1608690160254(', '').replace(');', '')
        htmls = json.loads(html)
        id = 1
        for i in htmls['data']['diff']:
            item = DongfangcaifuItem()
            item['id'] = id
            item['dm'] = str(i['f12'])
            item['name'] = str(i['f14'])
            item['zxj'] = str(i['f2'])
            item['zde'] = str(i['f4'])
            item['zdf'] = str(i['f3'])+'%'
            item['cjl'] = str(i['f5'])
            item['cje'] = str(i['f6'])+'万'
            item['zs'] = str(i['f18'])
            item['jk'] = str(i['f17'])
            item['zg'] = str(i['f15'])
            item['zd'] = str(i['f16'])
            item['wb'] = str(i['f33'])+'%'
            id +=1
            yield item


'''
http://59.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403962123528009196_1608690160254&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111&_=1608690160255
http://59.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403962123528009196_1608690160254&pn=1&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111&_=1608690160255
http://59.push2.eastmoney.com/api/qt/clist/get?cb=jQuery112403962123528009196_1608690160254&pn=2&pz=20&po=1&np=1&ut=bd1d9ddb04089700cf9c27f6f7426281&fltt=2&invt=2&fid=f3&fs=m:0+t:81+s:2048&fields=f1,f2,f3,f4,f5,f6,f7,f8,f9,f10,f12,f13,f14,f15,f16,f17,f18,f20,f21,f23,f24,f25,f26,f22,f33,f11,f62,f128,f136,f115,f152,f111&_=1608690160318
'''
#
# from scrapy.cmdline import execute
# execute(['scrapy', 'crawl', 'xsb','-o','video.csv'])