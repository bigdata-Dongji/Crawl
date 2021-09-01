# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class KkgamePipeline(object):
    def process_item(self, item, spider):
        # print(item)
        # with open('./7k7k.csv','a',encoding="utf-8",newline="")as f:
        #     f.write(item)
        return item

# class KkgamePipelineByMysql(object):
#     conn = None  # mysql的连接对象声明
#     cursor = None  # mysql游标对象声明
#
#     def open_spider(self, spider):
#         print('开始爬虫')
#         # 链接数据库
#         self.conn = pymysql.Connect(host='localhost', port=3306, user='root', password='511722', db='crawler')
#
#     # 编写向数据库中存储数据的相关代码
#     def process_item(self, item, spider):
#         # 1.链接数据库
#         # 2.执行sql语句
#         sql = 'insert into game values("%s","%s","%s","%s","%s","%s","%s","%s","%s")' % (item['game_date'], item['game_ms'], item['game_name'], item['game_score'], item['game_size'], item['game_title'], item['game_type'], item['game_url'], item['pinlunnum'])
#         self.cursor = self.conn.cursor()
#         # 执行事务
#         try:
#             self.cursor.execute(sql)
#             self.conn.commit()
#         except Exception as e:
#             print(e)
#             self.conn.rollback()
#         return item
#
#
#     def close_spider(self, spider):
#         print('爬虫结束')
#         self.cursor.close()
#         self.conn.close()