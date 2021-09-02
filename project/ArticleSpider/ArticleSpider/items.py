# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
# import redis
from ArticleSpider.models.es_types import ArticleType
from ArticleSpider.models.es_types import XinpiType
from w3lib.html import remove_tags
from elasticsearch_dsl.connections import connections
es = connections.create_connection(ArticleType._doc_type.using)

# redis_cli = redis.StrictRedis()

class ArticlespiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class LieyunArticleItem(scrapy.Item):
    title=scrapy.Field()
    create_date=scrapy.Field()
    url=scrapy.Field()
    url_object_id=scrapy.Field() # md5生产的ID，因很多url过长和长短不一，可以限定长度
    front_image_url=scrapy.Field()
    # front_image_path=scrapy.Field() # 封面图片位置
    tags=scrapy.Field()
    content=scrapy.Field()

    def save_to_es(self):
        article = ArticleType()
        article.title = self['title']
        article.create_date = self["create_date"]
        article.content = remove_tags(self["content"])
        article.front_image_url = self["front_image_url"]
        # if "front_image_path" in self:
        #     article.front_image_path = self["front_image_path"]
        article.url = self["url"]
        article.tags = self["tags"]
        article.meta.id = self["url_object_id"]

        article.suggest = gen_suggests(ArticleType._doc_type.index, ((article.title,10),(article.tags, 7)))

        article.save()

        # redis_cli.incr("lieyun_count")

        return

class XinpiItem(scrapy.Item):
    chi_name = scrapy.Field()  # 公司名称
    email = scrapy.Field()
    indurstry = scrapy.Field()  # 所属行业
    reg_addr = scrapy.Field()  # 注册地址
    legal_repr = scrapy.Field()  # 法人代表
    general_manager = scrapy.Field()  # 总 经 理

    report_date = scrapy.Field()  # 报告日期
    operating_revenue = scrapy.Field()  # 营业收入
    np_parent_company_owners = scrapy.Field()  # 归属母公司利润
    index=scrapy.Field() # 自定义ID

    def save_to_es(self):
        info = XinpiType()
        info.chi_name = self['chi_name']
        info.email = self["email"]
        info.indurstry = remove_tags(self["indurstry"])
        info.reg_addr = self["reg_addr"]
        info.legal_repr = self["legal_repr"]
        info.general_manager = self["general_manager"]
        info.report_date = self["report_date"]
        info.operating_revenue = self["operating_revenue"]
        info.np_parent_company_owners = self["np_parent_company_owners"]

        info.meta.id = self["index"]

        info.suggest = gen_suggests(ArticleType._doc_type.index, ((info.chi_name,10),(info.indurstry, 7)))

        info.save()
        # redis_cli.incr("lieyun_count")
        return


def gen_suggests(index, info_tuple):
    #根据字符串生成搜索建议数组
    used_words = set()
    suggests = []
    for text, weight in info_tuple:
        if text:
            #调用es的analyze接口分析字符串
            words = es.indices.analyze(index=index, analyzer="ik_max_word", params={'filter':["lowercase"]}, body=text)
            anylyzed_words = set([r["token"] for r in words["tokens"] if len(r["token"])>1])
            new_words = anylyzed_words - used_words
        else:
            new_words = set()

        if new_words:
            suggests.append({"input":list(new_words), "weight":weight})

    return suggests