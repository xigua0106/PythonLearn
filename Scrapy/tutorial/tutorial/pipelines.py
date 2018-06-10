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
        # 通过cursor创建游标 当游标建立之时，就自动开始了一个隐形的数据库事务
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