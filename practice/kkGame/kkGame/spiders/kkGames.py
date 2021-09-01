# -*- coding: utf-8 -*-
import scrapy
from kkGame.items import KkgameItem
import json

class KkgamesSpider(scrapy.Spider):
    name = 'kkGames'
    # 不需要域名，评论数的js网页不是同一个域名
    # allowed_domains = ['7k7k.com']
    # 分析网页结构，实现翻页
    start_urls = ['http://www.7k7k.com/tag/134/index_%s.htm'%i for i in range(1,96)]
    #获取列表页信息,获得详情页链接和评论数的js网页链接
    def parse(self, response):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        #获取到爬取内容的ul大框架
        ''
        html = response.xpath('//*[@id="theme-blue"]/div[3]/div[3]/div[1]/div/ul')
        #遍历框架下的li标签
        for i in html:
            #获取详情页的url
            link = i.xpath("./li/a/@href").extract()
            for li in link:
                    item=KkgameItem()
                    #获取游戏url地址
                    item["game_url"]=li
                    # 找到评论数所在的js网页链接规律，取出详情页url上的“id”
                    # 'http://www.7k7k.com/flash/199520.htm'
                    num1 = li.split('/')
                    num2 = num1[-1].split('.')
                    num3 = num2[0]
                    #用详情页url上的“id”来拼接评论数的js网页链接
                    url = 'https://changyan.sohu.com/api/2/topic/count?client_id=cyqHvdkcp&topic_id=&topic_source_id=7k7kmainsite{}&topic_url=&callback=getCmtSum'.format(num3)
                    #请求评论数的js网页链接，并传入item
                    yield scrapy.Request(
                        url,#请求url地址
                        headers=header,#请求头
                        callback=self.parse_in, #调用获取动态的评论数信息的parse_in
                        meta={"item":item} #传入item，键为item
                    )

    #获取动态的评论数信息
    def parse_in(self,response):
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36'}
        #接受parse传来的item
        item=response.meta["item"]
            # '/flash/160729.htm'
            # 'http://www.7k7k.com/flash/160729.htm'
        #取出详情页url上的“id”
        num1 = item["game_url"].split('/')
        num2 = num1[-1].split('.')
        num3 = num2[0]
        html1 = response.text.replace('getCmtSum(', '')
        html2 = html1.replace(');', '')
        #用详情页url上的“id”来拼接json数据的键，获取评论数数据
        urlss = json.loads(html2)["result"]['7k7kmainsite' + num3]['comments']
            # pl = urls.xpath('//*[@id="game-info"]/div[1]/span[1]/text()')
        pll = urlss
        item['pinlunnum'] = pll
        #请求详情页url，来获取数据，并传入item
        yield scrapy.Request(
            item["game_url"],#请求url地址
            headers=header,#请求头
            callback=self.parse_ins,#调用获取动态的评论数信息的parse_ins
            meta={"item":item}#传入item，键为item
        )

    #获取详情页信息
    def parse_ins(self,response):
        #接受parse_in传来的item
        item = response.meta["item"]
        #获取游戏名数据
        item['game_name'] = response.xpath('//*[@id="game-info"]/h1/a/text()').extract()
        # 获取游戏名类型
        type = response.xpath('//*[@id="game-info"]/div[1]/span[2]/text()')[0].extract().split('：')
        item['game_type'] = type[1]
        # 获取游戏大小
        size = response.xpath('//*[@id="game-info"]/div[1]/span[3]/text()')[0].extract().split('：')
        item['game_size'] = size[1].replace("M","")
        # 获取游戏日期
        date = response.xpath('//*[@id="game-info"]/div[1]/span[4]/text()')[0].extract().split('：')
        item['game_date'] = date[1]
        #获取游戏评分
        score_b = response.xpath('//*[@id="game-info"]/div[2]/span/text()').extract()
        score_s = response.xpath('//*[@id="game-info"]/div[2]/text()').extract()
        score_d = "".join(score_s[1])
        item['game_score'] = "".join(score_b) + score_d
        #获取游戏标签
        item['game_title'] = response.xpath('//*[@id="game-info"]/div[6]/a/text()').extract()
        #获取游戏描述
        strs = response.xpath('//*[@id="game-info"]/p/text()').extract()
        for i in strs:
            item['game_ms'] = "".join(i.split())
        print(item)
        #返回数据
        yield item
# 'https://changyan.sohu.com/api/2/topic/count?' \
# 'client_id=cyqHvdkcp&topic_id=&topic_source_id=7k7kmainsite152936&topic_url=&callback=getCmtSum'
