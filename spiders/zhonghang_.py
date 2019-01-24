
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

# from  tools.zhaohang import keybord_DD

import time

class China_bank():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        # self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'
        # self.chrome_options = Options()
        # self.chrome_options.binary_location = self.browser_url
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('Ie is Starting')
        self.browser.get("https://jf365.boc.cn/BOCGIFTORDERNET/toLoginJsp.do?")
        sleep(3)




        page_html2 = self.browser.page_source
        print("当前网址"+self.browser.page_source)
        # return page_html



    def start_spider(self):
        print("开始")
        self.process_request()
        sleep(0.1)



if __name__ == '__main__':
    s = China_bank()
    s.start_spider()



