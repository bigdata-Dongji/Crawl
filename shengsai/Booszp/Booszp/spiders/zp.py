# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.省赛备赛练习.Booszp.Booszp.items import BooszpItem

class ZpSpider(scrapy.Spider):
    name = 'zp'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101250100/?query=Python&page=1']

    def start_requests(self):
        headers = {
            "cookie": "_bl_uid=FFkORgvsjp7amhwXCp7a0s71nqyh; lastCity=101250100; sid=sem_pz_bdpc_dasou_title; __g=sem_pz_bdpc_dasou_title; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1608033138; wt2=CGgHnnurFM5FoBGh; __zp_seo_uuid__=9106b059-a6b6-4bac-87ef-27e31b6ae024; __c=1608033138; __l=r=&l=%2Fwww.zhipin.com%2Fc101250100%2F%3Fquery%3DPython%26page%3D1&s=3&friend_source=0&s=3&friend_source=0; __a=95969062.1575029172.1604303712.1608033138.132.14.30.30; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1608039599; __zp_stoken__=2fb1bJHwfQDpxd30oJnlWZmogQ1U8MS93T0FLMllhaWYPcwRHeRRYLjw1H0IhQBQLT3t0SWA1azEhJAwPOU4RDS0cSAM6PHgua1M3bGRlI3MNdxEEYWkOSSJDcFsADygJSSp%2BWiA%2FOE5UWEFsNA%3D%3D",
        }
        url = self.start_urls[0]
        yield scrapy.Request(
            url=url,
            cookies=headers,
            callback=self.parse

        )

    def parse(self, response):
        print(response.text)
        # html = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        # for i in html:
        #     item = BooszpItem()
        #     item['name']=(i.xpath('.//div[@class="job-title"]/span/a/text()'))  # 职位
            # item['position']=(i.xpath('.//span[@class="job-area-wrapper"]/span[1]/text()')[0])  # 地址
            # item['site']=(i.xpath('.//span[@class="job-pub-time"]/text()')[0])  # 发布时间
            # item['date']=(i.xpath('.//div[@class="job-limit clearfix"]/span/text()')[0])  # 薪资
            # item['pay']=(','.join(i.xpath('.//div[@class="job-limit clearfix"]/p/text()'))[0])  # 工作经验
            # item['experience']=(','.join(i.xpath('.//div[@class="job-limit clearfix"]/p/text()'))[1])  # 学历要求
            # item['company']=(i.xpath('.//div[@class="info-company"]/div/h3/a/text()')[0])  # 公司名称
            # item['company_type']=(i.xpath('.//div[@class="info-company"]/div/p/a/text()')[0])  # 公司类型
            # item['financing']=(','.join(i.xpath('.//div[@class="info-company"]/div/p/a/text()'))[0])  # 融资类型
            # item['number_of_people']=(','.join(i.xpath('.//div[@class="info-company"]/div/p/a/text()'))[1])  # 企业规模类型
            # item['technology']=(','.join(i.xpath('.//div[@class="info-append clearfix"]/div/span/text()')))  # 技术手段
            # item['welfare']=(i.xpath('.//div[@class="info-append clearfix"]/div[2]/span/text()'))  # 员工福利
            # print(item)
        # pass

from scrapy.cmdline import execute
execute(['scrapy','crawl','zp'])