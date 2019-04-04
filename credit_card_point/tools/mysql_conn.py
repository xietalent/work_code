from threading import  Thread
from lxml import etree

import pymysql

class My_set():
    def get_nums(self):
        with open(r'E:\code\spiders\text\deposits_html.txt',"r", encoding="utf-8") as f:
            html = f.read()

        deposits_tree = etree.HTML(html)

        divs = deposits_tree.xpath(".//div[@id='page_margin']//div[@id='page_content']")

        for div in divs:
            zhanghu_items=[]
            for i in range(1,20):
                try:
                    item={}
                    #账户信息
                    zhanghu_xinxi = div.xpath("./form[@id='form']/div[@class='info-show'][{}]/span/text()".format(i))
                    # print(type(zhanghu_xinxi))
                    zhanghu_leixing = zhanghu_xinxi[0]
                    # print(zhanghu_leixing)
                    zhanghu_huming = zhanghu_xinxi[1]
                    # print(zhanghu_huming)
                    zhanghu_nums = zhanghu_xinxi[2]
                    zhanghu_zhuangtai = zhanghu_xinxi[3]
                    item["账户类型"] = zhanghu_leixing
                    item["账户户名"] = zhanghu_huming
                    item["账号"] = zhanghu_nums
                    item["账户状态"] =  zhanghu_zhuangtai
                    zhanghu_items.append(item)


                    #存款信息
                    cunkuan_xinxi = div.xpath("./form[@id='form']/table[{}]//tr/td/text()".format(i))
                    items=[]
                    for j in range(0,10):
                        try:
                            strs = {}
                            # str = cunkuan_xinxi[i].strip()
                            xuhao = cunkuan_xinxi[0+11*j].strip()
                            chuzhong = cunkuan_xinxi[1+11*j].strip()
                            bizhong= cunkuan_xinxi[2+11*j].strip()
                            chaohui= cunkuan_xinxi[3+11*j].strip()
                            yu_e= cunkuan_xinxi[4+11*j].strip()
                            keyong_yue= cunkuan_xinxi[5+11*j].strip()
                            kaihuriqi= cunkuan_xinxi[6+11*j].strip()
                            cunqi= cunkuan_xinxi[7+11*j].strip()
                            daoqiriqi= cunkuan_xinxi[8+11*j].strip()
                            xucuncunqi= cunkuan_xinxi[9+11*j].strip()
                            zhuangtai= cunkuan_xinxi[10+11*j].strip()
                            # caozuo= cunkuan_xinxi[11+11*i].strip()

                            strs["序号"] = xuhao
                            strs["储种"] = chuzhong
                            strs["币种"] =bizhong
                            strs["钞汇"] =chaohui
                            strs["余额"] =yu_e
                            strs["可用余额"] =keyong_yue
                            strs["开户日期"] =kaihuriqi
                            strs["存期"] =cunqi
                            strs["到期日期"] =daoqiriqi
                            strs["续存存期"] =xucuncunqi
                            strs["状态"] =zhuangtai
                            # strs["操作"] =caozuo
                            # print(strs)
                            items.append(strs)
                        except:
                            pass
                    card_num = item["账号"]
                    # ss = Mysql_input()
                    # t2 = Thread(target=ss.set_data2, args=(i, items, card_num))
                    # print("启动线程2")
                    # t2.start()

                    ss = Mysql_input()
                    ss.set_data2(i,items,card_num)
                    print("卡{}余额信息:{}".format(i, items))


                    # print(items)
                    # print(cunkuan_xinxi)
                except:
                    # print("没找到")
                    pass
        print("账户信息:{}".format(zhanghu_items))

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

    def set_data(self,my_integral="900",bill="12月消费100积分"):
        self.connect()
        try:
            # sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
            sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
            self.cursor.execute(sql_1)
            self.conn.commit()
            print("成功添加至数据库!")
            res = self.cursor.fetchall()
            if res != None:
                self.close()
                return res
        except:
            self.conn.rollback()


    def set_data2(self,i,items,card_num):
        self.connect()
        for sa in range(10):
            try:
                my_item = items[sa]
                xuhao=my_item["序号"]
                chuzhong = my_item["储种"]
                bizhong= my_item["币种"]
                chaohui= my_item["钞汇"]
                yu_e= my_item["余额"]
                keyong_yue= my_item["可用余额"]
                kaihuriqi= my_item["开户日期"]
                cunqi= my_item["存期"]
                daoqiriqi= my_item["到期日期"]
                xucuncunqi= my_item["续存存期"]
                zhuangtai= my_item["状态"]
                print(my_item)
                print(yu_e)
                # print(zhuangtai)

                print("连接数据库")
                try:
                    # sql_1 = "INSERT INTO balance_info VALUES(null,'1','1','1','1','1','1','1','1','1','1','1','2');".format(card_num,xuhao,chuzhong,bizhong,chaohui,yu_e,keyong_yue,kaihuriqi,daoqiriqi)
                    sql_1 = "INSERT INTO balance_info VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(card_num,xuhao,chuzhong,bizhong,chaohui,yu_e,keyong_yue,kaihuriqi,cunqi,daoqiriqi,xucuncunqi,zhuangtai)
                    self.cursor.execute(sql_1)
                    self.conn.commit()
                    print("{}卡成功添加至数据库!".format(i))
                    res = self.cursor.fetchall()
                    # if res != None:
                    #     self.close()
                    #     return res
                except:
                    self.conn.rollback()

            except:
                pass



    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    ss = My_set()
    ss.get_nums()