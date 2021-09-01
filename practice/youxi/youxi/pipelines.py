# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class YouxiPipeline(object):
    ziduanming = ['游戏名称', '评论数', '类型', '大小', '日期', '评分', '标签', '游戏描述']      #定义一个写入将数据写入一个字段名
    with open("./7k7kgame.csv", 'a', encoding="utf-8", newline="")as f:
        wri = csv.writer(f)
        wri.writerow(ziduanming)
    def process_item(self, item, spider):
        datas= []
        for i in item.values():                 #循环item返回过来的值
            datas.append(i)                     #将返回的值传递给datas这个数组
        with open("./完全体7k7kgame.csv",'a',encoding="utf-8",newline="")as f:
            wri = csv.writer(f)
            wri.writerow(datas)                 #将数据用csv写入文件
        print(item)
        return item
# import os
# import csv
#
# class MoonBlogPipeline(object):
#
#         def __init__(self):
#             # csv文件的位置,无需事先创建
#             store_file = os.path.dirname(__file__) + './完全体7k7kgame.csv'
#             print("***************************************************************")
#             # 打开(创建)文件
#
#             self.file = open(store_file, 'a+', encoding="utf-8",newline='')
#             # csv写法
#             self.writer = csv.writer(self.file, dialect="excel")
#
#         def process_item(self, item, spider):
#             # 判断字段值不为空再写入文件
#             print("正在写入......")
#             if item['article_title']:
#                 # 主要是解决存入csv文件时出现的每一个字以‘，’隔离
#                 self.writer.writerow([item['article_title'],item['article_link'],item['publish_date'],item['scan_num'],item['article_content']])
#             return item
#
#         def close_spider(self, spider):
#             # 关闭爬虫时顺便将文件保存退出
#             self.file.close()