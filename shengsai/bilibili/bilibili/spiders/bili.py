# -*- coding: utf-8 -*-
import scrapy
from scrapy框架.shengsai.bilibili.bilibili.items import BilibiliItem

class BiliSpider(scrapy.Spider):
    name = 'bili'
    allowed_domains = ['bilibili.com']
    start_urls = [f'https://search.bilibili.com/all?keyword=%E7%88%AC%E8%99%AB&from_source=nav_suggest_new&page={i}' for i in range(1,11)]

    def parse(self, response):
        url =(response.url)
        cookies = {
            "cookie": "buvid3=44FFFDB6-39F7-4064-A92A-451B7F652038155819infoc; LIVE_BUVID=AUTO7415709407666831; stardustvideo=1; rpdid=|(ummm|~~RkJ0J'ul~|mR|~~~; im_notify_type_173234650=0; Hm_lvt_eaa57ca47dacb4ad4f5a257001a3457c=1576113961,1576125432,1578026918; blackside_state=1; CURRENT_QUALITY=80; CURRENT_FNVAL=80; _uuid=E7616C3A-B8EA-56BA-7DDB-63C60804DEFD39402infoc; bp_t_offset_37748081=462688223983654777; bp_video_offset_37748081=463152071861525740; sid=hsr0pmbe; DedeUserID=173234650; DedeUserID__ckMd5=c616239e333d39f8; SESSDATA=969c2d96%2C1622247645%2Cedf9b*b1; bili_jct=71bc6bda986c8dbe2b85901bb0fa497b; fingerprint3=a318682c183fc382c274fb22e5789b9f; fingerprint=a8843b494a265ca69bf006d636270150; fingerprint_s=a7c912cd2c37b6c271c5db5e869a9993; buivd_fp=44FFFDB6-39F7-4064-A92A-451B7F652038155819infoc; buvid_fp_plain=44FFFDB6-39F7-4064-A92A-451B7F652038155819infoc; PVID=1; bp_video_offset_173234650=470806665657414070; bp_t_offset_173234650=471205607990439810; finger=158939783; arrange=matrix"}
        yield scrapy.FormRequest(
            url=url,
            cookies=cookies,
            callback=self.data
        )

    def data(self, response):
        if response.url == 'https://search.bilibili.com/all?keyword=%E7%88%AC%E8%99%AB&from_source=nav_suggest_new&page=1':
            name = (response.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[1]/a/text()[2]').getall())    #标题
            time = (response.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[3]/span[3]/text()').getall()) #发布时间
            number = (response.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[3]/span[1]/text()').getall()) #观看人数
            author = (response.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[3]/span[4]/a/text()').getall()) #up主
            urls = (response.xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li/div/div[1]/a/@href').getall()) #链接
            for i in range(len(name)):
                item = BilibiliItem()
                item['name'] = name[i]
                item['time'] = time[i].strip()
                item['number'] = number[i].strip()
                item['author'] = author[i]
                item['url'] = urls[i].replace('//','')
                # print(item)
                yield item
        else:
            name = (response.xpath('//*[@id="all-list"]/div[1]/ul/li/div/div[1]/a/text()[1]').getall())  # 标题
            time = (
                response.xpath('//*[@id="all-list"]/div[1]/ul/li/div/div[3]/span[3]/text()').getall())  # 发布时间
            number = (
                response.xpath('//*[@id="all-list"]/div[1]/ul/li/div/div[3]/span[1]/text()').getall())  # 观看人数
            author = (
                response.xpath('//*[@id="all-list"]/div[1]/ul/li/div/div[3]/span[4]/a/text()').getall())  # up主
            urls = (response.xpath('//*[@id="all-list"]/div[1]/ul/li/div/div[1]/a/@href').getall())  # 链接
            for i in range(len(name)):
                item = BilibiliItem()
                item['name'] = name[i]
                item['time'] = time[i].strip()
                item['number'] = number[i].strip()
                item['author'] = author[i]
                item['url'] = urls[i].replace('//', '')
                # print(item)
                yield item

from scrapy.cmdline import execute
execute(['scrapy','crawl','bili','-o','video.csv'])
# execute(['scrapy','crawl','bili'])


'''
//*[@id="all-list"]/div[1]/ul/li[1]/div/div[1]/a/text()[1]
//*[@id="all-list"]/div[1]/div[2]/ul/li[1]/div/div[1]/a/text()[2]

'''
