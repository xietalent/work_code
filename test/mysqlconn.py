import pymysql

class Mysql_input(object):
    def __init__(self,host="47.97.217.36",user = "root",password="root",database="user",port = 3306,charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset


    def connect(self):
        self.conn = pymysql.connect(host = self.host,user = self.user,password = self.password,database = self.database,port = self.port,charset = self.charset)
        self.cursor = self.conn.cursor()

    def set_data(self,my_integral="900积分",bill="12月消费100积分"):
        self.connect()
        try:
            sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
            self.cursor.execute(sql_1)
            self.conn.commit()
            print("添加成功")
            res = self.cursor.fetchall()
            if res != None:
                self.close()
                return res
        except:
            self.conn.rollback()


    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    ss = Mysql_input()
    ss.set_data()