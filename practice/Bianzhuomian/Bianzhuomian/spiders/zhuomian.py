# -*- coding: utf-8 -*-
import scrapy
import json
import requests
class ZhuomianSpider(scrapy.Spider):
    name = 'zhuomian'
    allowed_domains = ['ss.netnr.com']
    start_urls = ['https://bird.ioliu.cn/v2?url=http%3A%2F%2Fwallpaper.apc.360.cn%2Findex.php%3Fc%3DWallPaper%26start%3D1%26count%3D12%26from%3D360chrome%26a%3DgetAppsByOrder%26order%3Dcreate_time']
    # start_urls = [f'https://bird.ioliu.cn/v2?url=http%3A%2F%2Fwallpaper.apc.360.cn%2Findex.php%3Fc%3DWallPaper%26start%3D{i}%26count%3D12%26from%3D360chrome%26a%3DgetAppsByOrder%26order%3Dcreate_time' for i in range(1,1000,12)]

    def parse(self, response):
        html = json.loads(response.text)
        for i in html['data']:
            html = requests.get(i['url_thumb'].replace('__85','__100'))
            with open("‪D:/壁纸爬取存放/桌面壁纸/" + "1"+str(i['utag']) + ".jpg", 'ab')as f:
                f.write(html.content)
