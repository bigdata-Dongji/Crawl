# -*- coding: utf-8 -*-
import scrapy


class DongyeguiwuSpider(scrapy.Spider):
    name = 'dongyeguiwu'
    allowed_domains = ['search.dangdang.com']
    start_urls = ['http://search.dangdang.com/?key2=%B6%AB%D2%B0%B9%E7%CE%E1&medium=01&category_path=01.00.00.00.00.00']

    def parse(self, response):
        html = response.xpath('//ul[@class="bigimg"]/li[.]')    #将网页数据进行解析
        datas = {}  #定义字典，使匹配的数据键值对
        for i in html:
            datas["title"] = i.xpath('./a/@title').extract_first()
            datas["url"] = i.xpath('./a/@href').extract_first()
            datas["title_jianjie"] = i.xpath('./p[1]/a/@title').extract_first()
            datas["book_jianjie"] = i.xpath('./p[2]/text()').extract_first()
            datas["price"] = i.xpath('./p[3]/span[1]/text()').extract_first()
            datas["yuan_price"] = i.xpath('./p[3]/span[2]/text()').extract_first()
            datas["dianzibook_price"] = i.xpath('./p[3]/a/i/text()').extract_first()
            datas["pinglun"] = i.xpath('./p[4]/a/text()').extract_first()
            datas["zuozhe"] = i.xpath('./p[5]/span[1]/a[1]/text()').extract_first()
            datas["time"] = i.xpath('./p[5]/span[2]/text()').extract_first()
            datas["chubangongsi"] = i.xpath('./p[5]/span[3]/a/text()').extract_first()
        yield (datas)       #使用迭代器将数据返回给pipelines

        nex_url = response.xpath('//*[@id="12810"]/div[5]/div[2]/div/ul/li[10]/a/@href').extract_first()    #获取下一页的按钮链接
        print(nex_url)
        if nex_url != " ":          #判断是否有下一页
            urls = "http://search.dangdang.com/" + nex_url
            yield scrapy.Request(
                urls,
                callback=self.parse,        #将链接返回给parse进行匹配数据
            )