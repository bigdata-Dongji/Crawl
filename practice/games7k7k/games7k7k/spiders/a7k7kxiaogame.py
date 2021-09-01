# -*- coding: utf-8 -*-
import scrapy
from games7k7k.items import Games7K7KItem

class A7k7kxiaogameSpider(scrapy.Spider):
    name = '7k7kxiaogame'
    allowed_domains = ['7k7k.com']
    start_urls = ['http://www.7k7k.com/tag/134/index_1.htm']

    def parse(self, response):
        # print(response.text)
        html = response.xpath('//*[@id="theme-blue"]/div[3]/div[3]/div/div/ul')
        # html = response.xpath('//*[@id="theme-blue"]/div[3]/div[3]/div[1]/div/ul')
        for i in html:
            url = i.xpath('./li/a/@href').extract()
            for i in url:
                item = Games7K7KItem()
                item['game_url'] = i
                yield scrapy.Request(
                    item['game_url'],
                    callback=self.parse_data,
                    meta={"itme":item}
                )


    # def parse_comment(self,response):
    #     item = response.meta['itme']
    #     id = item['game_url'].split('/')
    #     id1 = id[-1].split('.')[0]
    #     'https://changyan.sohu.com/api/2/topic/count?client_id=cyqHvdkcp&topic_id=&topic_source_id=7k7kmainsite'+id1+'&topic_url=&callback=getCmtSum'



    def parse_data(self,response):
        item = response.meta["itme"]
        #获取游戏的标题
        item['game_name'] = response.xpath('//h1[@class="game_info_tit"]/text()').extract()
        #获取游戏的类型
        item['game_type'] = response.xpath('//*[@class="game_info_f1"]/span/a/text()').extract()
        #获取游戏的时间
        item['game_date'] = response.xpath('//*[@class="game_info_f1"]/span[2]/text()').extract()
        #获取游戏的大小
        item['game_size'] = response.xpath('//*[@class="game_info_f1"]/span[3]/text()').extract()
        print(item)
        yield (item)


