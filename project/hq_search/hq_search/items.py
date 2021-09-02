# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from hq_search.models.es_types import BlogType
from w3lib.html import remove_tags

class HqSearchItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class itBlogItem(scrapy.Item):
    title= scrapy.Field()
    blog_url= scrapy.Field() # 对url进行md5生成
    author= scrapy.Field()
    publisher= scrapy.Field()
    blog_type= scrapy.Field()
    release_time= scrapy.Field()
    tags= scrapy.Field()
    likes= scrapy.Field()
    collection= scrapy.Field()
    reading= scrapy.Field()
    update_time= scrapy.Field()
    content= scrapy.Field()
    id=scrapy.Field() # es id

    def save_to_es(self):
        blog = BlogType()
        blog.title = self['title']
        blog.blog_url = self['blog_url']
        blog.author = self['author']
        blog.publisher = self['publisher']
        blog.blog_type = self['blog_type']
        blog.release_time = self['release_time']
        blog.tags = self['tags']
        blog.likes = self['likes']
        blog.collection = self['collection']
        blog.reading = self['reading']
        blog.update_time = self['update_time']
        blog.content = remove_tags(self['content'])
        # blog.meta.id=self['id']
        blog.save()

        return