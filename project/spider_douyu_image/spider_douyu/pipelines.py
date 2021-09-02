# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
from scrapy import Request
from scrapy.pipelines.images import ImagesPipeline

class ImagePipeline(ImagesPipeline):

    def get_media_requests(self, item, info):
        yield Request(item['image'],meta={'name':item['name']})

    def file_path(self, request, response=None, info=None, *, item=None):
        file_name=request.meta['name']+'.jpg'
        print('file_name:',file_name)
        return file_name

    def item_completed(self, results, item, info):
        image_paths=[x['path'] for ok,x in results if ok]
        print('completed')
        if not image_paths:
            item['image']='none'
        return item


class SpiderDouyuPipeline:
    def process_item(self, item, spider):
        return item