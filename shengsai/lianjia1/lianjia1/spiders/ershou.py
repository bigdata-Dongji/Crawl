# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.shengsai.lianjia1.lianjia1.items import Lianjia1Item

class ErshouSpider(scrapy.Spider):
    name = 'ershou'
    allowed_domains = ['zhuzhou.lianjia.com']
    # start_urls = ['https://zhuzhou.lianjia.com/ershoufang/pg2/']
    start_urls = [f'https://zhuzhou.lianjia.com/ershoufang/pg{i}/' for i in range(1,11)]

    def parse(self, response):
        div = response.xpath('//*[@class="sellListContent"]/li')
        for i in div:
            item = Lianjia1Item()
            xiaoqu1 = (i.xpath('./div/div[2]/div/a/text()').extract_first())
            xiaoqu2 = (i.xpath('./div/div[2]/div/a[2]/text()').extract_first())
            try:
                item['name'] = str(xiaoqu1 + '-' + xiaoqu2)       #小区名
            except: item['name'] =None
            guige = (i.xpath('./div/div[3]/div/text()').get())    #规格
            item['structure'] = guige.split(' | ')[0]   #房屋结构
            item['area'] = guige.split(' | ')[1]        #房屋面积
            item['floor'] = guige.split(' | ')[-2]      #楼层
            item['price'] = (i.xpath('./div/div[6]/div/span/text()').extract_first()) + '万' #价格
            # print(guige.split(' | '))
            # print(guige)
            # print(item)
            yield (item)


from scrapy.cmdline import execute
if __name__ == '__main__':
    execute(['scrapy', 'crawl', 'ershou','-o','house.csv'])