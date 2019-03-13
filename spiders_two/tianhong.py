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
        self.chrome_options = Options()
        self.chrome_options.add_argument('--headless')
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome(chrome_options = self.chrome_options)

    def __del__(self):
        self.browser.close()

    def process_request(self):

        self.browser.set_window_size(1200,1000)
        # self.browser.get("http://www.tianhong.cn/integral_list.html?crt.categoryId=19819")
        self.browser.get("https://passport.tianhong.cn/member/logout.html")
        username,passwd = self.user_info()
        try:
            WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID, 'loginBtn')))
        except:
            return  self.process_request()

        login_way = "1"
        if login_way =="1":
            self.browser.find_element_by_xpath("//div[@class='fl']/input[@id='username']").send_keys(username)
            sleep(0.2)
            self.browser.find_element_by_id("password").send_keys(passwd)
            sleep(0.1)
            self.browser.find_element_by_id("loginBtn").click()
            try:
                vercode = Vercode(self.browser)
                vercode.start_vercode()
                # sleep(8)
                self.browser.find_element_by_id("nsubmit").click()
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
        sleep(1)

    def user_info(self):
        # username = "19128324901"
        username = "15071469916"
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
        self.browser.find_element_by_xpath("//ul[@id='loginBar']/li[@id='li3']/a").click()
        sleep(0.5)
        # 切换当前窗口
        self.browser.switch_to.window(self.browser.window_handles[-1])
        srech_window = self.browser.current_window_handle
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



    #订单查询
    # def my_settings(self):
    #     self.browser.find_element_by_xpath("//dd[6]//a[@class='link']/span[@class='menu-text']").click()
    #     sleep(5)
    #     #查询个人设置信息配置
    #     # self.browser.find_element_by_xpath("//li[@class='selecthover']/dl/dd/ul/li[1]/a").click()
    #     # sleep(4)
    #     order_html = self.browser.page_source
    #     order_tree = etree.HTML(order_html)
    #     divs_e = order_tree.xpath(".//div[@class='custom-main-wrapper-cols']")
    #     items_e = []
    #     for div in divs_e:
    #         try:
    #             item_e = {}
    #             #UID
    #             uid = div.xpath(".//div[@class='userSetting-item'][2]/span[@class='vl-inline']/text()")[0].strip()
    #             # order_number2 = order_number.split("：")[1]
    #             #性别
    #             gender = div.xpath(".//div[@class='userSetting-setWrap']/div[1]/span[3]/span/em[@class='c666']/text()")[0].strip()
    #             # #生日
    #             birthday = div.xpath(".//div[@class='userSetting-setWrap']/div[@class='userSetting-setWrap-item odd'][2]/span[3]/span/em[@class='c666']/text()")[0].strip()
    #             #
    #             print("UID:{}".format(uid))
    #             print("性别:{}".format(gender))
    #             print("生日:{}".format(birthday))
    #             # print("产品数量:{}".format(product_nums))
    #             # print("所需积分数:{}".format(score_needs))
    #             # print("合计花费积分数积分数:{}".format(score_pay))
    #             # print("订单渠道:{}".format(order_channel))
    #             # print("订单状态:{}".format(order_status))
    #
    #         except:
    #             # none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
    #             #
    #             # print("{}".format(none_info))
    #             print("对不起,你最近没有订单")
    #         finally:
    #             pass
    #     sleep(0.1)
    #
    #     #历史订单查询
    #     # self.browser.find_element_by_id("orderHistory").click()
    #     # sleep(0.1)
    #     # self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/select[@id='orderHistory']/option[2]").click()
    #     # sleep(0.1)
    #     # self.browser.find_element_by_xpath("//div[@class='conRiTop']/div/a").click()
    #     # sleep(3)
    #     # order_his_html = self.browser.page_source
    #     # order_his_tree = etree.HTML(order_his_html)
    #     # divs_f = order_his_tree.xpath(".//div[@class='conRiContent']")
    #     # items_f = []
    #     # for div in divs_f:
    #     #     try:
    #     #         item_f = {}
    #     #         #订单详情
    #     #         #单价
    #     #         # 支付方式
    #     #         # 总额
    #     #         # 订单渠道
    #     #         # 订单状态
    #     #         print("")
    #     #     except:
    #     #         none_info = div.xpath("//p[@class='noOrders']/text()")[0].strip()
    #     #
    #     #         print("{}".format(none_info))
    #     #     finally:
    #     #         pass

    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'globalMenu')))
                print("登录成功")
                break
            except:
                pass
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


#滑动验证码解锁
class Vercode(object):
    def __init__(self,browser):
        self.browser = browser

    #模拟拖动
    def analog_drag(self):
        # self.browser
        distance = 320
        self.start_move(distance)
        pass

    #点击移动按钮,开始移动
    def start_move(self, distance):
        #点击滑块滑动
        # element = self.browser.find_element_by_xpath("//div[@class='slide-bar']/div[@class='slide-block']")
        #点击小图片滑动
        element = self.browser.find_element_by_xpath("//div[@class='cpt-drop-btn']")

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
            # sleep(0.01)
            time.sleep(random.randint(5,25) / 100)

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