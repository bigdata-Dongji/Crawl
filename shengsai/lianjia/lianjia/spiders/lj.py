# -*- coding: utf-8 -*-
import scrapy
from scrapy.cmdline import execute
from scrapy框架.shengsai.lianjia.lianjia.items import LianjiaItem

class LjSpider(scrapy.Spider):
    name = 'lj'
    allowed_domains = ['lianjia.com']
    start_urls = [f'https://bj.lianjia.com/ershoufang/pg{str(i)}/' for i in range(1,101)]

    def parse(self, response):
        div = response.xpath('//*[@class="sellListContent"]/li')
        for i in div:
            item = LianjiaItem()
            item['name'] = (i.xpath('./div/div/a/text()').extract_first())
            xiaoqu1 = (i.xpath('./div/div[2]/div/a/text()').extract_first())
            xiaoqu2 = (i.xpath('./div/div[2]/div/a[2]/text()').extract_first())
            item['xiaoqu'] = str(xiaoqu1+'-'+xiaoqu2)
            item['guige'] = (i.xpath('./div/div[3]/div/text()').extract_first())
            item['fabu'] = (i.xpath('./div/div[4]/text()').extract_first())
            item['biaoqian'] = (i.xpath('./div/div[5]/span/text()').extract())
            item['price'] = (i.xpath('./div/div[6]/div/span/text()').extract_first())+'万'
            item['danjia'] = (i.xpath('./div/div[6]/div[2]/span/text()').extract_first())
            item['url'] = (i.xpath('./a/@href').extract_first())
            print(item)
            yield (item)


if __name__ == '__main__':
    execute(['scrapy','crawl','lj'])