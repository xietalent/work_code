# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

import requests
import pymysql

from lxml import etree
from time import sleep
from threading import Thread


class GetFangyuan():
    def __init__(self):
        # self.url = "https://sz.58.com/ershoufang/0/?PGTID=0d30000c-0000-43d8-718d-7210fc6a3004&ClickID="
        self.url = "https://sz.58.com/ershoufang/0/pn"
        self.headers= {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }

    def parse(self,page):
        my_url = self.url+page+"/"
        # print(my_url)
        se = requests.Session()
        #请求
        ershou_fang_html = se.get(url=my_url,headers=self.headers)
        # print(ershou_fang_html.text)
        html = ershou_fang_html.text
        ershou_fang_tree = etree.HTML(html)
        divs = ershou_fang_tree.xpath(".//ul[@class='house-list-wrap']")
        items = []
        for num in range(1,100):
            try:
                for div in divs:
                    item = {}
                    #标题
                    fang_title  = div.xpath(".//li[{}]/div[@class='list-info']/h2[@class='title']/a/text()".format(num))[0].strip()
                    #户型
                    fang_huxing = div.xpath(".//li[{}]/div[@class='list-info']/p[@class='baseinfo'][1]/span[1]/text()".format(num))[0].strip()
                    #单价
                    fang_unit_price = div.xpath(".//li[{}]/div[@class='price']/p[@class='unit']/text()".format(num))[0].strip()
                    #发布时间
                    fang_time = div.xpath("./li[{}]/div[@class='time']/text()".format(num))[0].strip()

                    print(fang_title)
                    print(fang_huxing)
                    print(fang_unit_price)
                    print(fang_time)
                    item["fang_title"] = fang_title
                    item["fang_huxing"] = fang_huxing
                    item["fang_unit_price"] = fang_unit_price
                    item["fang_time"] = fang_time
                    items.append(item)

                    #k
                    set_sql = Mysql_input()
                    t2 = Thread(target=set_sql.set_data,args=(fang_title,fang_huxing,fang_unit_price,fang_time))
                    t2.start()

                    # set_sql.set_data(fang_title,fang_huxing,fang_unit_price,fang_time)
            except Exception as e :
                print(e)
                break
        # print(items)
        yema = "第{}页:".format(page)
        with open(r"fanginfo/fang.txt",'a+',encoding='utf-8') as fp:
            fp.write(yema)
            fp.write(str(items))
            fp.write("\n")
            fp.close()

    def start(self):
        for page in range(1,100):
            try:
                page = str(page)
                self.parse(page)
                sleep(1)
            except Exception as e:
                print(e)
                break


# 数据库连接
class Mysql_input(object):
        def __init__(self, host="47.97.217.36", user="root", password="root", database="user", port=3306,
                     charset="utf8"):
            self.host = host
            self.user = user
            self.password = password
            self.database = database
            self.port = port
            self.charset = charset

        def connect(self):
            self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,port=self.port, charset=self.charset)
            self.cursor = self.conn.cursor()

        def set_data(self,fang_title="None",fang_huxing="None",fang_unit_price="None",fang_time="None"):
            self.connect()
            try:
                sql_1 = "INSERT INTO fang_info VALUES(null,'{}','{}','{}','{}');".format(fang_title,fang_huxing,fang_unit_price,fang_time)
                # sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
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
    getfang = GetFangyuan()
    getfang.start()