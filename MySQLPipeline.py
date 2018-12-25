
import pymysql


class MysqlPipeline(object):
    COMMIT_NUM = 50

    def __init__(self):
        self.conn = None
        self.cur = None
        self.wait_for_commit = 0

    def open_spider(self, spider):
        self.conn = pymysql.connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='',
            db='xpc1801',
            charset='utf8mb4'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        if not hasattr(item, 'table_name'):
            return item
        cols, values = zip(*item.items())
        sql = "INSERT INTO `{}` ({}) VALUES " \
              "({})".format(
            item.table_name,
            ','.join(['`%s`' % k for k in cols]),
            ','.join(["%s"] * len(values))
        )
        self.cur.execute(sql, values)
  
        self.wait_for_commit += 1
        self.commit()
        return item

    def commit(self):
        if self.wait_for_commit >= self.COMMIT_NUM:
            self.conn.commit()
            print('commit %s rows to database' % self.wait_for_commit)
            self.wait_for_commit = 0

    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()
