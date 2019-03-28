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


class Starbucks():
    def __init__(self):
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.get("https://www.starbucks.com.cn/account/#/")
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID,'username')))
        username,passwd = self.user_info()
        #尝试登陆
        try:
            self.browser.find_element_by_id("username").send_keys(username)
            self.browser.find_element_by_xpath("//div[@class='password-group-field']//div[@class='ok']/input").send_keys(passwd)
            sleep(0.5)
            img_code = self.get_img()
            self.browser.switch_to.frame(0)
            self.browser.find_element_by_id("capAns").send_keys(img_code)
            sleep(0.5)
            self.browser.find_element_by_id("submit").click()

            self.browser.switch_to.parent_frame()
            # sleep(5)
            #点击登录
            # self.browser.find_element_by_xpath("//button[@class='button large']/span").click()
        except Exception as e:
            print(e)

    def user_info(self):
        username = "luzaiyanshen"
        passwd = "Zc003388"
        return username,passwd

    def get_vercode(self):
        vercode = input("请输入短信验证码:")
        return vercode

    def get_img(self):
        img_code = input("请输入图形验证码:")
        return img_code

    def get_cookies(self):
        cookies = self.browser.get_cookies()
        with open(r"E:\code\spiders_three\cookie_bag\starbucks_cook.txt",'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()

    def req_parse(self):
        pass

    def account_info(self):
        self.browser.get("https://www.starbucks.com.cn/account/#/")
        with open(r"E:\code\spiders_three\cookie_bag\starbucks_cook.txt", 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("https://www.starbucks.com.cn/account/#/")
        sleep(3)
        # 消费记录
        self.browser.get("https://www.starbucks.com.cn/account/#/activity")
        sleep(3)
        # 账户中心
        self.browser.get("https://www.starbucks.com.cn/account/#/profile")

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'subcategories')))
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
    run = Starbucks()
    tres1 = run.start()
    time2 = time.time()
    time3 = time2-time1
    total_time = round(time3,2)
    time4 = round(total_time-tres1,2)
    print("总耗时:{}s".format(total_time))
    print("总耗时(去除登录时间后):{}s".format(time4))


