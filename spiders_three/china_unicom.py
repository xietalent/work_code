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

from PIL import Image
from urllib import request,response
# from tools.keybord_DD import DD_input

import time
import requests
import ctypes
import urllib
import urllib3
import pytesseract
import pytesseract.pytesseract

class China_unicom(object):
    def __init__(self,timeout = None):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.browser.set_window_size(1200,1000)
        self.browser.get("https://uac.10010.com/?redirectURL=http://jf.10010.com/")
        sleep(1)
        username = self.user_info()
        iframe = self.browser.find_elements_by_tag_name("iframe")[0]
        self.browser.switch_to.frame(iframe)
        # self.browser.switch_to.frame()
        sleep(0.1)
        self.browser.find_element_by_id("userName").send_keys(username)
        sleep(0.1)
        login_way = input("请选择登录方式(1:服务密码/2:短信验证码):")
        if login_way =="1":
            my_passwd = "006688"
            self.browser.find_element_by_id("userPwd").send_keys(my_passwd)
            sleep(0.1)
            self.browser.find_element_by_id("randomCKCode").click()
            passw = self.passwd()
            try:
                self.browser.find_element_by_id("userCK").send_keys(passw)
                sleep(0.1)
            except:
                pass
            self.browser.find_element_by_id("login1").click()
        else:
            self.browser.find_element_by_xpath("//div[@class='boxTop']//li[3]/a").click()
            sleep(3)
            self.browser.find_element_by_id("randomCode").click()

            passw = self.passwd()
            self.browser.find_element_by_id("userPwd").send_keys(passw)
            sleep(0.1)
            self.browser.find_element_by_id("login1").click()
            sleep(1)

    def login_request(self):
        pass

    def user_info(self):
        username = "18576892996"
        return username

    def passwd(self):
        passw = input('请输入短信验证码:')
        return passw

    #积分查询
    def my_score(self):
        self.browser.find_element_by_xpath("//div[@class='center']//li[1]/dl/dt").click()
        sleep(0.1)
        #查询积分
        self.browser.find_element_by_xpath("//ul[@class='rightNav']/li[1]/dl/dd/ul/li[2]/a").click()
        WebDriverWait(self.browser,8,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'conRiTop')))
        self.browser.find_element_by_class_name("select_txt").click()
        sleep(0.1)
        #积分生成记录,6个月
        self.browser.find_element_by_xpath("//div[@class='option']/a[3]").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='serch']//img").click()
        sleep(4)

        score_html = self.browser.page_source
        score_tree = etree.HTML(score_html)

        #个人信息
        divs_a = score_tree.xpath("//div[@class='contentLeft']/div[@class='user']")
        items_a = []
        for div in divs_a:
            item_a ={}
            username = div.xpath("./span[@class='userPhone']/text()")[0].strip()
            #可用积分
            available_score = div.xpath("./span[@id='pointsInfoSpan']/i/text()")[0].strip()
            #积分抵用券
            score_diyong = div.xpath("./span[@id='coPointsInfoSpan']/i/text()")[0].strip()
            #积分限制券
            score_xianzhi = div.xpath("./span[@id='coVouchersInfoSpan']/i/text()")[0].strip()

            print("用户名为:{}".format(username))
            print("可用积分数为:{}".format(available_score))
            print("积分抵用券数为:{}".format(score_diyong))
            print("积分限制券数为:{}".format(score_xianzhi))

        #积分信息
        divs_b = score_tree.xpath("//div[@class='conRiContent']/div[@class='conRiTop']")
        items_b = []
        for div in divs_b:
            item_b = {}
            #当前总积分
            score_total = div.xpath("./ul/li[1]/span/p[@class='red']/text()")[0].strip()
            score_total = score_total.split(" ")[0].strip(" ")
            #当前可用积分
            score_available = div.xpath("./ul/li[2]/span/p[@class='red']/text()")[0].strip()
            score_available = score_available.split(" ")[0].strip(" ")
            #本月即将过期积分
            score_expire = div.xpath("./ul/li[3]/span/p[@class='red']/text()")[0].strip()
            score_expire = score_expire.split(" ")[0].strip(" ")

            print("当前总积分数:{}".format(score_total))
            print("当前可用积分数:{}".format(score_available))
            print("本月即将过期积分数:{}".format(score_expire))

        #积分生成记录
        divs_c = score_tree.xpath("//div[@class='content']/div[@class='switchArea']/ul/li[@id='tb1']")

        items_c = []
        for nums in range(2,100):
            try:
                for div in divs_c:
                    item_c = {}
                    #积分生成时间
                    score_genertime = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[1]/text()".format(nums))[0].strip()
                    #积分失效时间
                    score_failtime = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[2]/text()".format(nums))[0].strip()
                    score_nums = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    score_types = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()
                    print("积分生成时间:{}".format(score_genertime))
                    print("积分失效时间:{}".format(score_failtime))
                    print("积分值:{}".format(score_nums))
                    print("积分类型说明:{}".format(score_types))
            except:
                break


        #积分消费记录,半年内
        self.browser.find_element_by_xpath("//div[@class='switch']/ul/li[@id='sw2']").click()
        sleep(3)
        self.browser.find_element_by_xpath("//span[@class='select_txt']").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='select_box']/div[@class='option']/a[3]").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='serch']//img").click()
        sleep(3)

        order_html = self.browser.page_source
        order_tree = etree.HTML(order_html)
        divs_d = order_tree.xpath("//div[@class='switchArea']/ul/li[@id='tb2']")
        items_d = []
        for nums in range(2,100):
            try:
                for div in divs_d:
                    item_d = {}
                    #积分消费时间
                    score_consumtime = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[1]/text()".format(nums))[0].strip()
                    #积分消费值
                    score_consumnums = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[@class='green']/text()".format(nums))[0].strip()
                    #积分消费渠道
                    score_consumchannel = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    #积分兑换礼品
                    gifts_types = div.xpath("./table[@class='conBox-table']/tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()
                    print("积分消费时间:{}".format(score_consumtime))
                    print("积分消费值:{}".format(score_consumnums))
                    print("积分消费渠道:{}".format(score_consumchannel))
                    print("积分兑换礼品:{}".format(gifts_types))
            except:
                break


    #订单查询
    def my_order(self):
        self.browser.find_element_by_xpath("//ul[@class='rightNav']/li[1]/dl/dt").click()
        sleep(0.1)
        #查询近期订单
        self.browser.find_element_by_xpath("//li[@class='selecthover']/dl/dd/ul/li[1]/a").click()
        sleep(4)
        order_html = self.browser.page_source
        order_tree = etree.HTML(order_html)
        divs_e = order_tree.xpath(".//div[@id='replaceContent']/div[@class='conRiContent']")
        items_e = []
        for div in divs_e:
            try:
                item_e = {}
                #订单号
                order_number = div.xpath("./div[@class='ulContent']/p[1]/span[@class='orderNo']/text()")[0].strip()
                order_number2 = order_number.split("：")[1]
                #订单时间
                order_time = div.xpath(".//p[@class='orderNum']/span[@class='orderTime']/text()")[0].strip()
                #订单内容:
                #产品名称
                product_name = div.xpath(".//p[@class='orderNum']/span[@class='orderTime']/text()")[0].strip()
                #数量
                product_nums = div.xpath(".//ul/li[@class='in-li1']/a/div/span[2]/text()")[0].strip().split("×")[1]
                #所需积分数
                score_needs = div.xpath(".//ul/li[@class='in-li2']/span/text()")[0].strip()
                score_needs = score_needs.split(" ")[0]
                #支付信息积分值
                score_pay =  div.xpath(".//span[@class='sp']/b/text()")[0].strip()

                #订单渠道
                order_channel = div.xpath(".//ul[@class='out-ul']/li[3]/span/text()")[0].strip()
                #订单状态
                order_status = div.xpath(".//ul[@class='out-ul']/li[4]/span/text()")[0].strip()
                #制作

                print("订单号:{}".format(order_number2))
                print("订单时间:{}".format(order_time))
                print("产品名称:{}".format(product_name))
                print("产品数量:{}".format(product_nums))
                print("所需积分数:{}".format(score_needs))
                print("合计花费积分数积分数:{}".format(score_pay))
                print("订单渠道:{}".format(order_channel))
                print("订单状态:{}".format(order_status))

            except:
                # none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
                #
                # print("{}".format(none_info))
                print("对不起,你最近没有订单")
            finally:
                pass
        sleep(0.1)

        #历史订单查询
        self.browser.find_element_by_id("orderHistory").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/select[@id='orderHistory']/option[2]").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/a").click()
        sleep(3)
        order_his_html = self.browser.page_source
        order_his_tree = etree.HTML(order_his_html)
        divs_f = order_his_tree.xpath(".//div[@class='conRiContent']")
        items_f = []
        for div in divs_f:
            try:
                item_f = {}
                #订单详情
                #单价
                # 支付方式
                # 总额
                # 订单渠道
                # 订单状态

                print("")
            except:
                none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()

                print("{}".format(none_info))
            finally:
                pass


    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'center')))
                self.browser.find_element_by_id("content")
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
        print("可订单信息耗时{}s".format(tres3))
        print("登录过程耗时:{}s".format(tres1))
        print("获取积分信息耗时为:{}s".format(tres2))
        print("可订单信息耗时{}s".format(tres3))
        return tres1


if __name__ == '__main__':
    time1 = time.clock()
    runs = China_unicom()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}s".format(time2))
    print("总耗时(去除登录时间后):{}s".format(time3))