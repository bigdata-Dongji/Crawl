# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql

class MymovisPipeline(object):
    def process_item(self, item, spider):
        # 连接数据库
        conn = pymysql.connect(host='localhost',
                               user='root',
                               password='root',
                               db='python_datadb')

        # 创建一个游标
        cursor = conn.cursor()
        # item = {"name": '1', "starts": '2', "releasetime": '3', "score": 4}
        # table = 'create table mymovies(name varchar(255),starts varchar(255),relesetime varchar(255),score varchar(255))'
        sql = f'insert into mymovies values("{item["name"]}","{item["starts"]}","{item["releasetime"]}","{item["score"]}")'
        # cursor.execute(table)

        # conn.commit()
        cursor.execute(sql)
        conn.commit()
        return item
