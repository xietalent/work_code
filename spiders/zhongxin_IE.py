from selenium import webdriver
from logging import getLogger
from aip import AipOcr
from time import sleep
from selenium.webdriver.chrome.options import Options
import lxml
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image

import pymysql
import time

class Zhongxin_I():
    def __init__(self,timeout=None):
    # def __init__(self,phone_num,passwd,timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Ie()
        self.browser = webdriver.Chrome()
        # self.phone_num = phone_num
        # self.passwd = passwd


    def __del__(self):
        self.browser.close()


    def process_request(self):
        # phone_num = input("请输入手机号码:")
        # passwd = input("请输入密码:")
        account = input("用谁的账户(1/2):")


        if account == "1":
            phone_num = "15071469916"
            passwd = "zc006688"
            #0755-27066666
        else:
            phone_num = "13728647735"
            passwd = "419078chu"
            print("陈")


        # self.logger.debug('Ie is Starting')
        self.logger.debug('Chromee is Starting')

        self.browser.get("https://creditcard.ecitic.com/citiccard/ucweb/entry.do")
        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        # self.browser.save_screenshot("./images/login1.png")
        self.browser.find_element_by_id('phoneNbr').send_keys(phone_num)
        sleep(3)
        t1 = time.time()
        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("randImage").location
            self.browser.save_screenshot("./images/zx_login1.png")
            page_snap_obj = Image.open("./images/zx_login1.png")

            size = self.browser.find_element_by_id("randImage").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))
            #获取到验证码截图
            imgages.save("./images/zx_imcode.png")
            # imgages.show()
            sleep(1)
            #添加机器识别
            img_code = input("请输入验证码:")
            self.browser.find_element_by_id('img_code_text')
            self.browser.find_element_by_id('imgvalicode').send_keys(img_code)
            sleep(1)
        except:
            pass
        finally:
            pass
        t2 = time.time()
        tres = t2-t1
        print("验证码耗时:{}".format(tres))

        t3 = time.time()
        self.browser.find_element_by_id('getsms').click()
        #验证码
        ver_code = input("请输入手机验证码:")
        self.browser.find_element_by_id('valicode').send_keys(ver_code)
        sleep(0.5)


        #next
        self.browser.find_element_by_id('checkcode').click()
        sleep(2)
        t4 = time.time()
        tres2 = t4-t3
        tres2 = round(tres2,2)
        print("手机验证码耗时:{}".format(tres2))

        # login
        self.browser.find_element_by_id('mm').send_keys(passwd)
        t5 = time.time()
        self.browser.find_element_by_id('login').click()
        sleep(1)
        self.browser.save_screenshot("./images/index.png")

        # self.browser.find_element_by_xpath("//div[@class='wrap']/div[@class='head']/div[@class='menu']/ul/li[@class='yahei'][6]/a[@class='jffw']").click()
        t6 = time.time()
        tres3 = t6 - t5
        tres3 = round(tres3, 2)
        print("登录耗时:{}".format(tres3))

        t7 = time.time()
        self.browser.find_element_by_xpath("//div[@class='wrap']/div[@class='head']/div[@class='menu']/ul/li[@class='yahei'][5]/a[@class='jffw']").click()

        self.browser.save_screenshot("./images/jifen_page.png")

        page_html = self.browser.page_source
        t8 = time.time()
        tres4 = t8-t7
        tres4 = round(tres4, 2)
        print("积分页耗时{}".format(tres4))

        t9 = time.time()
        sleep(2)
        try:
            self.browser.find_element_by_link_text("兑换明细").click()
            print("1起效了")
        except:
            self.browser.find_element_by_xpath("//div[@class='wrap']/div[@class='main']/div[@class='sub_menu']/a[3]").click()
            print("1没效果")
        finally:
            pass
        sleep(2.5)

        try:
            self.browser.find_element_by_xpath("//div[@class='wrap']//div[@class='sl_data_a mt_10'][1]/div[@class='dh_link']/a[@href][3]").click()
            # self.browser.find_element_by_xpath("//div[@class='wrap']//div[@class='sl_data_a mt_10'][1]/div[@class='dh_link']/a[@id='last1Year']").click()
            print("路径")
        except:
            self.browser.find_element_by_link_text("1年").click()
            print("text生效")
        finally:
            pass

        t10 = time.time()

        tres5 = t10-t9
        tres5 = round(tres5,2)
        print("消费明细获取时间:{}".format(tres5))
        page_html2 = self.browser.page_source
        return page_html,page_html2



    def parses(self):
        t1 = time.clock()
        page_html,page_html2 = self.process_request()
        items = []
        response = etree.HTML(page_html)
        divs = response.xpath(".//div[@class='main']")
        for div in divs:
            item={}
            score = div.xpath(".//div[@class='table_mx score_jf_table']//tbody/tr[2]/td[1]/text()")[0]
            score = str(score).strip("['']")
            print("您当前可用积分为:"+score)
            print(type(score))
            # score = div.xpath(".//div[@class='table_mx score_jf_table']//tbody/tr[2]/td[1]")[0].strip()
            # ex_score = div.xpath("")
            item["score"] = score
            items.append(item)

        sleep(3)

        response2 = etree.HTML(page_html2)
        divs = response2.xpath(".//div[@class='wrap']/div[@id='oper_content']")
        for div in divs:
            item = {}
        #     # record = div.xpath("//div[@class='mt_10']/div[@id='exchange_list']//tbody/tr[2]/td")
            record = div.xpath(".//div[@class='mt_10']/div[@id='exchange_list']//tbody/tr[2]/td/text()")[0]
            record = str(record).strip("['']")
            print("record"+record)
            print(type(record))
            item["record"] = record
            items.append(item)

        print(items)
        t2 = time.clock()
        t2 = round(t2,2)
        print("解析时间".format(t2))
        my_integral = score
        bill = record


        # 普通方式
        # ss = Mysql_input()
        # ss.set_data(my_integral, bill )
        # self.browser.quit()

        # return my_integral, bill







#数据库连接
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

    def set_data(self,my_integral="12300",bill="12月消费800积分"):
        self.connect()
        try:
            sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
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
    t1 = time.clock()
    zhongx = Zhongxin_I()
    zhongx.parses()
    t2 = time.clock()
    t3 = round(t2, 2)
    print("本次数据获取耗时:{}s".format(t3))

