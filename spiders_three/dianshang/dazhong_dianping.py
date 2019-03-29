# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

import lxml
import time
import json
import selenium
import requests
import re
import random

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


class DazhongDianping():
    def __init__(self,loginway=2,timeout=None):
        self.browser = webdriver.Chrome()
        self.timeout = timeout
        self.loginway = loginway

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        self.browser.get("https://account.dianping.com/login?redir=http://www.dianping.com")
        usename, passwd = self.user_info()

        WebDriverWait(self.browser,5,1).until(EC.element_to_be_clickable((By.CLASS_NAME,"mid-out")))
        sleep(0.5)
        self.browser.switch_to.frame(0)
        self.browser.find_element_by_class_name("icon-pc").click()
        # sleep(5)
        if self.loginway == 1:
            # 普通登录
            sleep(0.5)
            try:
                self.browser.find_element_by_id("tab-account").click()
                sleep(0.2)
                self.browser.find_element_by_id("account-textbox").send_keys(usename)
                sleep(0.1)
                # 密码
                self.browser.find_element_by_id("password-textbox").send_keys(passwd)
                sleep(0.1)
                self.browser.find_element_by_id("login-button-account").click()
            except Exception as e:
                return e
        elif self.loginway == 2:
            #动态验证码登录
            try:
                self.browser.find_element_by_id("mobile-number-textbox").send_keys(usename)
                sleep(0.1)
                self.browser.find_element_by_id("send-number-button").click()
                ver_code = self.get_vercode()
                self.browser.find_element_by_id("number-textbox").send_keys(ver_code)
                sleep(0.1)
                self.browser.find_element_by_id("login-button-mobile").click()
            except Exception as e:
                print(e)
        else:
            print("没有这种登录方式,bye")

    def user_info(self):
        # username = input("请输入用户名")
        username = "15071469916"
        passwd = "zx150219"
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
        print(cookies)
        print(type(cookies))
        with open(r'E:\code\spiders_three\cookie_bag\dianping_cook.txt', 'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(0.5)

    def req_dianping(self):
        # 使用cookie模拟登录状态
        with open(r'E:\code\spiders_three\cookie_bag\dianping_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
        cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
        print("cookie:{}".format(cookie))
        cookie_str = '; '.join(item for item in cookie)
        print("cookiestr:{}".format(cookie_str))

        url = "http://www.dianping.com/member/836391532"
        headers = {
            'cookie': cookie_str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        tuniu_html = requests.get(url=url, headers=headers)
        with open(r"E:\code\spiders_three\text\dianping_info.txt", 'w', encoding="utf-8")  as fp:
            fp.write(tuniu_html.text)
            fp.close()
        print(tuniu_html.text)
        # my_info = tuniu_html.text

        # with open(r"E:\code\spiders_three\text\dianping_info.txt", 'r', encoding="utf-8") as f:
        #     html = f.read()
        # html_tree = etree.HTML(html)
        # my_info_tree = etree.HTML(html_tree)
        # divs = html_tree.xpath("//div[@class='main-content']")
        # print(divs)
        # for div in divs:
        #     pass

    def account_info(self):
        self.browser.get("http://www.dianping.com/member/836391532")
        with open(r'E:\code\spiders_three\cookie_bag\dianping_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("http://www.dianping.com/member/836391532")
        sleep(3)
        #收藏
        self.browser.get("http://www.dianping.com/member/836391532/wishlists")
        sleep(3)
        #点评
        self.browser.get("http://www.dianping.com/member/836391532/reviews")

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                WebDriverWait(self.browser,15,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'has-child')))
                # print("登录结束")
                self.get_cookie()
                break
            except Exception as e:
                print(e)
                break
        t2 = time.time()
        tres1 = t2 - t1
        tres1 = round(tres1, 2)
        # print("请求登录耗时:{}".format(tres1))

        # self.req_dianping()
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("请求登录耗时:{}".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        return tres1

if __name__ == '__main__':
    time1 = time.time()
    run = DazhongDianping()
    tres1 = run.start()
    time2 = time.time()
    time3 = time2 - time1
    total_time = round(time3, 2)
    time4 = round(total_time - tres1, 2)
    print("总耗时:{}s".format(total_time))
    print("总耗时(去除登录时间后):{}s".format(time4))