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

class Adidas():
    def __init__(self,timeout=None):
        self.browser = webdriver.Chrome()
        self.timeout = timeout

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1100,1000)
        self.browser.get("https://www.adidas.com.cn/member/login")
        usename, passwd = self.user_info()
        WebDriverWait(self.browser,5,1).until(EC.element_to_be_clickable((By.ID,"loginBtn")))
        # 普通登录
        sleep(0.5)
        try:
            self.browser.find_element_by_xpath("//div[@class='login-box-content']/a[2]/h4[1]").click()
            sleep(0.5)
            self.browser.find_element_by_id("loginName").send_keys(usename)
            sleep(0.1)
            #获取短信验证码
            self.browser.find_element_by_id("password").send_keys(passwd)
            # vercode = self.get_vercode()
            # self.browser.find_element_by_xpath("//div[@class='validation_hints']/a[1]").click()
            sleep(0.1)
            # self.browser.find_element_by_id("verifyCode").send_keys(vercode)
            sleep(0.1)
            self.browser.find_element_by_id("loginBtn").click()
        except Exception as e:
            return e

    def user_info(self):
        # username = input("请输入用户名")
        username = "19128324901"
        passwd = "zc003399"
        return username,passwd

    def get_vercode(self):
        vercode = input("请输入短信验证码:")
        return vercode

    def get_img(self):
        img_code = input("请输入图形验证码:")
        return img_code

    def get_cookie(self):
        # 获取cookie
        cookies = self.browser.get_cookies()
        print(type(cookies))
        with open(r'E:\code\spiders_three\cookie_bag\adidas_cook.txt', 'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(0.5)

    def req_IHG(self):
        # 使用cookie模拟登录状态
        with open(r'E:\code\spiders_three\cookie_bag\adidas_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
        cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
        print("cookie:{}".format(cookie))
        cookie_str = '; '.join(item for item in cookie)
        print("cookiestr:{}".format(cookie_str))

        url = "https://www.adidas.com.cn/myAccount/point?locale=zh_CN"
        headers = {
            'cookie': cookie_str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        tuniu_html = requests.get(url=url, headers=headers)
        with open(r"E:\code\spiders_three\text\adidas_info.txt", 'w', encoding="utf-8")  as fp:
            fp.write(tuniu_html.text)
            fp.close()
        print(tuniu_html.text)
        # my_info = tuniu_html.text

        with open(r"E:\code\spiders_three\text\adidas_info.txt", 'r', encoding="utf-8") as f:
            html = f.read()
        html_tree = etree.HTML(html)
        # my_info_tree = etree.HTML(html_tree)
        divs = html_tree.xpath("//div[@class='main-content']")
        print(divs)
        for div in divs:
            pass

    def account_info(self):
        self.browser.get("https://www.adidas.com.cn/myAccount/point?locale=zh_CN")
        with open(r'E:\code\spiders_three\cookie_bag\adidas_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("https://www.adidas.com.cn/myAccount/point?locale=zh_CN")
        sleep(3)
        #我的优惠券
        self.browser.get("https://www.adidas.com.cn/myAccount/coupons?locale=zh_CN")
        sleep(3)
        #我的订单
        self.browser.get("https://www.adidas.com.cn/orderHistory?orderType=0&locale=zh_CN")

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                sleep(3)
                # WebDriverWait(self.browser,15,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'save_btn')))
                # print("登录结束")
                self.get_cookie()
                break
            except Exception as e:
                print(e)
        t2 = time.time()
        tres1 = t2 - t1
        tres1 = round(tres1, 2)
        # print("请求登录耗时:{}".format(tres1))

        # self.req_IHG()
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("请求登录耗时:{}".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        return tres1


if __name__ == '__main__':
    time1 = time.clock()
    run = Adidas()
    tres1 = run.start()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))
