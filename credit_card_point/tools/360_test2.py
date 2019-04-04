
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
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
from pykeyboard import PyKeyboard
from pymouse import PyMouse

import time
import os


class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # option = webdriver.ChromeOptions()
        # option.add_argument('--headless')
        # self.browser = webdriver.Chrome360(chrome_options=option)
        # self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome360()
        # self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'
        # 'User-Agent'='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"')
        # self.chrome_options = Options()
        # self.chrome_options.binary_location = self.browser_url
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)

    # def __del__(self):
    #     self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        print("开始")
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
        #
        self.browser.get("https://user.cmbchina.com/User/Login")
        # self.browser.get("https://www.baidu.com/")

        #农行:
        # self.browser.get("https://perbank.abchina.com/EbankSite/startup.do?r=6FD4F769ED09906B")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(3)
        # page_html = self.browser.page_source
        # print("当前网址"+self.browser.page_source)

        sleep(2)

        #启动输入密码
        main1 = r"D:\installMy\my_script\login_1.exe"
        ss = os.system(main1)
        print(ss.__abs__())


        sleep(5)










        # k = PyKeyboard()
        # # k.tab_key(k.enter_key)
        #
        # time.sleep(2)
        # k.type_string('sds123')
        #
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # time.sleep(2)
        # k.type_string('helloworld!')
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # time.sleep(2)
        # k.type_string('helloworld!')
        # k.tab_key(k.space_key)
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # time.sleep(2)
        # k.type_string('helloworld!')
        # k.tab_key(k.space_key)
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # time.sleep(2)
        # k.type_string('helloworld!')
        # k.tab_key(k.space_key)
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # sleep(2)
        # k.type_string('helloworld!')
        # k.tab_key(k.space_key)
        # k.press_key(k.tab_key)
        # k.release_key(k.tab_key)
        # sleep(2)
        # k.type_string('helloworld!')
        # # k.tab_key(k.enter_key)
        # print("pykeyboar")
        #
        #     # '''输入一串英文'''
        # # ss = k.return_key
        # s = "helloworld!"
        # for i in s:
        #     sleep(0.1)
        #     k.tap_key(i)
        #     # k.press_key(i)
        #     # k.release_key(i)
        #     # k.type_string('helloworld!')
        # # k.tab_key(ss)
        # sleep(2)
        # print("pykeyboar结束")
        # html = self.browser.execute_script("return document.documentElement.outerHTML")

        # html = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")

        # print(html)


        print("aaa")

        user_name = "5456465465465"
        passwd = "213154sdf"

        self.browser.find_element_by_id("spnLoginName").send_keys(user_name)
        sleep(0.2)
        self.browser.find_element_by_id("spnPassword").send_keys(passwd)







if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()



