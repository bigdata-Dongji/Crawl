# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
import pandas as pd
import logging

logger = logging.getLogger(__name__)


class Ssr2Pipeline:
    def __init__(self):
        self.pd = pd.DataFrame(
            columns=["name", "location", "duration", "release_time", "score", "detail"])
        self.pd2 = pd.DataFrame(
            columns=["url", "tags", "plot", "directors"])

    def open_spider(self, spider):
        self.start_time = time.time()

    def process_item(self, item, spider):
        if item.__class__.__name__ == "Ssr2Item_1":
            self.pd = self.pd.append(
                dict(zip(["name", "location", "duration", "release_time", "score", "detail"],
                         list(dict(item).values()))),
                ignore_index=True)

        if item.__class__.__name__ == "Ssr2Item_2":
            self.pd2 = self.pd2.append(
                dict(zip(["url", "tags", "plot", "directors"], list(dict(item).values()))),
                ignore_index=True)

    def close_spider(self, spider):

        self.pd = self.pd.sort_values(by="detail").reset_index()
        del self.pd['detail']
        self.pd2 = self.pd2.sort_values(by="url").reset_index()
        del self.pd2['url']
        end = pd.concat([self.pd, self.pd2], axis=1)
        del end['index']
        end.to_csv("ssr2.csv", index=None)
        self.end_time = time.time()
        print("耗时", self.end_time - self.start_time)
