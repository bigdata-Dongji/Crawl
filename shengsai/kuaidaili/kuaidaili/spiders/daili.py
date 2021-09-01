# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy框架.省赛备赛练习.kuaidaili.kuaidaili.items import KuaidailiItem


class DailiSpider(CrawlSpider):
    name = 'daili'
    allowed_domains = ['kuaidailli.com']
    start_urls = [f'https://www.kuaidaili.com/free/inha/{i}/' for i in range(1,3782)]

    def start_requests(self):
        cookies = {
            "Cookie": "channelid=0; sid=1608084612894148; _ga=GA1.2.226409582.1608084614; _gid=GA1.2.2069245587.1608084614; sessionid=ae970a687ae26fb09e7ee98a384f5bba; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1608084614,1608084709; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1608084745"
        }
        for i in self.start_urls:
            yield scrapy.Request(
                url=i,
                cookies=cookies,
                callback=self.parse_item
            )

    def parse_item(self, response):
        data = response.xpath('//*[@class="table table-bordered table-striped"]/tbody/tr')
        for i in data:
            item = KuaidailiItem()
            item['ip']=(i.xpath('./td/text()').extract()[0])
            item['port']=(i.xpath('./td/text()').extract()[1])
            item['niming']=(i.xpath('./td/text()').extract()[2])
            item['type']=(i.xpath('./td/text()').extract()[3])
            item['city']=(i.xpath('./td/text()').extract()[4])
            item['sudu']=(i.xpath('./td/text()').extract()[5])
            item['date']=(i.xpath('./td/text()').extract()[6])
            print(item)



from scrapy.cmdline import execute
execute(['scrapy','crawl','daili'])

