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


class Sasa(object):
    def __init__(self,timeout = None):
        self.timeout = timeout
        # self.chrome_options = Options()
        # self.chrome_options.add_argument('--headless')
        # self.logger = getLogger(__name__)
        # self.browser = webdriver.Chrome(chrome_options = self.chrome_options)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        # self.browser.get("http://www.tianhong.cn/integral_list.html?crt.categoryId=19819")
        self.browser.get("https://www.sasa.com/account/login")
        username,passwd = self.user_info()
        try:
            WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID, 'page_signin')))
        except:
            return  self.process_request()

        login_way = "1"
        #账户密码登录
        if login_way =="1":
            try:
                #获取图形验证码
                img_code = self.get_img()
                self.browser.find_element_by_xpath("//div[@class='signupbox']//li[1]/span/input").send_keys(username)
                sleep(0.1)
                self.browser.find_element_by_xpath("//div[@class='signupbox']//li[2]/span/input").send_keys(passwd)
                # self.browser.find_element_by_xpath("//div[@class='signupbox']//li[2]/span/inp").send_keys(passwd)
                sleep(0.1)
                self.browser.find_element_by_xpath("//div[@class='signupbox']//li[3]/span/input").send_keys(img_code)
                sleep(0.1)

                self.browser.find_element_by_xpath("//span[@class='form-act']/button").click()
            except Exception as e:
                print(e)

        else:
            pass
        sleep(1)

    def user_info(self):
        username = "19128324901"
        # username = "15071469916"
        passwd = "zc006699"
        return username,passwd

    def passwd(self):
        passw = input('请输入短信验证码:')
        return passw

    def get_img(self):

        imgs = input("请输入图形验证码:")
        return  imgs

    #积分查询
    def my_score(self):
        cookieDict = {}
        cookie = [item["name"] + "=" + item["value"] for item in self.browser.get_cookies()]
        for i in cookie:
            cookieDict[i.split('=')[0]] = i.split('=')[-1]
        print(cookieDict)
        sleep(0.1)
        self.browser.find_element_by_xpath("//ul[@id='loginBar']/li[@id='li3']/a").click()
        sleep(0.5)
        # 切换当前窗口
        # self.browser.switch_to.window(self.browser.window_handles[-1])
        # srech_window = self.browser.current_window_handle
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dk_side_menu')))

        score_html = self.browser.page_source
        score_tree = etree.HTML(score_html)
        #个人信息
        divs_a = score_tree.xpath("//div[@class='dk_user']")
        items_a = []
        for div in divs_a:
            item_a ={}
            #待付款
            pending_payment = div.xpath(".//div[@class='user_info_box02']/p[1]/a[1]/text()")[0].strip()
            #待评价
            comment = div.xpath(".//div[@class='user_info_box02']/p[1]/a[2]/text()")[0].strip()
            #通知
            notice =div.xpath(".//div[@class='user_info_box02']/p[1]/a[3]/text()")[0].strip()
            #可用购物券
            shopping_voucher = div.xpath(".//div[@class='user_info_box02']/p[2]/span[1]/a/text()")[0].strip()
            #我的积分
            my_points = div.xpath(".//div[@class='user_info_box02']/p[2]/span[2]/a/text()")[0].strip()
            #用户名
            #vip卡号
            #账户余额
            #

            print("待付款:{}".format(pending_payment))
            print("待评价:{}".format(comment))
            print("通知:{}".format(notice))
            print("可用购物券:{}".format(shopping_voucher))
            print("我的积分数为:{}".format(my_points))

        self.browser.find_element_by_xpath("//div[@class='dk_recent']/h3[@class='dk_tit02']/a").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'dk_user_data')))

        order_html = self.browser.page_source
        order_tree = etree.HTML(order_html)
        # 个人信息
        divs_a = order_tree.xpath("//div[@class='dk_user_data']")
        items_a = []
        for div in divs_a:
            item_a = {}
            # 订单商品
            # pending_payment = div.xpath(".//div[@class='user_info_box02']/p[1]/a[1]/text()")[0].strip()
            # 收货人
            # 订单金额
            # 下单时间
            # 订单装态
            # 操作

            # print("待付款:{}".format(pending_payment))
            # print("待评价:{}".format(comment))
            # print("通知:{}".format(notice))
            # print("可用购物券:{}".format(shopping_voucher))
            # print("我的积分数为:{}".format(my_points))
            try:
                no_order = div.xpath(".//td[@class='order_num']/text()")[0].strip()
                print(no_order)
            except:
                pass




    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'point')))
                print("登录成功")
                break
            except Exception as e:
                print(e)
        t2 = time.time()
        tres1 = t2-t1
        tres1 = round(tres1,2)
        print("登录过程耗时:{}s".format(tres1))
        sleep(1)

        # 积分信息
        self.my_score()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("获取积分信息耗时为:{}s".format(tres2))
        sleep(0.1)

        # 订单信息
        # self.my_settings()
        # t4 = time.time()
        # tres3 = t4 - t3
        # tres3 = round(tres3)
        # print("可订单信息耗时{}s".format(tres3))
        print("登录过程耗时:{}s".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        # print("可订单信息耗时{}s".format(tres3))
        return tres1





if __name__ == '__main__':
    time1 = time.clock()
    runs = Sasa()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))