# -*- coding: utf-8 -*-
import scrapy
from maoyan.items import MaoyanItem
import json
from datetime import datetime
import pandas as pd
#猫眼数据：1-23疫情前,7.20疫情后

class MaoyanSpiderSpider(scrapy.Spider):
    name = 'maoyan_yiqing_after'
    # allowed_domains = ['maoyan.com']
    # start_urls = ['https://piaofang.maoyan.com/dashboard-ajax/movie?showDate=20201012&movieId=1328712']
    header = {
        'User-Agent' : 'Mozilla / 5.0(WindowsNT6.3;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 77.0.3865.120Safari / 537.36'
    }
    def start_requests(self):
        for i in self.datelist('20200720','20201012'):
            url='https://piaofang.maoyan.com/dashboard-ajax/movie?showDate='+i
            yield scrapy.Request(
                url=url,
                headers=self.header,
                callback=self.parse
            )
    def datelist(self,beginDate,endDate):
        # beginDate, endDate是形如‘20160601’的字符串或datetime格式
        date_l = [datetime.strftime(x, '%Y%m%d') for x in list(pd.date_range(start=beginDate, end=endDate))]
        return date_l
    def parse(self, response):
        html = json.loads(response.text)
        for i in html['movieList']['list']:
            item=MaoyanItem()
            item['movieName'] = i['movieInfo']['movieName']  # 电影名字
            item['movieInfo'] = i['movieInfo']['movieId']  # 电影ID
            item['releaseInfo'] = i['movieInfo']['releaseInfo']  # 电影上映的天数
            item['boxSplitUnit'] = i['boxSplitUnit']['num'] + i['boxSplitUnit']['unit']  # 电影当天票房
            item['sumBoxDesc'] = i['sumBoxDesc']  # 电影总票房
            item['showCount'] = i['showCount']  # 电影排片场次
            item['boxRate'] = i['boxRate']  # 票房占比
            item['avgSeatView'] = i['avgSeatView']  # 电影上座率
            item['avgShowView'] = i['avgShowView']  # 电影场均人数
            print(item)
            # yield item
