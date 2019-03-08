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
import pytesseract
import pytesseract.pytesseract

class Aiqiyi(object):
    def __init__(self,timeout = None):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        self.browser.get("http://www.ewj.com/mobileApp/index.jsx#/loginPage")
        sleep(1)
        username,passwd = self.user_info()

        sleep(1)
        # login_way = input("请选择登录方式(1:密码登录/2:短信验证码):")
        login_way = "1"
        if login_way =="1":
            self.browser.find_element_by_xpath("//div[@class='clearfix']/input[@class='nostyle userid']").send_keys(username)
            sleep(0.2)
            self.browser.find_element_by_xpath("//section[@id='loginPage']//div[@class='border-bottom'][2]//input").send_keys(passwd)
            sleep(0.2)
            # imgs = self.get_img()
            # sleep(0.2)
            # self.browser.find_element_by_xpath("//div[@id='captcha']//input[@class='v_code']").send_keys(imgs)
            # sleep(0.1)
            self.browser.find_element_by_xpath("//section[@id='loginPage']//div/div[5]").click()
            sleep(3)
            self.browser.find_element_by_xpath("//section[@class='foot-nav']/ul/li[4]/a/span[1]").click()

        else:
            #短信验证码登录
            self.browser.find_element_by_xpath("//div[@class='login-frame']//span[@class='fr']/a[2]").click()
            sleep(2)
            self.browser.find_element_by_xpath("//div[@class='login-frame']//div[@class='login-frame-ti']/a[1]").click()
            sleep(2)
            #切换当前窗口
            self.browser.switch_to.window(self.browser.window_handles[-1])
            srech_window = self.browser.current_window_handle
            sleep(0.1)
            #点击
            self.browser.find_element_by_xpath("//div[@class='login-frame-top']/div[@class='login-frame-ti']/div[@class='info-container']//input[1]").send_keys(username)
            sleep(0.2)
            self.browser.find_element_by_xpath("//div[@class='login-step-con']/div[1]//div[@class='login-frame-ti']/a[1]").click()
            sleep(0.1)
            passw = self.passwd()
            # self.browser.find_element_by_xpath("//div[@class='login-frame-ti']//div[@class='tip-container']/input").send_keys(passw)
            # sleep(0.1)
            # self.browser.find_element_by_xpath("//div[@class='login-step-con']/div[2]//div[@class='login-frame-ti']/a[1]").click()
        sleep(2)

    def user_info(self):
        # username = "19128324901"
        username = "15071469916"
        passwd = "zc003399"
        return username,passwd

    def passwd(self):
        passw = input('请输入短信验证码:')
        return passw

    def get_img(self):
        imgs = input("请输入图形验证码:")
        return  imgs

    #积分查询
    def my_score(self):

        score_html = self.browser.page_source
        score_tree = etree.HTML(score_html)

        #个人信息
        divs_a = score_tree.xpath("//div[@id='user_panel']/div[@class='user_info']")
        items_a = []
        for div in divs_a:
            item_a ={}
            #用户名
            username = div.xpath(".//table/tbody/tr/td/span/text()")[0].strip()
            #可用积分
            available_score = div.xpath(".//span[@id='points']/a/text()")[0].strip()
            # #会员信息
            # member_info = div.xpath(".//div[@class='vt-vip-growthLevel']/p[@class='vt-vip-info']/text()")[0].strip()
            # #积分限制券
            # score_xianzhi = div.xpath("./span[@id='coVouchersInfoSpan']/i/text()")[0].strip()

            print("用户名为:{}".format(username))
            print("可用积分数为:{}".format(available_score))
            # print("会员信息:{}".format(member_info))
            # print("积分限制券数为:{}".format(score_xianzhi))


    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID, 'points')))
                print("登录成功")
                break
            except:
                pass
        t2 = time.time()
        tres1 = t2-t1
        tres1 = round(tres1,2)
        print("登录过程耗时:{}s".format(tres1))

        # 积分信息
        self.my_score()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("获取积分信息耗时为:{}s".format(tres2))
        sleep(0.1)

        # 订单信息
        self.my_settings()
        t4 = time.time()
        tres3 = t4 - t3
        tres3 = round(tres3)
        print("可订单信息耗时{}s".format(tres3))
        print("登录过程耗时:{}s".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        print("可订单信息耗时{}s".format(tres3))
        return tres1

if __name__ == '__main__':
    time1 = time.clock()
    runs = Aiqiyi()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))