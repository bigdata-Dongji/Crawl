import scrapy


class QingganSpider(scrapy.Spider):
    name = 'qinggan'
    base_url='https://ke.qq.com/course/list/%E6%83%85%E6%84%9F?page='
    page=1

    def start_requests(self):
        url=self.base_url+str(self.page)
        yield scrapy.Request(url,self.parse)
    def parse(self, response):

        for i in range(24):
            name=response.xpath(f'//li[@data-report-position="{i+1}"]//h4/a/@title').get()
            price=response.xpath(f'//li[@data-report-position="{i+1}"]//span[@class="line-cell item-price  custom-string"]/text()').get().replace('¥','')
            people=response.xpath(f'//li[@data-report-position="{i+1}"]//span[@class="line-cell item-user custom-string"]/text()').get().strip().split('人')[0]
            print(name)
            print(price)
            print(people)
            with open('data.csv','a',encoding='utf8')as f:
                f.write(f'{name},{price},{people}\n')
        self.page+=1
        url = self.base_url + str(self.page)
        yield scrapy.Request(url, self.parse)

from scrapy.cmdline import execute
execute('scrapy crawl qinggan'.split())
