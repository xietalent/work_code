import pymysql
import re模块

class StudentsSql(object):
    def __init__(self,host="47.97.217.36",user = "root",password="root",database="stu",port = 3306,charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset


    def connect(self):
        self.conn = pymysql.connect(host = self.host,user = self.user,password = self.password,database = self.database,port = self.port,charset = self.charset)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()


    def query_one(self,sql_line):
        self.connect()
        self.cursor.execute(sql_line)
        res = self.cursor.fetchall()
        # res = self.cursor.fetchone()
        if res != None:
            self.close()
            return res


    def query_all(self,condition,myid):
        self.connect()
        self.cursor.execute("select {} from students where id={};".format(condition,myid))
        res = self.cursor.fetchall()
        if res != None:
            self.close()
            return res

if __name__ == '__main__':
    sqls = StudentsSql()
    res = sqls.query_all("name",2)
    print(res)
