# -*- coding: utf-8 -*-
import scrapy
import logging

logger=logging.getLogger(__name__)

class LogDemoSpider(scrapy.Spider):
    name = 'log_demo'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://itcast.cn/']

    def parse(self, response):

        for i in range(10):
            item={}
            item['com_from']='itcast'
            logger.warning(item)
            yield item
