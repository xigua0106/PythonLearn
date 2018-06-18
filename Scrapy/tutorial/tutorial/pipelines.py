# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json
import pymysql
from twisted.enterprise import adbapi
import codecs
import json
from logging import log
from Helper.DBHelper import DBHelper


# TODO 试一下mongoDB
class TutorialPipeline(object):
    collection_name = 'scrapy_items'

    # sql = "INSERT INTO `trending` (`title`, `abstract`, `nickname`, `comments`, `likes`, `money`) " \
    #       "VALUES ('%s', '%s', '%s', '%s', '%s', '%s')" \
    #       % (item['title'], item['abstract'], item['nickname'], item['comments'], item['likes'], item['money'], )

    def __init__(self):
        self.dbHelper = DBHelper()
        # self._connection = pymysql.connect("localhost", "root", "op90--", "test", charset='utf8')
        # 通过cursor创建游标 当游标建立之时，就自动开始了一个隐形的数据库事务
        # self._cursor = self._connection.cursor()

    def process_item(self, item, spider):
        sql = "INSERT INTO `NowCoder`(question,answer) values(%s,%s)"
        #  *表示拆分元组，调用insert（*params）会重组成元组
        self.dbHelper.insert(sql, item['question'], item['answer'])
        return item


class JsonWithEncodingPipeline(object):
    # 保存到文件中对应的class
    #    1、在settings.py文件中配置
    #    2、在自己实现的爬虫类中yield item,会自动执行
    def __init__(self):
        # 保存为json文件
        self.file = codecs.open('info.json', 'w', encoding='utf-8')

    def process_item(self, item, spider):
        # 转为json的
        line = json.dumps(dict(item)) + "\n"
        # 写入文件中
        self.file.write(line)
        return item

    # 爬虫结束时关闭文件
    def spider_closed(self, spider):
        self.file.close()


# class MysqlTwistedPipline(object):
#     # 采用异步的方式插入数据
#     def __init__(self,dbpool):
#         self.dbpool = dbpool
#
#     @classmethod
#     def from_settings(cls,settings):
#         dbparms = dict(
#             host=settings["MYSQL_HOST"],
#             port=settings["MYSQL_PORT"],
#             user=settings["MYSQL_USER"],
#             passwd=settings["MYSQL_PASSWD"],
#             db=settings["MYSQL_DB"],
#             use_unicode=True,
#             charset="utf8",
#         )
#         dbpool = adbapi.ConnectionPool("pymysql",**dbparms)
#         return cls(dbpool)
#
#     def process_item(self,item,spider):
#         '''
#         使用twisted将mysql插入变成异步
#         :param item:
#         :param spider:
#         :return:
#         '''
#         query = self.dbpool.runInteraction(self.do_insert,item)
#         query.addErrback(self.handle_error)
#
#     def handle_error(self,failure):
#         #处理异步插入的异常
#         print(failure)
#
#     def do_insert(self,cursor,item):
#         #具体插入数据
#         insert_sql = '''
#             insert into jobbole_article(title,create_date,url,url_object_id,front_image_url,front_image_path,comment_nums,fav_nums,praise_nums,tag,content) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)
#             '''
#         cursor.execute(insert_sql,(item["title"],item["create_date"],item["url"],item["url_object_id"],item["front_image_url"],item["front_image_path"],item["comment_nums"],item["fav_nums"],item["praise_nums"],item["tag"],item["content"]))


# class ArticleImagePipeline(ImagesPipeline):
#     '''
#     对图片的处理
#     '''
#     def item_completed(self, results, item, info):
#
#         for ok ,value in results:
#             if ok:
#                 image_file_path = value["path"]
#                 item['front_image_path'] = image_file_path
#             else:
#                 item['front_image_path'] = ""
#
#
#         return item