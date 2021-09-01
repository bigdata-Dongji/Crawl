# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql

class GamePipeline(object):
    def process_item(self, item, spider):
        #链接数据库
        conn = pymysql.connect(host="localhost",user ="root", password ="root",database ="4399xiaoyouxi",charset ="utf8")

        #得到一个可以执行的sql语句的光标对象
        cursor = conn.cursor()  #执行完毕返回的结果集默认以元组显示

        #定义一个写入的SQL语句
        sql = "inster into xiaoyouxi values(%s,%s,%s,%s,%s,%s)"%(item["title"],item["fenlei"],item["daixao"],pymysql.escape_string(item["url"]),item["leixing"],item["jieshao"])
        # data = [item["title"],item["fenlei"],item["daixao"],item["date"],item["leixing"],item["jieshao"]]
        # print(data)

        #拼接写入的sql语句
        cursor.execute(sql)

        #涉及写的操作要注意提交
        conn.commit()

        #关闭链接
        cursor.close()
        conn.close()
        return item
