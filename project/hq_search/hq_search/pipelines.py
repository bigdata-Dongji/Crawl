# encoding:utf8
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import codecs,json


class HqSearchPipeline:
    def process_item(self, item, spider):
        return item

class JsonPipeline():
    # 自定义json文件的导出
    def __init__(self):
        self.file=open('data/blog.json', 'a', encoding='utf8')

    def process_item(self, item, spider):
        lines=json.dumps(dict(item),ensure_ascii=False)+'\n'
        self.file.write(lines)
        return item

    def spider_closed(self,spider):
        self.file.close()

class ElasticsearchPipeline():
    # 将数据写入到es中
    def process_item(self,item,spider):
        # 将item转换为es的数据
        item.save_to_es()
        return item