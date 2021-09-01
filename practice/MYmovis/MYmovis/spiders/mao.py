# -*- coding: utf-8 -*-
import scrapy


class MaoSpider(scrapy.Spider):
    name = 'mao'
    allowed_domains = ['maoyan.com/']
    offset = 0
    url = "https://maoyan.com/board/4?offset="
    # ********** Begin **********#
    # 1.对url进行定制，为翻页做准备
    start_urls = [url + str(offset)]


    # 2.定义爬虫函数parse()
    def parse(self, response):
        urls = response.xpath('//dl[@class="board-wrapper"]/dd[.]')  # 将数据进行解析
        # //*[@id="app"]/div/div/div/dl/dd[.]/a
        pj = 'https://maoyan.com/'  # 将网页链接定义，方便下面数据进行拼接
        for i in urls:
            item = {}
            # item["href"] = pj + i.xpath('./a/@href').extract_first()  # 拼接网页链接
            item["name"] = i.xpath('./a/@title').extract_first()  # 获取数据的标题等内容
            item["starts"] = i.xpath('./div/div/div/p[2]/text()').extract_first().replace("\n", "").replace(" ",
                                                                                                            "")  # 将数据进行简单的清洗使数据规范化
            item["releasetime"] = i.xpath('./div/div/div/p[3]/text()').extract_first()
            # 上映时间
            item['releasetime'] = i.xpath(".//div[1]/p[3]/text()").extract()[0]
            score1 = i.xpath("./div/div/div[2]/p/i[1]/text()").extract()[0]
            score2 = i.xpath("./div/div/div[2]/p/i[2]/text()").extract()[0]
            # 评分
            item['score'] = score1 + score2
            yield (item)

        if self.offset < 100:
            self.offset += 10
            yield scrapy.Request(self.url + str(self.offset), callback=self.parse)


