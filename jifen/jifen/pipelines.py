# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.utils.project import get_project_settings
from .items import ProductItem
import pymysql

# class JifenPipeline(object):
#     def process_item(self, item, spider):
#         return item


class JifenPipeline(object):
    def open_spider(self,spider):
        settings = get_project_settings()
        host = settings['HOST']
        port = settings['PORT']
        user = settings['USER']
        password = settings['PASSWORD']
        dbname = settings['DBNAME']
        charset = settings['CHARSET']
        # 链接数据库
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=dbname, charset=charset)
        # 获取游标
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        # 执行sql语句，写入到数据库中
        # 拼接sql语句

        # sql = "insert into "

        # if isinstance(item,ProductItem):
        #     sql = 'insert into book_list(author,book_name, book_pic_url, url) values("%s","%s","%s","%s")' % (item['author'],item['book_name'], item['book_pic_url'], item['url'])
        # elif isinstance(item, ProductItem):
        #     sql = 'insert into book_detail(book_name2,book_img_url, book_update, book_hot,book_type,book_intro) values("%s","%s","%s","%s","%s","%s")' % (
        # item['book_name2'], item['book_img_url'], item['book_update'], item['book_hot'], item['book_type'],
        # item['book_intro'])
        # else :
        #     sql = 'insert into book_catalog(catalog_id,catalog_title, catalog_url) values("%s","%s","%s")' % (
        # item['catalog_id'], item['catalog_title'], item['catalog_url'])
        # self.cursor.execute(sql)
        # # 提交一下
        # self.conn.commit()
        # # 执行sql语句
        try:
            self.cursor.execute(sql)
            # 提交一下
            self.conn.commit()
        except Exception as e:
            print('*' * 100)
            print(e)
            print('*' * 100)
            # 回滚
            self.conn.rollback()

        return item

    def close_spider(self, spider):
        #关闭游标
        self.cursor.close()
        # 关闭数据库
        self.conn.close()