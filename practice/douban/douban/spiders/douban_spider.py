# -*- coding: utf-8 -*-
import scrapy
from douban.items import DoubanItem
class DoubanSpiderSpider(scrapy.Spider):
    #爬虫名称
    name = 'douban_spider'
    #爬虫允许抓取的域名
    allowed_domains = ['movie.douban.com']
    #爬虫抓取数据地址
    start_urls = ['http://movie.douban.com/top250']
    # print(1)

    def parse(self, response):
        # print(1)
        # print(response.text)
        # // *[ @ id = "content"] / div / div[1] / ol / li[1]
        #获取主要div层的数据
        movie_list = response.xpath("//div[@class='article']//ol[@class='grid_view']/li")
        for i_item in movie_list:           #将主要数据进行循环获取所需要的数据
            douban_item = DoubanItem()      #启用导入的items
            douban_item['serial_number']=i_item.xpath(".//div[@class='item']//em/text()").extract_first()       #获取电影排名
            douban_item['movie_name']=i_item.xpath(".//div[@class='info']/div[@class='hd']/a/span[1]/text()").extract_first()       #获取电影的名字
            # // *[ @ id = "content"] / div / div[1] / ol / li[1] / div / div[2] / div[2] / p[1] / text()[1]
            # // *[ @ id = "content"] / div / div[1] / ol / li[1] / div / div[2] / div[2] / p[1] / text()[2]
            # descs = i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()").extract()
            # for i_desc in descs:
            #     i_desc_str = "".join(i_desc.split())
            #     print(i_desc_str)
            #     douban_item['introduce'] = i_desc_str
            actions= i_item.xpath(".//div[@class='info']//div[@class='bd']/p[1]/text()[1]").extract_first()        #xpath获取导演数据
            douban_item['action'] = actions.split()         #将导演数据进行清洗
            douban_item['star'] = i_item.xpath(".//span[@class='rating_num']/text()").extract_first()   #获取电影评分
            douban_item['evaluate'] = i_item.xpath(".//div[@class='star']//span[4]/text()").extract_first() #获取电影评价
            douban_item['describle'] = i_item.xpath(".//p[@class='quote']/span/text()").extract_first()   #获取简介
            yield douban_item

        # 解析下一页
        next_link = response.xpath("//span[@class='next']/link/@href").extract()
        if next_link:       #判断是否有下一页的连接
            next_link = next_link[0]
            yield scrapy.Request("https://movie.douban.com/top250" + next_link, callback=self.parse)    #将下一页的网站返回给parse重新解析

