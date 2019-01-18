
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from logging import getLogger
from aip import AipOcr
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys

import lxml
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image
import time

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Chrome()

        # self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'

        # 'User-Agent'='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'

        self.options = webdriver.ChromeOptions()
        self.options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"')
        # self.chrome_options = Options()
        # self.chrome_options.binary_location = self.browser_url
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser = webdriver.Chrome360(chrome_options=self.options)

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")

        # self.browser.get("https://user.cmbchina.com/User/Login")
        self.browser.get("https://pbsz.ebank.cmbchina.com/CmbBank_GenShell/UI/GenShellPC/Login/Login.aspx?logintype=C")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(4)
        page_html = self.browser.page_source
        print("当前网址"+self.browser.page_source)

        sleep(2)

        html = self.browser.execute_script("return document.documentElement.outerHTML")

        html = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")

        print(html)

        user_name = "13728647735"
        passwd = "419078"

        self.browser.find_element_by_id("spnLoginName").click()
        self.browser.find_element_by_id("spnLoginName").send_keys(Keys.CONTROL,'a')
        # self.browser.find_element_by_id("spnLoginName").send_keys(user_name)
        sleep(3)
        self.browser.find_element_by_id("spnPassword").send_keys(passwd)




if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()
    del s



