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

class Bailian():
    def __init__(self,timeout=None):
        self.browser = webdriver.Chrome()
        self.timeout = timeout
        self.logger = getLogger(__name__)
        # self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(chrome_options = self.chrome_options)

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        self.browser.get("https://passport.bl.com/")
        usename, passwd = self.user_info()
        WebDriverWait(self.browser,5,1).until(EC.element_to_be_clickable((By.ID,"loginId")))
        # 普通登录
        sleep(0.5)
        try:
            self.browser.find_element_by_id("loginId").send_keys(usename)
            sleep(0.1)
            #密码
            self.browser.find_element_by_id("password").send_keys(passwd)
            #获取图形验证码
            img_code = self.get_img()
            sleep(0.1)
            self.browser.find_element_by_id("verifyCode").send_keys(img_code)
            sleep(0.1)
            self.browser.find_element_by_id("loginsubmit").click()
        except Exception as e:
            return e
        sleep(0.5)
        #如果有提示修改密码,点击取消
        try:
            self.browser.find_element_by_id("j-password-close").click()
        except:
            pass
        #
        sleep(0.1)
        try:
            self.browser.find_element_by_xpath("//div[@id='adv-show']/a[@class='close']").click()
        except:
            pass
        #切换个人主页
        # self.browser.find_element_by_id("member_name").click()
        # sleep(5)
        # self.browser.switch_to.window(self.browser.window_handles[-1])


    def user_info(self):
        # username = input("请输入用户名")
        username = "15071469916"
        passwd = "zc003399"
        return username,passwd

    def get_vercode(self):
        vercode = input("请输入短信验证码:")
        return vercode

    def get_img(self):
        img_code = input("请输入图形验证码:")
        return img_code
        # return img_code

    def get_cookie(self):
        # 获取cookie
        cookies = self.browser.get_cookies()
        print(type(cookies))
        with open(r'E:\code\spiders_three\cookie_bag\bailian_cook.txt', 'w') as fp:
            fp.write(json.dumps(cookies))
            fp.close()
        sleep(0.5)

    def req_bailian(self):
        # 使用cookie模拟登录状态
        with open(r'E:\code\spiders_three\cookie_bag\bailian_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
        cookie = [item["name"] + "=" + item["value"] for item in list_cookies]
        print("cookie:{}".format(cookie))
        cookie_str = '; '.join(item for item in cookie)
        print("cookiestr:{}".format(cookie_str))

        url = "https://my.bl.com/ym/nl/memberPointList.html"
        headers = {
            'cookie': cookie_str,
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
        }
        tuniu_html = requests.get(url=url, headers=headers)
        with open(r"E:\code\spiders_three\text\bailian_info.txt", 'w', encoding="utf-8")  as fp:
            fp.write(tuniu_html.text)
            fp.close()
        print(tuniu_html.text)
        # my_info = tuniu_html.text

    def account_info(self):
        self.browser.get("https://my.bl.com/ym/nl/memberPointList.html")
        with open(r'E:\code\spiders_three\cookie_bag\bailian_cook.txt', 'r', encoding='utf-8') as fp:
            list_cookies = json.loads(fp.read())
            for c in list_cookies:
                self.browser.add_cookie(c)
        self.browser.get("https://my.bl.com/ym/nl/memberPointList.html")
        sleep(3)
        #我的订单
        self.browser.get("https://my.bl.com/ym/orderList.html")
        sleep(3)
        #我的余额
        self.browser.get("https://my.bl.com/ym/mybalance.html")
        sleep(3)
        #电子卡券
        self.browser.get("https://my.bl.com/center/series/myCoupon.html")

    def start(self):
        t1 = time.time()
        while True:
            self.process_request()
            try:
                # WebDriverWait(self.browser,15,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'hd_login')))
                print("登录结束")
                self.get_cookie()
                break
            except Exception as e:
                print(e)
                break
        t2 = time.time()
        tres1 = t2 - t1
        tres1 = round(tres1, 2)
        # print("请求登录耗时:{}".format(tres1))

        self.req_bailian()
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("请求登录耗时:{}".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        return tres1

class Vercode(object):
    def __init__(self,browser):
        self.browser = browser

    #模拟拖动
    def analog_drag(self):
        distance = 200
        self.start_move(distance)
        pass

    #点击移动按钮,开始移动
    def start_move(self, distance):
        #点击滑块滑动
        # element = self.browser.find_element_by_xpath("//div[@class='slide-bar']/div[@class='slide-block']")
        #点击小图片滑动
        element = self.browser.find_element_by_id("nc_1_n1z")

        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        distance -= element.size.get('width') / 2
        # distance += 15
        distance += 100

        # 按下鼠标左键
        ActionChains(self.browser).click_and_hold(element).perform()
        time.sleep(0.5)
        while distance > 0:
            if distance > 10:
                # 如果距离大于10，就让他移动快一点
                # span = random.randint(5, 8)
                span = random.randint(10, 15)
            else:
                # 快到缺口了，就移动慢一点
                span = random.randint(2, 3)
            ActionChains(self.browser).move_by_offset(span, 0).perform()
            distance -= span
            time.sleep(random.randint(10, 50) / 100)

        ActionChains(self.browser).move_by_offset(distance, 1).perform()
        ActionChains(self.browser).release(on_element=element).perform()

    def start_vercode(self):

        self.analog_drag()


if __name__ == '__main__':
    time1 = time.time()
    run = Bailian()
    tres1 = run.start()
    time2 = time.time()
    time3 = time2 - time1
    total_time = round(time3, 2)
    time4 = round(total_time - tres1, 2)
    print("总耗时:{}s".format(total_time))
    print("总耗时(去除登录时间后):{}s".format(time4))