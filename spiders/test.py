
from selenium import webdriver
from logging import getLogger
from lxml import etree
from time import sleep
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image

import pymysql

browser = webdriver.Chrome()

browser.get("https://www.baidu.com")
# browser.get("https://personalbank.cib.com.cn/pers/main/login.do")

sleep(3)
#
try:
    browser.find_element_by_class_name('ui-label')
    ver_code = input("请输入验证码:")
    browser.find_element_by_name('mobilecaptchafield').send_keys(ver_code)
    sleep(3)

except:
    print("没这个节点,老铁再找找")

    browser.close()


# if browser.find_element_by_class_name('ui-label'):
#
#     ver_code = input("请输入验证码:")
#     browser.find_element_by_name('mobilecaptchafield').send_keys(ver_code)
#     sleep(3)
#
# else:
#     print("没这个节点,老铁再找找")
#
#     browser.close()

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
        login_method = input("登录方式(卡号/登录名):")

        if login_method == "卡号":
            self.card_num()
            # print("卡号登录")
        elif login_method == "登录名":
            print("将通过登录名+密码的方式登录")

        else:
            print("登录方式不对,请重新输入")
            self.process_request()



if __name__ == '__main__':
    ss = Xingye_C()
    ss.process_request()