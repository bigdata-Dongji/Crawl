import scrapy,time,json,re
from scrapy import Request
from chinahr.items import ChinahrItem

class JobSpider(scrapy.Spider):
    name = 'job'
    allowed_domains = ['www.chinahr.com']
    start_urls = ['http://search.chinahr.com/sh/job/?key=%E5%89%8D%E7%AB%AF']

    def parse(self, response):
        job_list=response.xpath('//div[@class="jobList pc_search_listclick"]/@data-detail').getall()
        json_data = re.findall('____json4fe = .*?({"dispid":".*?","name":".*?","listname":".*?"}).*?;', response.text, re.S)[0]
        city = json.loads(json_data).get('name')
        for i in job_list:
            time.sleep(3)
            yield Request(i,self.get_detail,dont_filter=True,meta={'city':city})
        next_page=response.xpath('//*[@class="page-next"]/@href').get()
        yield Request(next_page,self.parse,dont_filter=True)


    def get_detail(self,response):
        item=ChinahrItem()


        name = response.xpath('//h1/text()').get()
        salary = response.xpath('//span[@class="job_salary"]/text()').get()
        job_addr = response.xpath('//span[@class="job_addr"]/text()').get()
        try:
            exp = job_addr.split('|')[1].strip()
        except:
            exp=''
        try:
            edu = job_addr.split('|')[2].strip()
        except:
            edu=''
        try:
            demand = job_addr.split('|')[3].strip()
        except:
            demand = ''
        try:
            classification = job_addr.split('|')[4].strip()
        except:
            classification = ''
        treatment = response.xpath('//div[@class="job_left"]/div[2]/span/text()').getall()
        treatment=''.join(treatment)
        time = response.xpath('//div[@class="job_left"]/div[4]/span/text()').get()
        detail = response.xpath('//div[@class="desc_text"]/text()').getall()
        detail=''.join(detail)

        com_name = response.xpath('//span[@class="job_enterprisename"]/@title').get()
        address = response.xpath('//div[@class="job_left"]/div[3]/span/text()').get()
        type_list = response.xpath('//span[@class="job_enterprisetype"]/text()').get()
        try:
            industry = type_list.split('|')[0].strip()
        except:
            industry=''
        try:
            people_num = type_list.split('|')[1].strip()
        except:
            people_num=''
        introduce = response.xpath('//div[@class="details_text"]/text()').getall()
        introduce=''.join(introduce)

        item['name']=name
        item['salary']=salary
        item['exp']=exp
        item['edu']=edu
        item['demand']=demand
        item['classification']=classification
        item['treatment']=treatment
        item['time']=time
        item['detail']=detail
        item['com_name']=com_name
        item['address']=address
        item['industry']=industry
        item['people_num']=people_num
        item['introduce']=introduce
        item['city']=response.meta['city']

        yield item