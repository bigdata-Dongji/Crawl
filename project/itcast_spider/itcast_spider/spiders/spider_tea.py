# encoding:utf8
import scrapy
'''
爬取 传智播客-黑马程序员 师资库
'''

class SpiderTeaSpider(scrapy.Spider):
    name = 'spider_tea' # 爬虫名
    allowed_domains = ['itcast.cn'] # 允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']  # 最开始请求的url地址

    def parse(self, response):
        # 处理start_urls地址对应的响应
        # name=response.xpath('//div[@class="tea_con"]//h3/text()').extract()
        # print(name)

        # 分组
        li_list=response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item={}
            item['name']=li.xpath('.//h3/text()').extract_first()
            # extract_first()方法获取不到数据时会返回None值，所以更推荐extract_first()代替extract()[0]
            # item['title']=li.xpath('.//h4/text()').extract()[0]
            item['title']=li.xpath('.//h4/text()').extract_first()
            # print(item)
            # yield方法将数据传送到pipelines里，yield方法可以减少内存的占用
            yield item