import scrapy
from ssr1.items import Ssr1Item


class Ssr1spiderSpider(scrapy.Spider):
    name = 'ssr1spider'
    allowed_domains = ['ssr1.scrape.center']
    start_urls = ['https://ssr1.scrape.center/']
    page = 2


    def parse(self, response):
        for res in response.xpath("//*[@id=\"index\"]/div[@class=\"el-row\"]/div[@class=\"el-col el-col-18 el-col-offset-3\"]/div[@class=\"el-card item m-t is-hover-shadow\"]/div[@class=\"el-card__body\"]/div[@class=\"el-row\"]"):
            item = Ssr1Item()
            detail_url = "http://ssr1.scrape.center" + str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/a/@href").extract_first())
            name = str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/a/h2/text()").extract_first())
            location = str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/div[2]/span[1]/text()").extract_first())
            duration = str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/div[2]/span[3]/text()").extract_first())
            release_time = str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/div[3]/span/text()").extract_first())
            score = str(res.xpath("./div[@class=\"el-col el-col-24 el-col-xs-5 el-col-sm-5 el-col-md-4\"]/p/text()").extract_first())
            item['name'] = name
            item['location'] = location
            item['duration'] = duration
            item['release_time'] = release_time
            item['score'] = score.replace(" ", "").replace("\n", "")

            yield scrapy.Request(
                url=detail_url,
                callback=self.parse_detail,
                meta={"item": item}
            )

        if self.page <= 10:
            yield scrapy.Request(
                url="https://ssr1.scrape.center/page/" + str(self.page),
                callback=self.parse,
            )
        self.page += 1

    def parse_detail(self, response):
        item = response.meta['item']
        tags = "、".join(response.xpath("//*[@id=\"detail\"]//div[@class=\"categories\"]//span/text()").extract())
        item['tags'] = tags
        plot = response.xpath("//*[@id=\"detail\"]//div[@class=\"drama\"]/p/text()").extract_first()
        item['plot'] = plot.replace(" ", "").replace("\n", "")
        directors = "、".join(response.xpath("//*[@id=\"detail\"]//div[@class=\"directors el-row\"]//div[@class=\"el-card__body\"]/p/text()").extract())
        item['directors'] = directors

        yield item
