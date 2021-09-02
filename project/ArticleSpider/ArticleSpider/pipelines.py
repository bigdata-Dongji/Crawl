# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join, Identity

# from utils.common import extract_num
# from settings import SQL_DATETIME_FORMAT, SQL_DATE_FORMAT

from w3lib.html import remove_tags
from ArticleSpider.models.es_types import ArticleType
from ArticleSpider.models.es_types import XinpiType



from elasticsearch_dsl.connections import connections
es = connections.create_connection(ArticleType._doc_type.using)
es = connections.create_connection(XinpiType._doc_type.using)


class ArticlespiderPipeline:
    def process_item(self, item, spider):
        return item

class JsonWithEncodingPipeline(object):
    # 自定义json文件导出
    def __init__(self):
        # self.file=codecs.open('lieyun_news.json','a',encoding='utf8')
        self.file=codecs.open('test.json','a',encoding='utf8')

    def process_item(self, item, spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()

class ElasticsearchPipeline(object):
    #将数据写入到es中

    def process_item(self, item, spider):
        #将item转换为es的数据
        item.save_to_es()

        return item