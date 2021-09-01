# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs
import time
import logging

logger = logging.getLogger(__name__)

class Ssr1Pipeline:
    def __init__(self):
        self.f = codecs.open("ssr1.csv", "a+", "utf-8")
        self.f.write("name,location,duration,release_time,score,tags,plot,directors\n")

    def open_spider(self, spider):
        self.start_time = time.time()

    def process_item(self, item, spider):
        self.f.write(
            dict(item)['name'] + "," + dict(item)['location'] + "," + dict(item)['duration'] + "," + dict(item)[
                'release_time'] + "," + dict(item)['score'] + "," + dict(item)['tags'] + "," + dict(item)[
                'plot'] + "," + dict(item)['directors'] + "\n")
        return item

    def close_spider(self, spider):
        self.f.close()
        self.end_time = time.time()
        print("耗时", self.end_time - self.start_time)
