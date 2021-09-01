# -*- coding: utf-8 -*-
import scrapy


class Top100Spider(scrapy.Spider):
    name = 'top100'
    allowed_domains = ['maoyan.com']
    #for i in range(0,11):
    start_urls = ["https://maoyan.com/board/4?offset=%s"%i for i in range(0,101,10)]    #使用三元表达式进行网页的翻页操作

    def parse(self, response):
        # print(response.text)
        item = {}
        urls = response.xpath('//dl[@class="board-wrapper"]/dd[.]')         #将数据进行解析
        # //*[@id="app"]/div/div/div/dl/dd[.]/a
        pj = 'https://maoyan.com/'              #将网页链接定义，方便下面数据进行拼接
        for i in urls:
            item["href"] = pj + i.xpath('./a/@href').extract_first()        #拼接网页链接
            item["title"] = i.xpath('./a/@title').extract_first()           #获取数据的标题等内容
            item["daoyan"] = i.xpath('./div/div/div/p[2]/text()').extract_first().replace("\n","").replace(" ","")  #将数据进行简单的清洗使数据规范化
            item["time"] = i.xpath('./div/div/div/p[3]/text()').extract_first()
            yield item      #使用迭代器进行数据的返回