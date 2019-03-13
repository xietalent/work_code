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
import json
import cv2
import numpy as np

class Tuniu(object):
    def __init__(self):
        # self.chrome_options = Options()
        # self.chrome_options.add_argument("--headless")
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.get("https://www.shangri-la.com/cn/corporate/golden-circle/gcsignin")
        self.browser.set_window_size(1200,800)
        try:
            WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID,"js-login-btn")))
        except Exception as e :
            print(e)
        # self.browser.find_element_by_class_name("line-name").click()
        sleep(1)
        username, passwd = self.user_info()
        try:
            self.browser.find_element_by_name("gcMemberId").send_keys(username)
            sleep(0.1)
            self.browser.find_element_by_name("password").send_keys(passwd)
            sleep(0.1)
            # img_code = self.get_img()
            # self.browser.find_element_by_id("identify").send_keys(img_code)
            sleep(0.1)
            self.browser.find_element_by_id("js-login-btn").click()
            sleep(20)
            try:
                self.get_vercode()
                vercode = Vercode(self.browser)
                vercode.start_vercode()
            except:
                pass
        except Exception as  e :
            print(e)

    def user_info(self):
        username = "1598749576@qq.com"
        passwd = "10hgzjcs"
        return username,passwd

    def get_img(self):
        img_code = input("请输入验证码")

        return img_code

    def get_vercode(self):
        # self.browser.find_element_by_xpath("//a[@class='geetest_link']/div[1]/div/canvas[1]")
        location = self.browser.find_element_by_xpath("//a[@class='geetest_link']/div[1]/div/canvas[1]").location
        self.browser.save_screenshot("ria.png")
        page_snap_obj = Image.open("ria.png")

        size = self.browser.find_element_by_xpath("//a[@class='geetest_link']/div[1]/div/canvas[1]").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        imgages = page_snap_obj.crop((left, top, right, bottom))
        imgages.save("imcode.png")

    def get_cookie(self):
        # 获取cookie
        cookies = self.browser.get_cookies()
        print(type(cookies))
        with open(r'E:\code\spiders_three\cookie_bag\shangrila_cook.txt', 'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(0.5)

    def req_tuniu(self):
        # 使用cookie模拟登录状态
        with open(r'E:\code\spiders_three\cookie_bag\shangrila_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
        cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
        print("cookie:{}".format(cookie))
        cookie_str = '; '.join(item for item in cookie)
        print("cookiestr:{}".format(cookie_str))
        # url = "http://www.tuniu.com/"
        # url = "https://i.tuniu.com/"
        url = "https://www.shangri-la.com/cn/corporate/golden-circle/gcsignin"
        headers = {
            'cookie': cookie_str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
        }
        tuniu_html = requests.get(url=url, headers=headers)
        with open(r"E:\code\spiders_three\text\tuniu_info.txt",'w',encoding="utf-8")  as fp:
            fp.write(tuniu_html.text)
            fp.close()
        # print(tuniu_html.text)

        my_info = tuniu_html.text
        with open(r"E:\code\spiders_three\text\tuniu_info.txt", 'r', encoding="utf-8") as f:
            html = f.read()

        html_tree = etree.HTML(html)
        my_info_tree = etree.HTML(tuniu_html)

        divs = my_info_tree.xpath("//div[@class='main-content']")
        print(divs)
        for div in divs:
            # 昵称
            nikename = div.xpath("//p[@id='user-name']/a/text()")[0].strip()
            # 优惠券
            coupon = div.xpath("//div[@class='header-right']/ul/li[1]/a[1]/div/p/b/text()")[0].strip()
            # 抵用券
            voucher = div.xpath("//div[@class='header-right']/ul/li[2]/a[1]/div/p/b/text()")[0].strip()
            # ;旅游券
            travel_voucher = div.xpath("//div[@class='header-right']/ul/li[1]/a[2]/div/p/b/text()")[0].strip()
            # 牛大头
            niudatou = div.xpath("//div[@class='header-right']/ul/li[2]/a[2]/div/p/b/text()")[0].strip()

            print("wod昵称为:{}".format(nikename))
            print("优惠券:{}".format(coupon))
            print("抵用券为:{}".format(voucher))
            print("旅游券为:{}".format(travel_voucher))
            print("牛大头数为:{}".format(niudatou))

    def my_points(self):
        self.browser.set_window_size(1200, 800)
        self.browser.get("https://www.shangri-la.com/cn/")
        with open(r'E:\code\spiders_three\cookie_bag\shangrila_cook.txt','r',encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("https://www.shangri-la.com/cn/")
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,"user-msg")))
        sleep(2)
        my_info_html = self.browser.page_source
        my_info_tree = etree.HTML(my_info_html)

        divs = my_info_tree.xpath("//div[@class='main-content']")
        for div in divs:
            #昵称
            nikename = div.xpath("//p[@id='user-name']/a/text()")[0].strip()
            #优惠券
            coupon = div.xpath("//div[@class='header-right']/ul/li[1]/a[1]/div/p/b/text()")[0].strip()
            #抵用券
            voucher = div.xpath("//div[@class='header-right']/ul/li[2]/a[1]/div/p/b/text()")[0].strip()
            #;旅游券
            travel_voucher = div.xpath("//div[@class='header-right']/ul/li[1]/a[2]/div/p/b/text()")[0].strip()
            #牛大头
            niudatou = div.xpath("//div[@class='header-right']/ul/li[2]/a[2]/div/p/b/text()")[0].strip()

            print("昵称为:{}".format(nikename))
            print("优惠券:{}".format(coupon))
            print("抵用券为:{}".format(voucher))
            print("旅游券为:{}".format(travel_voucher))
            print("牛大头数为:{}".format(niudatou))

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                # WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID,'searchSub')))
                print("登录结束")
                self.get_cookie()
                break
            except Exception as e:
                print(e)
        t2 = time.time()
        tres1 = t2 - t1
        tres1 = round(tres1, 2)
        print("请求登录耗时:{}".format(tres1))
        sleep(10)

        # 积分信息
        #requests请求
        # self.req_tuniu()
        #selenium请求
        self.my_points()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("获取积分信息耗时为:{}s".format(tres2))

class Vercode(object):
    def __init__(self,browser):
        self.browser = browser

    #模拟拖动
    def analog_drag(self):
        # self.browser
        distance = 265
        self.start_move(distance)

    #点击移动按钮,开始移动
    def start_move(self, distance):
        #点击滑块滑动
        # element = self.browser.find_element_by_xpath("//div[@class='slide-bar']/div[@class='slide-block']")
        #点击小图片滑动
        element = self.browser.find_element_by_xpath("//div[@class='geetest_slider_button']")

        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        distance -= element.size.get('width') / 2
        # distance += 15
        distance += 20

        # 按下鼠标左键
        ActionChains(self.browser).click_and_hold(element).perform()
        time.sleep(0.5)
        while distance > 0:
            if distance > 20:
                # 如果距离大于10，就让他移动快一点
                # span = random.randint(5, 8)
                span = random.randint(10, 15)
            else:
                # 快到缺口了，就移动慢一点
                span = random.randint(2, 3)
            ActionChains(self.browser).move_by_offset(span, 0).perform()
            distance -= span
            sleep(0.1)
            time.sleep(random.randint(5,25) / 100)

        ActionChains(self.browser).move_by_offset(distance, 1).perform()
        ActionChains(self.browser).release(on_element=element).perform()

    def start_vercode(self):
        self.analog_drag()


if __name__ == '__main__':
    running = Tuniu()
    running.start()