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

        # 设置chrome浏览器无界面模式
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Ie()
        # self.phone_num = phone_num
        # self.passwd = passwd

    # def __del__(self):
    #     self.browser.close()

    def process_request(self):
        # username = input("请输入用户名:")
        # username = "15071469916"
        username = "530328199502132116"
        # username = "张雄"
        # passwd = input("请输入一账通密码:")
        passwd = "zc006688"
        self.logger.debug('Ie is Starting')

        self.browser.get("https://creditcard.pingan.com.cn/financing/login.screen?sid_source=CreditcardCP")

        sleep(3)



        #切换至iframe
        self.browser.switch_to.frame("toalogin")


        #获取验证码
        location = self.browser.find_element_by_id("validateImg").location
        self.browser.save_screenshot("./images/pingan/pingan_login.png")
        page_snap_obj = Image.open("./images/pingan/pingan_login.png")

        size = self.browser.find_element_by_id("validateImg").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        images = page_snap_obj.crop((left, top, right, bottom))
        # sleep(1)
        # images.save("imcode.png")
        # image1 = images.save("./static/img/imgcode.png")
        images.save("./images/pingan/pingan_imgcode.png")
        sleep(0.2)
        images.show()


        sleep(1)
        # location = self.browser.find_element_by_id("imgCode").location
        # self.browser.save_screenshot("./images/pingan/pingan_login1.png")

        self.browser.find_element_by_id('j_username').send_keys(username)
        sleep(1)
        self.browser.find_element_by_class_name("f30").click()
        sleep(1)
        self.browser.find_element_by_id('j_password').send_keys(passwd)
        sleep(1)
        print("密码")

        # self.browser.find_element_by_class_name("pa_ui_keyboard_close pa_ui_keyboard_key").click()
        # sleep(1)
        # print("ok")

        # self.browser.find_element_by_id('j_password').send_keys(passwd)

        sleep(1)




        #验证码
        ver_code = input("请输入验证码:")

        self.browser.find_element_by_id('check_code').send_keys(ver_code)

        self.browser.find_element_by_id('loginlink').click()

        sleep(3)
        #next


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

