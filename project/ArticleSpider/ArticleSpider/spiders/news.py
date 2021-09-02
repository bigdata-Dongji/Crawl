# -*- coding: utf-8 -*-
# 采集来源：猎云网的上市公司栏目

import re
import time
import random
import scrapy
from urllib import parse
from scrapy import Request
from ArticleSpider.items import LieyunArticleItem
from ArticleSpider.utils import common
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals

class NewsSpider(scrapy.Spider):
    name = 'news'
    allowed_domains = ['lieyunwang.com']
    start_urls = ['http://zzw.hsmdb.com/iwin_zzbweb-webapp/info/v2/query/f10_company_profile?en_prod_code=600000.SS']
    

    #收集猎云网所有404的url以及404页面数
    handle_httpstatus_list = [404]

    def __init__(self, **kwargs):
        self.num = 1
        self.fail_urls = []
        dispatcher.connect(self.handle_spider_closed, signals.spider_closed)
        # 控制数量
        if self.num == 3200:
            exit()

    def handle_spider_closed(self, spider, reason):
        self.crawler.stats.set_value("failed_urls", ",".join(self.fail_urls))

    def parse(self, response):
        '''
        1.获取新闻列表页中的新闻url并交给scrapy进行下载后调用相应的解析方法
        2.获取下一页的url并交给scrapy进行下载，下载完成后交给parse继续跟进
        '''
        post_nodes=response.xpath('//div[@class="article-container"]/div')
        for post_node in post_nodes: # for循环里xpath语法前要加.否则只会取第一行
            image_url=post_node.xpath('.//a[@class="lyw-article-img pull-left"]/img/@data-src').extract_first("")
            if image_url.startswith("//"):
                image_url = "https:" + image_url
            post_url=post_node.xpath('.//h2[@class="lyw-article-title-h2"]/a/@href').extract_first("")
            yield Request(url=parse.urljoin(response.url, post_url), meta={"front_image_url": image_url},
                          callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url=response.xpath('//li[@class="next"]/a/@href').extract_first("")
        yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)

    def parse_detail(self,response):
        match_re = re.match(".*?(\d+)", response.url)
        if match_re:
            article_item = LieyunArticleItem()
            post_id = match_re.group(1)

            # 提取标题
            title=response.xpath('//h1[@class="lyw-article-title"]/text()').extract()[1].strip()
            # 提取标签，得到列表
            tag_list=response.xpath('//ul[@class="article-tags mb20 clearfix"]/li/a/text()').extract()
            tags = ','.join(tag_list)  # 因MySQL等数据库没有列表类型，故转为str字符串
            # 提取内容
            content=response.xpath('//div[@id="main-text-id"]').extract()[0]
            # 提取发布时间
            create_date=response.xpath('//span[@class="time"]/text()').extract()[0]



            article_item['title']=title
            article_item['create_date']=create_date
            article_item['tags']=tags
            article_item['url']=response.url  # 当前url链接
            article_item['content']=content
            if response.meta.get('front_image_url',''):
                article_item['front_image_url']=response.meta.get('front_image_url','')
            else:
                article_item['front_image_url'] =[]
            article_item['url_object_id']=common.get_md5(article_item['url'])

        print('正在爬取第 ',self.num,' 条')
        self.num+=1
        # 控制速度
        tr = random.uniform(0.4, 2.2)  # 生成0.4-2.2之间的随机小数
        time.sleep(tr)


        yield article_item