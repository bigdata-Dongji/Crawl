# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy框架.practice.CSDN.CSDN.items import CsdnItem

class CsdnblogsSpider(scrapy.Spider):
    name = 'csdnblogs'
    # allowed_domains = ['csdn.net']
    start_urls = ['https://www.csdn.net/api/articles?type=more&category=python&shown_offset=0']

    def start_requests(self):
        cookies = {
            'cookie':'uuid_tt_dd=10_19932723480-1568805481877-227076; UN=weixin_43863724; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=6525*1*10_19932723480-1568805481877-227076!5744*1*weixin_43863724!1788*1*PC_VC; smidV2=20191029192142c62db2507bc80bc0cebad8f98fad917700eda62a0b4115f00; UserName=weixin_43863724; UserInfo=b068726040384159a11b5372b9f995a9; UserToken=b068726040384159a11b5372b9f995a9; UserNick=%E5%BD%AD%E6%B6%9B%E6%B6%9B; AU=2B5; BT=1600849023964; p_uid=U010000; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%221%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22uid_%22%3A%7B%22value%22%3A%22weixin_43863724%22%2C%22scope%22%3A1%7D%7D; __gads=ID=74319cc733dbee2a-22cb4b984fc40003:T=1603283323:RT=1603283323:S=ALNI_Mb9UvUb8UoaQaWHhxxzfuz_lFLb3w; dc_session_id=10_1607153970191.208015; csrfToken=FQnjv-EEUFKqjMZnxO3lKgc8; c_first_ref=www.baidu.com; c_segment=4; c_ref=https%3A//www.baidu.com/link; dc_sid=d4432766e842152d2a81a1cafab77389; TY_SESSION_ID=f9024861-3fc6-4145-905f-2c0eb07ab64a; searchHistoryArray-new=%5B%22vue%22%2C%22%26%23x%22%2C%22%26%23xe%22%5D; firstDie=1; c_first_page=https%3A//blog.csdn.net/ahaotata/article/details/83931597; c_pref=https%3A//www.baidu.com/link; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1607000805,1607080984,1607153973,1607155271; log_Id_click=55; c_utm_medium=distribute.pc_category.none-task-blog-hot-14.nonecase; c_page_id=default; dc_tos=qkuwzy; log_Id_pv=346; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1607155343; log_Id_view=1234'
        }
        yield scrapy.FormRequest(
            self.start_urls[0],
            cookies=cookies,
            callback=self.parse
        )

    def parse(self, response):
        url = re.findall('"url":"(https:.*?)"',response.text)
        for i in url:
            item = CsdnItem()
            item['url'] = i.replace('\\','')
            # print(i.replace('/',''))
            yield scrapy.Request(
                url=item['url'],
                callback=self.data,
                meta={'item':item}
            )
            # break

    def data(self,response):
        item = response.meta['item']
        html = (response.text)
        # try:
        item['name'] = re.findall('<h1 class="title-article" id="articleContentId">(.*?)</h1>',html)[0]
        item['yuanchuang'] = re.findall('版权声明：本文为博主(.*?)，遵循',html)[0]
        item['date'] = re.findall('<span class="time">(\d+-\d+-\d+ \d+:\d+:\d+)</span>',html)[0]
        item['yuedu'] = re.findall('<span class="read-count">(.*?)</span>',html)[0]
        item['type'] =response.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[2]/div/a/text()').extract()
        item['biaoqian'] = response.xpath('//*[@id="mainBox"]/main/div[1]/div/div/div[2]/div[2]/div/a[2]/text()').extract()

        yield (item)
        # except:
        #     print(item)