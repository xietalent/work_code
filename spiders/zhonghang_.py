
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
import time

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'

        self.chrome_options = Options()
        self.chrome_options.binary_location = self.browser_url
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")

        self.browser.get("https://jf365.boc.cn/BOCGIFTORDERNET/toLoginJsp.do?")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(3)
        page_html2 = self.browser.page_source
        print("当前网址"+self.browser.page_source)
        # return page_html











if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()



