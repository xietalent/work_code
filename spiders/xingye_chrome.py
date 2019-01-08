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


class Xingye_C():
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


    def card_num(self):
        print("卡号登录")
        card_nums = input("请输入卡号:")

        page_html = self.browser.page_source
        return page_html

    def username(self):
        print("将通过登录名+密码的方式登录")
        # username = input("请输入登录名:")
        username = "15071469916"
        # passwd = input("请输入登录密码:")
        passwd = "zc006688"
        self.logger.debug('Ie is Starting')
        self.browser.get("https://personalbank.cib.com.cn/pers/main/login.do")

        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        my_cookie = self.browser.get_cookies()
        print(my_cookie)

        # self.browser.find_element_by_class_name('login-type-label').click()
        self.browser.find_element_by_xpath(".//div[@class='wrap']//form[@id='loginForm']//li[3]/label").click()
        sleep(2)
        self.browser.save_screenshot("./images/xylogin1.png")
        # self.browser.find_element_by_xpath('j_username').send_keys(username)
        self.browser.find_element_by_id('loginNameTemp').send_keys(username)

        # self.browser.find_elements_by_link_text()
        sleep(3)
        buttons = self.browser.find_element_by_id('iloginPwd').send_keys(passwd)
        # sleep(5)
        # for button in buttons:
        #     if button.text == "Post":
        #         button.click()
        # sleep(3)

        # 验证码
        # ver_code = input("请输入验证码:")
        # self.browser.find_element_by_id('check_code').send_keys(ver_code)
        # self.browser.find_element_by_id('mobilecaptchafield').send_keys(ver_code)

        self.browser.find_element_by_id('loginSubmitBtn').click()

        # next
        sleep(3)
        self.browser.save_screenshot("./images/jifen_page.png")
        page_html = self.browser.page_source
        return page_html



    def process_request(self):
        # login_method = input("登录方式(卡号/登录名):")
        login_method = "卡号"

        if login_method == "卡号":
            page_html = self.card_num()

        elif login_method == "登录名":
            page_html = self.username()

        else:
            print("登录方式不对,请重新输入")
            self.process_request()


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
    zx = Xingye_C()
    zx.process_request()

