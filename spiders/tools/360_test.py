#
# from selenium import webdriver
# from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
# from scrapy.http import HtmlResponse
# from logging import getLogger
# from aip import AipOcr
# from time import sleep
# from selenium.webdriver.chrome.options import Options
# import lxml
# from lxml import etree
# import pytesseract
# import pytesseract.pytesseract
# from urllib import request
# from PIL import Image
# import time
#
# class SeleniumMiddleware():
#     def __init__(self,timeout=None,service_args=[]):
#         self.logger = getLogger(__name__)
#         self.timeout = timeout
#         # self.browser = webdriver.PhantomJS()
#         self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'
#
#         self.chrome_options = Options()
#         self.chrome_options.binary_location = self.browser_url
#         self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
#
#     def __del__(self):
#         self.browser.close()
#
#     # def process_request(self,request,spider):
#     def process_request(self):
#         self.logger.debug('PhantomJS is Starting')
#         # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
#
#         self.browser.get("https://www.baidu.com")
#         # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
#         sleep(3)
#         page_html = self.browser.page_source
#         print("当前网址"+self.browser.page_source)
#         # return page_html
#         sleep(2)
#
#         user_name = "大白菜"
#         passwd = "213154sdf"
#
#         self.browser.find_element_by_id("kw").send_keys(user_name)
#         sleep(2)
#         # self.browser.find_element_by_id("spnPassword").send_keys(passwd)
#         self.browser.find_element_by_id("su").click()
#         sleep(3)
#
#
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

__browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'  ##360浏览器的地址
chrome_options = Options()
chrome_options.binary_location = __browser_url

driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)
time.sleep(3)
driver.quit()
#
#
#
# if __name__ == '__main__':
#     s = SeleniumMiddleware()
#     s.process_request()
#
#
#
