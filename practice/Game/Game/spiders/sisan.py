# -*- coding: utf-8 -*-
import scrapy
import re
from Game.items import GameItem

class SisanSpider(scrapy.Spider):
    name = 'sisan'
    allowed_domains = ['4399.com']
    urls = ['1','1_2','1_3']
    start_urls = ['http://www.4399.com/special/%s.htm'%i for i in urls]     #使用三元表达式实现翻页操作
    # start_urls = ['http://www.4399.com/special/1_2.htm']

    def parse(self, response):
        html = response.xpath('//div[@class="d_cen"]/ul/li')        #将4399小游戏的网页页面给xpath解析
        #/html/body/div[5]/ul[60]/li[1]/div/a
        for i in html:                  #将解析的数据循环，方便清洗数据
            item = GameItem()           #导入items的方法，定义键
            url = i.xpath('./div/a/@href').extract_first()
            if url[0] == "/":
                item['urls']="http://www.4399.com"+url      #将匹配的游戏链接赋值给一个键
            else:
                continue
            #获取游戏ID
            # id = url.split("/")
            # id1 = id[-1][:-4]
            # print(id1)
            yield scrapy.Request(       #使用scrapy返回游戏链接到下一个方法解析
                item["urls"],
                callback=self.parse_data,
                meta={"item":item["urls"]}      #将数据传入
            )
            # break

    def parse_data(self,response):      #将接收的网页链接给xpath解析数据
        item = {}
        try:
            html = response.xpath('//div[@class="intr-r"]')     #将数据进行匹配和清洗
            item["title"]=html.xpath('./div[1]/h1/a/text()').extract_first()
            item["fenlei"]=html.xpath('./div[2]/a/text()').extract_first()
            daxiao=html.xpath('./div[2]/text()').extract()
            dx=daxiao[-1].split("\xa0\xa0|\xa0\xa0")[1]     #将数据切割进行数据规范化
            item["daixao"]=dx.split("：")[1]
            date=daxiao[-1].split("\xa0\xa0|\xa0\xa0")[-1]
            item["date"]=date.split("：")[1]
            item["leixing"] = html.xpath('./div[3]/a/text()').extract()
            item["jieshao"] = html.xpath('./div[4]/div/font/text()').extract_first()
            item["url"] = response.meta["item"]
            print(item)
            yield item      #使用迭代器将键值对的数据返回，将返回的数据使用scrapy的命令进行保存
        except:
            pass
