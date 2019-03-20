# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

import random
import time
import re
import requests
import time
import ctypes
import urllib
import urllib3
import pytesseract
import pytesseract.pytesseract
import json
import cv2
import numpy as np

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
from retrying import retry
# from tools.keybord_DD import DD_input



class Botao(object):
    def __init__(self,timeout=None):
        self.timeout = timeout
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,800)
        self.browser.get("http://m.99inn.cc/Index/Login?")
        usename, passwd = self.user_info()
        WebDriverWait(self.browser,5,1).until(EC.element_to_be_clickable((By.ID,"tabs-container")))
        # 选择登录方式
        # loginway = input("请选择登录方式(1,2):")
        loginway = "1"
        # 普通登录
        if loginway == "1":
            try:
                self.browser.find_element_by_xpath("//div[@class='swiper-wrapper']/div[1]/form/div[@class='row-input'][1]/input").send_keys(usename)
                sleep(0.1)
                self.browser.find_element_by_xpath("//div[@class='swiper-wrapper']/div[1]/form/div[@class='row-input'][2]/input").send_keys(passwd)
                sleep(0.1)

                self.browser.find_element_by_xpath("//div[@class='swiper-wrapper']/div[1]/form/button").click()
            except Exception as e:
                return e
        else:
            print("快捷登录")
            ver_code = input("请输入短信验证码:")

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
        with open(r'E:\code\spiders_three\cookie_bag\rujia_cook.txt', 'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(0.5)


    def account_info(self):
        self.browser.get("http://www.bthhotels.com/Member/Score")
        with open(r'E:\code\spiders_three\cookie_bag\rujia_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("http://www.bthhotels.com/Member/Score")
        sleep(3)
        self.browser.get("https://www.bthhotels.com/Member/CarbonScore")
        sleep(3)
        self.browser.get("https://www.bthhotels.com/Member/digitalcoupon")



    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                sleep(5)
                # WebDriverWait(self.browser,15,0.5).until(EC.element_to_be_clickable((By.ID,'userinfo')))
                # print("登录结束")
                self.get_cookie()
                break
            except Exception as e:
                print(e)
        t2 = time.time()
        tres1 = t2 - t1
        tres1 = round(tres1, 2)
        # print("请求登录耗时:{}".format(tres1))

        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("请求登录耗时:{}".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        return tres1


if __name__ == '__main__':
    time1 = time.clock()
    run = Botao()
    tres1 = run.start()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))
