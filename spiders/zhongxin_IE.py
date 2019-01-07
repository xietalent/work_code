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
        phone_num = "15071469916"
        # passwd = input("请输入密码:")
        passwd = "zc006688"
        self.logger.debug('Ie is Starting')

        self.browser.get("https://creditcard.ecitic.com/citiccard/ucweb/entry.do")
        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        # self.browser.save_screenshot("./images/login1.png")
        self.browser.find_element_by_id('phoneNbr').send_keys(phone_num)
        sleep(3)



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
            imgages.show()
            sleep(2)

            #添加机器识别

            img_code = input("请输入验证码:")
            self.browser.find_element_by_id('img_code_text')
            self.browser.find_element_by_id('imgvalicode').send_keys(img_code)
            sleep(1)
        except:
            pass
        finally:
            pass

        self.browser.find_element_by_id('getsms').click()
        #验证码
        ver_code = input("请输入手机验证码:")
        self.browser.find_element_by_id('valicode').send_keys(ver_code)
        sleep(2)

        #next
        self.browser.find_element_by_id('checkcode').click()
        sleep(2)

        # login
        self.browser.find_element_by_id('mm').send_keys(passwd)
        self.browser.find_element_by_id('login').click()

        self.browser.save_screenshot("./images/index.png")

        self.browser.find_element_by_xpath(".//div[@class='head']/div[@class='menu']//li[@class='yahei'][6]/a[@class='jffw']").click()

        self.browser.save_screenshot("./images/jifen_page.png")

        page_html = self.browser.page_source
        return page_html


    def parses(self):

        page_html = self.process_request()
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
    zhongx = Zhongxin_I()
    zhongx.parses()
