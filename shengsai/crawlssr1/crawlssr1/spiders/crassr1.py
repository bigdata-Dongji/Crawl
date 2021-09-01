# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from crawlssr1.items import Crawlssr1Item

class Crassr1Spider(CrawlSpider):
    name = 'crassr1'
    allowed_domains = ['ssr1.scrape.center']
    start_urls = ['https://ssr1.scrape.center/']

    rules = (
        Rule(LinkExtractor(allow=r'/detail/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'/page/\d+'), follow=True),
    )

    def parse_item(self, response):
        item = Crawlssr1Item()
        html = response
        item['name'] = html.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/a/h2/text()').extract_first()
        item['city'] = html.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[2]/span[1]/text()').extract_first()
        item['date'] = html.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[3]/span/text()').extract_first()
        item['jianjie'] = html.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[2]/div[4]/p/text()').extract_first().strip()
        item['score'] = html.xpath('//*[@id="detail"]/div[1]/div/div/div[1]/div/div[3]/p[1]/text()').extract_first().strip()
        item['daoyan'] = html.xpath('//*[@id="detail"]/div[2]/div/div/div/div/div/p/text()').extract_first()
        yield (item)

