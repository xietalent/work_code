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
        self.browser.get("https://www.iqiyi.com/iframe/loginreg?show_back=1&from_url=http://www.iqiyi.com/u/point")
        sleep(1)
        username,passwd = self.user_info()

        # iframe = self.browser.find_elements_by_tag_name("iframe")[0]
        # self.browser.switch_to.frame(iframe)
        # self.browser.switch_to.frame()

        self.browser.find_element_by_xpath("//div[@class='login-frame']//span[@class='fr']/a[1]").click()
        sleep(2)
        # login_way = input("请选择登录方式(1:密码登录/2:短信验证码):")
        login_way = "1"
        if login_way =="1":
            self.browser.find_element_by_xpath("//div[@class='login-frame-top']/div[@class='login-frame-ti']/div/div[2]/input[1]").send_keys(username)
            sleep(0.2)
            self.browser.find_element_by_xpath("//div[@class='login-frame']//input[@class='txt-info txt-password']").send_keys(passwd)
            sleep(0.2)
            self.browser.find_element_by_xpath("//div[@class='login-frame']//div[@class='login-frame-ti']/a[1]").click()
            sleep(2)
            try:
                vercode = Vercode(self.browser)
                vercode.start_vercode()
            except:
                pass
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
        username = "19128324901"
        # username = "15071469916"
        passwd = "zc006699"
        return username,passwd

    def passwd(self):
        passw = input('请输入短信验证码:')
        return passw

    def ver_code(self):

        pass

    #积分查询
    def my_score(self):
        # self.browser.find_element_by_xpath("//div[@class='center']//li[1]/dl/dt").click()
        # sleep(0.1)
        # #查询积分
        # self.browser.find_element_by_xpath("//ul[@class='rightNav']/li[1]/dl/dd/ul/li[2]/a").click()
        # WebDriverWait(self.browser,8,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'conRiTop')))
        # self.browser.find_element_by_class_name("select_txt").click()
        # sleep(0.1)
        # #积分生成记录,6个月
        # self.browser.find_element_by_xpath("//div[@class='option']/a[3]").click()
        # sleep(0.1)
        # self.browser.find_element_by_xpath("//div[@class='serch']//img").click()
        # sleep(4)

        score_html = self.browser.page_source
        score_tree = etree.HTML(score_html)

        #个人信息
        divs_a = score_tree.xpath("//div[@class='main_inner']")
        items_a = []
        for div in divs_a:
            item_a ={}
            #用户名
            username = div.xpath(".//div[@class='vt-user-info']/h2/a[@id='ucbannerName']/text()")[0].strip()
            #可用积分
            available_score = div.xpath(".//div[@class='vt-user-info']//a[2]/text()")[1].strip()
            #会员信息
            member_info = div.xpath(".//div[@class='vt-vip-growthLevel']/p[@class='vt-vip-info']/text()")[0].strip()
            # #积分限制券
            # score_xianzhi = div.xpath("./span[@id='coVouchersInfoSpan']/i/text()")[0].strip()

            print("用户名为:{}".format(username))
            print("可用积分数为:{}".format(available_score))
            print("会员信息:{}".format(member_info))
            # print("积分限制券数为:{}".format(score_xianzhi))



    #订单查询
    def my_settings(self):
        self.browser.find_element_by_xpath("//dd[6]//a[@class='link']/span[@class='menu-text']").click()
        sleep(5)
        #查询个人设置信息配置
        # self.browser.find_element_by_xpath("//li[@class='selecthover']/dl/dd/ul/li[1]/a").click()
        # sleep(4)
        order_html = self.browser.page_source
        order_tree = etree.HTML(order_html)
        divs_e = order_tree.xpath(".//div[@class='custom-main-wrapper-cols']")
        items_e = []
        for div in divs_e:
            try:
                item_e = {}
                #UID
                uid = div.xpath(".//div[@class='userSetting-item'][2]/span[@class='vl-inline']/text()")[0].strip()
                # order_number2 = order_number.split("：")[1]
                #性别
                gender = div.xpath(".//div[@class='userSetting-setWrap']/div[1]/span[3]/span/em[@class='c666']/text()")[0].strip()
                # #生日
                birthday = div.xpath(".//div[@class='userSetting-setWrap']/div[@class='userSetting-setWrap-item odd'][2]/span[3]/span/em[@class='c666']/text()")[0].strip()
                #
                print("UID:{}".format(uid))
                print("性别:{}".format(gender))
                print("生日:{}".format(birthday))
                # print("产品数量:{}".format(product_nums))
                # print("所需积分数:{}".format(score_needs))
                # print("合计花费积分数积分数:{}".format(score_pay))
                # print("订单渠道:{}".format(order_channel))
                # print("订单状态:{}".format(order_status))

            except:
                # none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
                #
                # print("{}".format(none_info))
                print("对不起,你最近没有订单")
            finally:
                pass
        sleep(0.1)

        #历史订单查询
        # self.browser.find_element_by_id("orderHistory").click()
        # sleep(0.1)
        # self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/select[@id='orderHistory']/option[2]").click()
        # sleep(0.1)
        # self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/a").click()
        # sleep(3)
        # order_his_html = self.browser.page_source
        # order_his_tree = etree.HTML(order_his_html)
        # divs_f = order_his_tree.xpath(".//div[@class='conRiContent']")
        # items_f = []
        # for div in divs_f:
        #     try:
        #         item_f = {}
        #         #订单详情
        #         #单价
        #         # 支付方式
        #         # 总额
        #         # 订单渠道
        #         # 订单状态
        #
        #         print("")
        #     except:
        #         none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
        #
        #         print("{}".format(none_info))
        #     finally:
        #         pass

    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'menu-text')))
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



class Vercode(object):
    def __init__(self,browser):
        self.browser = browser

    #模拟拖动
    def analog_drag(self):
        self.browser

        distance = 150
        self.start_move(distance)
        pass


    #点击移动按钮,开始移动
    def start_move(self, distance):
        #点击滑块滑动
        # element = self.browser.find_element_by_xpath("//div[@class='slide-bar']/div[@class='slide-block']")
        #点击小图片滑动
        element = self.browser.find_element_by_xpath("//div[@class='jigsaw']/div[@class='jigsaw-bg']/div[contains(@class,'jigsaw-block')]")

        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        distance -= element.size.get('width') / 2
        # distance += 15
        distance += 30

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
    time1 = time.clock()
    runs = Aiqiyi()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))