# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline


class SpiderStarPipeline:
    def process_item(self, item, spider):
        return item

class ImagePipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        yield Request(item['images'],meta={'':item,'':item['']})

    def file_path(self, request, response=None, info=None, *, item=None):
        ...