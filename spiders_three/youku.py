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

class Youku(object):
    def __init__(self,timeout = None):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()
        # self.browser.quit()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        self.browser.get("http://point.youku.com/page/mall/index")
        sleep(1)
        #获取用户名,密码
        username,passwd = self.user_info()

        # iframe = self.browser.find_elements_by_tag_name("iframe")[0]
        # self.browser.switch_to.frame(iframe)
        # self.browser.switch_to.frame()

        self.browser.find_element_by_class_name("nologin").click()
        sleep(2)

        #选择登录方式
        # login_way = input("请选择登录方式(1:密码登录/2:短信验证码):")
        login_way = "1"
        if login_way =="1":
            #手机/邮箱/优酷土豆账号
            self.browser.find_element_by_id("YT-ytaccount").send_keys(username)
            sleep(0.2)
            self.browser.find_element_by_id("YT-ytpassword").send_keys(passwd)
            sleep(0.1)
            self.browser.find_element_by_id("YT-nloginSubmit").click()

            sleep(3)
            try:
                distance = 320
                self.start_move(distance)
                sleep(2)
                img_code = input("请输入图形验证码:")
                self.browser.find_element_by_id("nc_1_captcha_input").send_keys(img_code)
                sleep(0.1)
                self.browser.find_element_by_id("nc_1_scale_submit").click()
            except:
                pass


        else:
            #验证码登录
            self.browser.find_element_by_id("YT-showMobileLogin-text").click()
            sleep(2)
            self.browser.find_element_by_id("YT-mAccount").send_keys(username)
            self.browser.find_element_by_id("YT-getMobileCode").click()
            sleep(0.1)
            passwd = input("请输入短信验证码:")
            self.browser.find_element_by_id("YT-mPassword").send_keys(passwd)
            sleep(0.1)
            self.browser.find_element_by_id("YT-mloginSubmit").click()

        sleep(2)

    def user_info(self):
        # username = "19128324901"
        username = "15071469916"
        passwd = "zx150219"
        return username,passwd

    def passwd(self):
        passw = input('请输入短信验证码:')
        return passw

    def start_move(self,distance):
        # 点击滑块滑动
        element = self.browser.find_element_by_id("nc_1_n1z")
        # 点击小图片滑动
        # element = self.browser.find_element_by_xpath(
        #     "//div[@class='jigsaw']/div[@class='jigsaw-bg']/div[contains(@class,'jigsaw-block')]")

        # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
        distance -= element.size.get('width') / 2
        # distance += 15
        distance += 21

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

    def img_code(self):
        self.browser.find_element_by_xpath("table")
        pass

    #积分查询
    def my_score(self):
        #查询积分
        sleep(0.1)
        info_html = self.browser.page_source
        info_tree = etree.HTML(info_html)

        #个人信息+积分
        divs_a = info_tree.xpath("//div[@class='wuserifo']")
        items_a = []
        for div in divs_a:
            item_a ={}
            username = div.xpath("./div[@class='userdata']//div[@class='u-ifo']/span[1]/text()")[0].strip()
            #等级积分
            available_score = div.xpath(".//div[@class='u-jifen']/strong[@id='integral']/text()")[0].strip()
            #积分抵用券
            print("用户名为:{}".format(username))
            print("可用积分数为:{}".format(available_score))

        sleep(5)

        #积分明细:等级积分交易记录
        self.browser.find_element_by_xpath("//div[@class='userhislist']/ul/li[@id='order_record']").click()
        sleep(3)
        score_html = self.browser.page_source
        score_tree = etree.HTML(score_html)
        divs_b = score_tree.xpath("//div[@class='integral']")
        items_b = []
        #所有记录
        try:
            while self.browser.find_element_by_xpath(".//div[@class='tab']/table/tbody/tr[2]/td[1]"):
                for nums in range(2, 7):
                    try:
                        for div in divs_b:
                            item_b = {}
                            # 时间
                            datetiame = div.xpath(".//div[@class='tab']/table/tbody/tr[{}]/td[1]/text()".format(nums))[
                                0].strip()
                            # 使用/获取情况
                            score_info = div.xpath(".//div[@class='tab']/table/tbody/tr[{}]/td[2]/text()".format(nums))[
                                0].strip()
                            # 积分数
                            score_nums = div.xpath(".//div[@class='tab']/table/tbody/tr[{}]/td[3]/text()".format(nums))[
                                0].strip()
                            # 备注
                            remarks = div.xpath(".//div[@class='tab']/table/tbody/tr[{}]/td[4]/text()".format(nums))[
                                0].strip()

                            print("日期:{}".format(datetiame))
                            print("使用/获取情况:{}".format(score_info))
                            print("积分数:{}".format(score_nums))
                            print("备注:{}".format(remarks))
                    except:
                        # self.browser.find_element_by_xpath("//div[@class='page']/div[@class='next']/span").click()
                        break
                self.browser.find_element_by_xpath("//div[@class='page']/div[@class='next']/span").click()
                sleep(1.5)
        except:
            pass


    #订单查询
    def my_order(self):
        # self.browser.find_element_by_xpath("//ul[@class='rightNav']/li[1]/dl/dt").click()
        # sleep(0.1)
        # #查询近期订单
        # self.browser.find_element_by_xpath("//li[@class='selecthover']/dl/dd/ul/li[1]/a").click()
        # sleep(4)
        # order_html = self.browser.page_source
        # order_tree = etree.HTML(order_html)
        # divs_e = order_tree.xpath(".//div[@id='replaceContent']/div[@class='conRiContent']")
        # items_e = []
        # for div in divs_e:
        #     try:
        #         item_e = {}
        #         #订单号
        #         order_number = div.xpath("./div[@class='ulContent']/p[1]/span[@class='orderNo']/text()")[0].strip()
        #         order_number2 = order_number.split("：")[1]
        #         #订单时间
        #         order_time = div.xpath(".//p[@class='orderNum']/span[@class='orderTime']/text()")[0].strip()
        #         #订单内容:
        #         #产品名称
        #         product_name = div.xpath(".//p[@class='orderNum']/span[@class='orderTime']/text()")[0].strip()
        #         #数量
        #         product_nums = div.xpath(".//ul/li[@class='in-li1']/a/div/span[2]/text()")[0].strip().split("×")[1]
        #         #所需积分数
        #         score_needs = div.xpath(".//ul/li[@class='in-li2']/span/text()")[0].strip()
        #         score_needs = score_needs.split(" ")[0]
        #         #支付信息积分值
        #         score_pay =  div.xpath(".//span[@class='sp']/b/text()")[0].strip()
        #
        #         #订单渠道
        #         order_channel = div.xpath(".//ul[@class='out-ul']/li[3]/span/text()")[0].strip()
        #         #订单状态
        #         order_status = div.xpath(".//ul[@class='out-ul']/li[4]/span/text()")[0].strip()
        #         #制作
        #
        #         print("订单号:{}".format(order_number2))
        #         print("订单时间:{}".format(order_time))
        #         print("产品名称:{}".format(product_name))
        #         print("产品数量:{}".format(product_nums))
        #         print("所需积分数:{}".format(score_needs))
        #         print("合计花费积分数积分数:{}".format(score_pay))
        #         print("订单渠道:{}".format(order_channel))
        #         print("订单状态:{}".format(order_status))
        #
        #     except:
        #         # none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
        #         #
        #         # print("{}".format(none_info))
        #         print("对不起,你最近没有订单")
        #     finally:
        #         pass
        sleep(0.1)

    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'switch-wrapper')))
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
        self.my_order()
        t4 = time.time()
        tres3 = t4 - t3
        tres3 = round(tres3)
        print("奖品兑换记录耗时{}s".format(tres3))
        print("登录过程耗时:{}s".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        print("奖品兑换记录耗时{}s".format(tres3))
        return tres1


if __name__ == '__main__':
    time1 = time.clock()
    runs = Youku()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))