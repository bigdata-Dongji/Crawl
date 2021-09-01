# -*- coding: utf-8 -*-
import scrapy
import json

class ZhaopinSpider(scrapy.Spider):
    name = 'zhaopin'
    allowed_domains = ['sou.zhaopin.com']
    start_urls = ['https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=749&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=Python&kt=3&=0&_v=0.60644065&x-zp-page-request-id=d8b80f83abb3409badc0b64551a09d3a-1574772249835-690663&x-zp-client-id=17cb1fd9-5e9d-4fe5-a36a-04f87a8e9f14&MmEwMD=45BCGtiCwteAFl6QhYBGKPW7FPJeiVqPBMMUZxBXvf1v81t_8odDJME50r20EFQIZTrYA90Rh9yn3WzBBB7nq_gAc6sOM8Mp2emnwzJoNIs8jjVqshu.poNvm.FdPi6YMGkS.FwIUpCOMZky5mAlYj9k.sNeudaKaAAPEasSRLf0l8Lek9U5wyXcXxvEANo1IL1ftr0wf.MRvDzYuGr.Wt6rY6ZAaPVomXC5pO18ZPtqzMCj4QlGK41ewbCVN0XGvjqlecQfnLBSCg8eZghAijguGsXJ6cHS.GxyNyBKXgJ1uhvlywaBmdlZLpCHXf2tg6OG5_iqzGEHGFg2c6m8iwdrjoRd2Oq9GJOgCrYSmLIAHHRuVB9Fm5xSfLjcw75r59dPXYLm7tPF8GZ5c7i7uzGNs']

    def parse(self, response):
        html = json.loads(response.text)
        for i in html["data"]["results"]:
            item = {}
            item["职位"] = i['jobName']
            item["公司"] = i['company']['name']
            item["网址"] = i['company']['url']
            item["时间"] = i['updateDate']
            item["工资"] = i['salary']
            item["学历"] = i['eduLevel']['name']
            try:
                item["经验"] = i['workingExp']['name']
            except:
                print("pass")
            item["待遇"] = i['welfare']
            print(item)
        #     print(datas)
