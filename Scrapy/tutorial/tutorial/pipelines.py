# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
import pymysql
#TODO 试一下mongoDB
class TutorialPipeline(object):
    collection_name = 'scrapy_items'

    def __init__(self):
        self._connection = pymysql.connect("localhost", "root", "op90--", "test", charset='utf8')
        # 通过cursor创建游标
        self._cursor = self._connection.cursor()

    def process_item(self, item, spider):
        info = dict(item)
        sql = "INSERT INTO `trending` (`title`, `abstract`, `nickname`, `comments`, `likes`, `money`) " \
              "VALUES ('%s', '%s', '%s', '%s', '%s', '%s')"\
              % (item['title'], item['abstract'], item['nickname'], item['comments'], item['likes'], item['money'], )
        self._cursor.execute(sql)
        # 提交SQL
        self._connection.commit()
        return item
    #
    # # 打开数据库连接
    # db = pymysql.connect("localhost", "aver3", "op90--", "JianShuDB", charset='utf8')
    # # 使用cursor()方法获取操作游标
    # 在Python数据库编程中，当游标建立之时，就自动开始了一个隐形的数据库事务
    # cursor = db.cursor()
    # # 如果数据表已经存在使用 execute() 方法删除表。
    # cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")
    # # 创建数据表SQL语句
    # sql = """CREATE TABLE EMPLOYEE (
    #          FIRST_NAME  CHAR(20) NOT NULL,
    #          LAST_NAME  CHAR(20),
    #          AGE INT,
    #          SEX CHAR(1),
    #          INCOME FLOAT )"""
    # cursor.execute(sql)
    # # 关闭数据库连接
    # db.close()
