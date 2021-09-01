from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ssr2.items import Ssr2Item_1, Ssr2Item_2


class Ssr2spiderSpider(CrawlSpider):
    name = 'ssr2spider'
    allowed_domains = ['ssr1.scrape.center']
    start_urls = ['https://ssr1.scrape.center/']

    rules = (
        Rule(LinkExtractor(allow=r'page/\d+'), callback='parse_item', follow=True),
        Rule(LinkExtractor(allow=r'detail/\d+'), callback='parse_detail', follow=True)
    )

    def parse_item(self, response):
        for res in response.xpath("//*[@id=\"index\"]/div[@class=\"el-row\"]/div[@class=\"el-col el-col-18 el-col-offset-3\"]/div[@class=\"el-card item m-t is-hover-shadow\"]/div[@class=\"el-card__body\"]/div[@class=\"el-row\"]"):
            item = Ssr2Item_1()
            detail_url = "https://ssr1.scrape.center" + str(res.xpath("./div[@class=\"p-h el-col el-col-24 el-col-xs-9 el-col-sm-13 el-col-md-16\"]/a/@href").extract_first())
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
            item['detail']=detail_url.replace(" ", "").replace("\n", "").split("/")[-1]
            yield item

    def parse_detail(self, response):
        item = Ssr2Item_2()
        item['url'] = str(response.url).split("/")[-1]
        tags = "、".join(response.xpath("//*[@id=\"detail\"]//div[@class=\"categories\"]//span/text()").extract())
        item['tags'] = tags
        plot = response.xpath("//*[@id=\"detail\"]//div[@class=\"drama\"]/p/text()").extract_first()
        item['plot'] = plot.replace(" ", "").replace("\n", "")
        directors = "、".join(response.xpath(
            "//*[@id=\"detail\"]//div[@class=\"directors el-row\"]//div[@class=\"el-card__body\"]/p/text()").extract())
        item['directors'] = directors
        yield item
