from django.test import TestCase
import pymysql
# from .models import Integral,User
# Create your tests here.

# items = [{'my_integral': '0积分'}, {'bill': []}]
# my_integral = items[0]['my_integral']
# bill = items[1]['bill']
# if bill == []:
#     bill="暂无消费记录"
#
# items={
#     "my_integral":my_integral,
#     "bill":bill,
# }
#
# insert_ = Integral.objects.create(items)
# print(items)





# items = {'name': '6259691129820511', 'passwd': 'zc006688'}
#
# insert_ = User.objects.create(**items)


class Mysql_input(object):
    def __init__(self, host="47.97.217.36", user="root", password="root", database="user", port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()


    def get_data(self):
        self.connect()
        sql_2 = "select * from user1 order by id DESC limit 1;"
        self.cursor.execute(sql_2)
        res = self.cursor.fetchone()
        print(res)


if __name__ == '__main__':
    s = Mysql_input()
    s.get_data()