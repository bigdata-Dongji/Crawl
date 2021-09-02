# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
# from itemadapter import ItemAdapter
import logging

logger=logging.getLogger(__name__)

class ItcastSpiderPipeline:
    def process_item(self, item, spider):
        print(item)
        # if spider.name=='log_demo':
        #     logger.warning('-'*10)
        with open('poetry.txt','a')as f:
            f.write(f"{item['title']}\n{item['author']} {item['dynasty']}\n{item['content']}\n")
        return item
