# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import  getLogger
from lxml import etree
from aip import  AipOcr
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
from PIL import Image
from urllib import request,response
# from tools.keybord_DD import DD_input

import random
import time
import re
import requests
import time
import ctypes
import urllib
import urllib3
import json
import pytesseract
import pytesseract.pytesseract
import requests


class Cookie_login():
    def __init__(self):
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        # self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome(chrome_options = self.chrome_options)
        # self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    #获取cookie
    def get_cookie(self):
        self.browser.get("https://i.qq.com/")
        sleep(0.2)
        self.browser.switch_to.frame("login_frame")
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@id='bottom_qlogin']/a").click()
        sleep(0.5)
        self.browser.find_element_by_id("u").send_keys("2235110071")
        self.browser.find_element_by_id("u").send_keys("159")
        sleep(0.1)
        passwd = input("请输入密码:")
        self.browser.find_element_by_id("p").send_keys("qazwsx123{}".format(passwd))
        # self.browser.find_element_by_id("p").send_keys("")
        sleep(0.1)
        self.browser.find_element_by_id("login_button").click()
        sleep(5)

        print(self.browser.current_url)
        cookies = self.browser.get_cookies()
        print(type(cookies))
        with open('cook.txt','w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(5)

    #使用cookie模拟登录状态
    def use_cookie(self):
        with open('cook.txt','r') as fp:
            cookie = fp.read()
            cookie = json.loads(cookie)
            for c in cookie:
                self.browser.add_cookie(c)
        self.browser.refresh()

        with open('cook.txt','r',encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
        cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
        print("cookie:{}".format(cookie))
        cookie_str = '; '.join(item for item in cookie)
        print("cookiestr:{}".format(cookie_str))
        # url = "https://user.qzone.qq.com/2235110071"
        url = "https://user.qzone.qq.com/1598749576"
        headers = {
            'cookie':cookie_str,
            'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        qz_html = requests.get(url=url,headers = headers)
        print(qz_html.text)

    def start(self):
        self.get_cookie()
        sleep(0.5)
        self.use_cookie()
        sleep(10)

if __name__ == '__main__':
    running = Cookie_login()
    running.start()
