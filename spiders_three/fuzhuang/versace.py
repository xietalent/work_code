# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

import lxml
import time
import json
import selenium
import requests
import re

from selenium import webdriver
from time import sleep
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
from retrying import retry


class Versace():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.get("https://www.versace.cn/zh-cn/%E6%88%91%E7%9A%84%E8%B4%A6%E6%88%B7/")
        # WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'form-button')))
        username,passwd = self.user_info()
        #尝试登陆
        try:
            self.browser.find_element_by_xpath("//input[@id='dwfrm_login_username']").send_keys(username)
            sleep(0.1)
            self.browser.find_element_by_xpath("//input[@id='dwfrm_login_password']").send_keys(passwd)
            sleep(0.5)
            self.browser.find_element_by_class_name("//form[@id='dwfrm_login']/div[4]/button").click()
            # sleep(5)
            #点击登录
            # self.browser.find_element_by_xpath("//button[@class='button large']/span").click()
        except Exception as e:
            print(e)

    def user_info(self):
        username = "1598749576@qq.com"
        passwd = "Zc003399"
        return username,passwd

    def get_vercode(self):
        vercode = input("请输入短信验证码:")
        return vercode

    def get_img(self):
        img_code = input("请输入图形验证码:")
        return img_code

    def get_cookies(self):
        cookies = self.browser.get_cookies()
        with open(r"E:\code\spiders_three\cookie_bag\givenchy_cook.txt",'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()

    def req_parse(self):
        pass

    def account_info(self):
        self.browser.get("https://www.givenchy.com/apac/zh/myaccount?loginprocess=true")
        with open(r"E:\code\spiders_three\cookie_bag\givenchy_cook.txt", 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("https://www.givenchy.com/apac/zh/myaccount?loginprocess=true")

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                # WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'subcategories')))
                sleep(5)
                self.get_cookies()
                break
            except Exception as e :
                print(e)
        t2 = time.time()
        tres1 =t2- t1
        tres1 = round(tres1,2)
        # print("请求登录耗时为:{}s".format(tres1))

        # self.req_parse()
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("请求登录耗时:{}".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        return tres1


if __name__ == '__main__':
    time1 = time.time()
    run = Versace()
    tres1 = run.start()
    time2 = time.time()
    time3 = time2-time1
    total_time = round(time3,2)
    time4 = round(total_time-tres1,2)
    print("总耗时:{}s".format(total_time))
    print("总耗时(去除登录时间后):{}s".format(time4))


