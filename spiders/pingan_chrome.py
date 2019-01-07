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


class Pingan_C():
    def __init__(self,timeout=None):
    # def __init__(self,phone_num,passwd,timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome()
        # self.phone_num = phone_num
        # self.passwd = passwd

    def __del__(self):
        self.browser.close()

    def process_request(self):
        username = input("请输入用户名:")
        passwd = input("请输入一账通密码:")
        self.logger.debug('Ie is Starting')

        self.browser.get("https://creditcard.pingan.com.cn/financing/login.screen?sid_source=CreditcardCP")

        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        self.browser.save_screenshot("./images/login1.png")
        self.browser.find_element_by_xpath('j_username').send_keys(username)
        self.browser.find_elements_by_link_text()
        # self.browser.find_element_by_id('j_username').send_keys(username)
        sleep(1)




        #验证码
        ver_code = input("请输入验证码:")
        self.browser.find_element_by_id('check_code').send_keys(ver_code)

        self.browser.find_element_by_id('loginlink').click()


        #next


        self.browser.save_screenshot("./images/jifen_page.png")

        page_html = self.browser.page_source

        items = []
        response = etree.HTML(page_html)





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

    def set_data(self,my_integral="900",bill="12月消费100积分"):
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
    zx = Pingan_C()
    zx.process_request()

