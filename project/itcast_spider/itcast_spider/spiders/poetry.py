# -*- coding: utf-8 -*-
import scrapy
'''
爬取古诗文
'''

class PoetrySpider(scrapy.Spider):
    name = 'poetry'
    allowed_domains = ['gushiwen.cn']
    start_urls = ['https://www.gushiwen.cn/default_1.aspx']

    def parse(self, response):
        li_list=response.xpath('//div[@class="sons"]')
        for li in li_list:
            item={}
            if len(li.xpath('.//a/b/text()')) > 0:
                item['title']=li.xpath('.//a/b/text()').extract_first()
                item['author']=li.xpath('.//p[@class="source"]/*/text()').extract_first()
                item['dynasty']=li.xpath('.//p[@class="source"]/*/text()').extract()[1] # 朝代
                item['content']=''.join(li.xpath('.//div[@class="contson"]//text()').getall()).strip()
                yield item
        # 找到下一页的url地址
        next_url=response.xpath('//*[@id="amore"]/@href').extract_first()
        if next_url!=None:
            next_url='https://www.gushiwen.cn/'+next_url
            yield scrapy.Request(next_url,callback=self.parse)