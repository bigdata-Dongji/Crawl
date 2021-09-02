import scrapy
from spider_star.items import SpiderStarItem
import time

class StarImageSpider(scrapy.Spider):
    name = 'star_image'
    allowed_domains = ['win4000.com']
    start_urls = ['http://www.win4000.com/mt/index.html']

    def parse(self, response):
        time.sleep(1)
        li=response.xpath('//*[@class="Left_bar"]//li')
        for i in li:
            images_url=i.xpath('./a/@href').get()
            name=i.xpath('./a/p/text()').get()
            item=SpiderStarItem(images_url=images_url,name=name)
            yield scrapy.Request(url=images_url,callback=self.parse_detail,meta={'item':item})

        next_page=response.xpath('//a[@class="next"]/@href').get()
        yield scrapy.Request(next_page,self.parse,dont_filter=True)
    def parse_detail(self,response):
        time.sleep(1)
        introduction=response.xpath('//*[@class="intro_p"]/p/text()').get()
        images=response.xpath('//div[@class="tab_box"]//li/a/img/@data-src').getall()
        item=response.meta['item']
        item['introduction']=introduction
        item['images']=images
        yield item