# encoding:utf8
'''
source:https://segmentfault.com/blogs
'''
from scrapy import Request
from urllib import parse
import re

import scrapy
from hq_search.items import itBlogItem
class ItBlogSpider(scrapy.Spider):
    name = 'it_blog'
    # allowed_domains = ['https://segmentfault.com/']
    start_urls = ['https://segmentfault.com/blogs']
    # id=0

    def parse(self, response):

        '''
        1.获取列表页中的url并交给scrapy进行下载后调用相应的解析方法
        2.获取下一页的urL并交给scrapy进行下载， 下载完成后交给parse继续跟进
        '''
        li=response.xpath('//div[@class="summary"]')

        for i in li[:2]:
            # self.id+=1
            # print('正在爬取第 {} 条数据'.format(self.id))
            url=i.xpath('.//a/@href').extract_first()
            author=i.xpath('//ul[@class="author list-inline"]/li/span/a[1]/text()').extract_first() # 作者
            publisher=i.xpath('//ul[@class="author list-inline"]/li/span/a[2]/text()').extract_first() # 发布专栏
            judge=i.xpath('./h2/@class').extract_first().split()[-1] # 判断是否原创，还是转载
            if judge=='blog-type-1':
                blog_type='原创'
            else:
                blog_type = '转载'
            yield Request(url=parse.urljoin(response.url,url),
                          meta={'author':author,'publisher':publisher,'blog_type':blog_type},
                          callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        # next_url=response.xpath('//li[@class="next page-item"]/a/@href').extract_first()
        # yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)

    def parse_detail(self,response):
        blog_item=itBlogItem()

        # 标题
        title=response.xpath('//h1[@id="sf-article_title"]/a/text()').extract_first()
        # 发布时间
        release_time=response.xpath('//time[@class="text-secondary ml-2"]/text()').extract_first().split()[1]
        # 内容
        content=response.xpath('//article[@class="article fmt article-content"]').extract_first()
        # 标签
        tags=[i.strip() for i in response.xpath('//div[@class="m-n1"]/a/text()').extract() if i.strip() != '']
        tags=','.join(tags)
        # 点赞数
        likes=re.findall('<script>.*?votes: (\d+),.*?</script>',response.text,re.S)[0]
        # 收藏数
        collection=re.findall('<script>.*?bookmarks: (\d+),.*?</script>',response.text,re.S)[0]
        # 阅读量
        reading=response.xpath('//div[@id="sf-article_metas"]/@data-viewsword').extract_first()
        # 更新时间
        update_time=''.join(response.xpath('//time[@itemprop="datePublished"]/text()').extract()[1].split())

        # blog_item['id'] = response.meta.get('id', '')
        blog_item['title']=title
        blog_item['blog_url']=response.url
        blog_item['author']=response.meta.get('author','')
        blog_item['publisher']=response.meta.get('publisher','')
        blog_item['blog_type']=response.meta.get('blog_type','')
        blog_item['release_time']=release_time
        blog_item['tags']=tags
        blog_item['likes']=likes
        blog_item['collection']=collection
        blog_item['reading']=reading
        blog_item['update_time']=update_time
        blog_item['content']=content

        yield blog_item

