# # -*- coding: utf-8 -*-
#
# # Define your item pipelines here
# #
# # Don't forget to add your pipeline to the ITEM_PIPELINES setting
# # See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#
# from scrapy.pipelines.images import ImagesPipeline
import scrapy
import requests
# class ImgsPipeline(object):
#     def process_item(self, item, spider):
#         with open('./imgss'+str(item['img_src'])+'.jpg','wb')as f:
#             HTML= scrapy.Request(item['img_src'])
#             # f.write(HTML)
#             print(HTML)
#
#         return item


import scrapy
from scrapy.pipelines.images import ImagesPipeline


class ImgsPipeline(ImagesPipeline):
    """
    类说明：自定义的专用于图片下载的管道类
    """

    def get_media_requests(self, item, info):
        # 这里因为获取的是二进制数据，所以不需要 callback回调请求
        yield scrapy.Request(item['img_src'])

    def file_path(self, request, response=None, info=None,):
        imgName = request.url.split('/')[-1]        #图片的名字
        return imgName

    def item_completed(self, results, item, info):
        return item  # 返回给下一个即将被执行的管道类
