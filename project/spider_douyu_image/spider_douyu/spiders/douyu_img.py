import scrapy,json
from spider_douyu.items import SpiderDouyuItem

class DouyuImgSpider(scrapy.Spider):
    name = 'douyu_img'
    allowed_domains = ['douyu.com']
    base_url='https://www.douyu.com/gapi/rknc/directory/yzRec/'
    offset=1
    start_urls = [base_url+str(offset)]

    def parse(self, response):
        data_li=json.loads(response.body).get('data').get('rl')
        if len(data_li)==0:
            print('数据长度为0')
            return
        item = SpiderDouyuItem()
        for data in data_li:

            item['name']=data['rn']
            item['image']=data['rs1']
            yield item
        self.offset+=1
        url=self.base_url+str(self.offset)
        yield scrapy.Request(url,callback=self.parse,dont_filter=True)