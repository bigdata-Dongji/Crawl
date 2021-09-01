# -*- coding: utf-8 -*-
import scrapy
import json

class ItemSpider(scrapy.Spider):
    name = 'item'
    allowed_domains = ['photo.fengniao.com']
    start_urls = ['https://photo.fengniao.com/ajaxPhoto.php?action=getPhotoLists&fid=101&sort=0&page=%s'%i for i in range(1,51)]

    def parse(self, response):
        html = json.loads(response.text)
        for i in  html['content']:
            datas = {}
            datas["name"] = i['title']
            datas["image"] = i["image"].replace("?imageView2/2/w/300/q/100/ignore-error/1/","")
            yield (datas)