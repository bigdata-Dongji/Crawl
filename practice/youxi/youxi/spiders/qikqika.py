# -*- coding: utf-8 -*-
import scrapy
import re
import requests
import json

class QikqikaSpider(scrapy.Spider):
    name = 'qikqika'
    allowed_domains = ['7k7k.com']
    start_urls = ['http://www.7k7k.com/tag/134/index_%s.htm#p-anchor'%i for i in range(1,96)]       #网页进行翻页

    def parse(self, response):
        items = response.xpath('//div[@class="ui-slide-cont"]/ul/li/a/@href')              #将网页数据进行xpath选取
        urls=[]
        for i in items:                         #将网页选择的数据进行循环
            url = re.findall("data='(.*?)'>",str(i))[0]         #用正则表达式进行连接拼接
            if url[0] == "/":
                urls.append('http://www.7k7k.com'+url)
        for i in urls[:-3]:
            try:
                item = {}                       #设置一个空字典
                html = requests.get(i).text     #用requests获取拼接的网页链接数据
                title = re.findall('target="_self">(.*?)</a></h1>',html)    #正则匹配游戏的标题
                urlss = re.findall('<a href="/swf/(.*?).htm" target="_self" class="trans-play"', html)  #正则匹配游戏链接
                urla = 'https://changyan.sohu.com/api/2/topic/count?client_id=cyqHvdkcp&topic_id=&topic_source_id=7k7kmainsite{}&topic_url=&callback=getCmtSum'.format(urlss[0])
                hts = requests.get(urla).text
                hts = hts.replace("getCmtSum(", "").replace(");", "")
                comment = json.loads(hts)['result']['7k7kmainsite' + str(urlss[0])]['comments']     #获取评论的json数据
                # print(comment)
                #将完整数据进行获取
                data = re.findall('<span class="item">已有<span class="cy_cmt_count" id=".*?">(.*?)</span>(.*?)</span> <span class="item">(.*?)</span> <span class="item">(.*?)</span> <span class="item">(.*?)</span>',html)
                leixing = data[0][2]    #获取游戏的类型
                daxiao = data[0][3]    #获取游戏的大小
                date = data[0][4]    #获取游戏的上架时间
                pingfen = re.findall('<span>(.*?)</span>(.*?)<i class="gray">(.*?)</i></div>',html)         #获取游戏的评分
                miao = re.compile('<p class="game-describe">\\r\\n                        (.*?)                        </p>',re.S)
                miaoshu = re.findall(miao,html)             #获取游戏的描述
                biao = re.compile('<div class="game-tag">(.*?)：.*?a href=".*?">(.*?)</a>.*?ref=".*?">(.*?)</a.*?ref=".*?">(.*?)</a.*?ref=".*?">(.*?)</a.*?div>',re.S)
                biaoqian = re.findall(biao,html)    #获取游戏的标签
                item["名字"]=title[0]
                item["评论"]=comment
                item["类型"]=leixing
                item["大小"]=daxiao
                item["时间"]=date
                item["评分"]=pingfen[0][0]+pingfen[0][1]+pingfen[0][2]
                item["标签"] = biaoqian[0][:3]
                item["描述"]=miaoshu[0]
                # print(item)
                yield item          #将游戏数据进行返回给pipelines
            except:                 #获取数据异常就跳过该数据，保证代码的运行
                pass


