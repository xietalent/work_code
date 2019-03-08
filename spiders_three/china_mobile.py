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
import lxml
import requests
import ctypes
import urllib
import urllib3
import pytesseract
import pytesseract.pytesseract


class China_mobile(object):
    def __init__(self,timeout= None):
        self.timeout=timeout
        self.logger = getLogger(__name__)
        self.chrome_options = Options()
        self.chrome_options.add_argument("--headless")
        self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        #有界面模式
        # self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.logger.debug('Chrome is Starting')
        self.browser.set_window_size(1200,900)
        self.browser.get("https://login.10086.cn/?channelID=12019&backUrl=http://jf.10086.cn/t")
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID ,'submit_bt')))
        self.login_request()

    #登录
    def login_request(self):
        # loginway = input("请选择登录方式(服务密码/短信验证码):")
        loginway = "22"
        # username = input("请输入用户名:")
        username = "15071469916"
        # if loginway == "服务密码":
        if loginway == "1":
            self.servie_passwd(username)
        else:
            self.sms_ver_code(username)
        sleep(0.2)
        self.browser.find_element_by_id("submit_bt").click()
        return username

    #服务密码登录
    def servie_passwd(self,username):
        self.browser.find_element_by_id("p_name").send_keys(username)
        kehuhao = input("请输入服务密码:")
        sleep(0.1)
        self.browser.find_element_by_id("p_pwd").send_keys(kehuhao)
        sleep(0.2)
        self.browser.find_element_by_id("submit_bt").click()
        sleep(1)
        self.browser.find_element_by_id("getSMSPwd").click()

        ver_code = input("请输入收到的短信验证码:")
        sleep(0.1)
        self.browser.find_element_by_id("sms_pwd").send_keys(ver_code)
        sleep(0.2)
        # self.browser.
        return  kehuhao

    #短信验证码
    def sms_ver_code(self,username):
        self.browser.find_element_by_id("sms_login_1").click()
        sleep(0.2)
        self.browser.find_element_by_id("sms_name").send_keys(username)
        try:
            self.browser.find_element_by_id("getSMSPwd1").click()
            ver_code = input("请输入收到的短信验证码:")
            sleep(0.1)
            self.browser.find_element_by_id("sms_pwd_l").send_keys(ver_code)
            sleep(0.2)
        except:
            pass

    def account_info(self):
        self.browser.find_element_by_xpath("//li[@class='listHover']//a").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'adress-title ')))

        account_source = self.browser.page_source
        with open(r"E:\code\spiders_two\templates\china_mobile\account.txt","w+",encoding="utf-8") as fp:
            fp.write(account_source)
        # self.score_info()
        # self.issue_record()
        # self.usage_record()

    #积分信息7
    def score_info(self):
        self.browser.find_element_by_xpath(".//dd[@id='dd1']/a[@class='dispalyblock']").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'integral-information-th-left')))
        score_source = self.browser.page_source
        sleep(1)
        score_tree = etree.HTML(score_source)
        divs = score_tree.xpath("//div[@id='0']")
        for div in divs:
            # 可用积分
            available = div.xpath("//div[@class='fl'][1]/div[@class='tablecell']/p/i/text()")[0].strip()
            #积分余额
            score_balance = div.xpath("//div[@class='fl'][2]/div[@class='tablecell']/p/i/text()")[0].strip()

            print("可用积分为:{}".format(available))
            print("积分余额为:{}".format(score_balance))

    #积分发放记录
    def issue_record(self):
        self.browser.find_element_by_xpath(".//li[@id='1']/span[@class='dispalyinlineblock']").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID,"JF_JFXX_FF_CX")))
        self.browser.find_element_by_xpath("//div[@id=1]//span[@id='show']/a[@class='dispalyblock']").click()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@class='search-bar-options']/a[4]").click()
        sleep(0.2)
        self.browser.find_element_by_id("JF_JFXX_FF_CX").click()
        sleep(2)
        issue_source = self.browser.page_source
        issue_tree = etree.HTML(issue_source)
        divs = issue_tree.xpath("//div[@id='1']/table")
        for nums in range(2,100):
            try:
                for div in divs :
                    # 积分类型
                    score_type = div.xpath("./tbody/tr[{}]/td[1]/text()".format(nums))[0].strip()
                    # 发放积分数
                    score_nums = div.xpath("./tbody/tr[{}]/td[2]/text()".format(nums))[0].strip()
                    # 发放时间
                    release_date = div.xpath("./tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    # 到期日
                    try:
                        expiry_date = div.xpath("./tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()
                        # 备注
                    except:
                        expiry_date = "空"
                    remarks = div.xpath("./tbody/tr[{}]/td[5]/text()".format(nums))[0].strip()

                    print("积分类型:{}".format(score_type))
                    print("发放积分数:{}".format(score_nums))
                    print("发放时间:{}".format(release_date))
                    print("到期日:{}".format(expiry_date))
                    print("备注为:{}".format(remarks))
            except:
                break

    #使用记录
    def usage_record(self):
        self.browser.find_element_by_xpath(".//li[@id='2']/span[@class='dispalyinlineblock']").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID, "JF_JFXX_SY_CX")))
        self.browser.find_element_by_xpath("//div[@id='2']//span[@id='show']/a[@class='dispalyblock']").click()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@id='2']//div[@class='search-bar-options']/a[3]").click()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@id='2']//a[@id='JF_JFXX_SY_CX']").click()
        sleep(2)
        usage_source = self.browser.page_source
        usage_tree = etree.HTML(usage_source)
        divs = usage_tree.xpath("//div[@id='2']/table")
        for nums in range(2, 100):
            try:
                for div in divs:
                    # 使用积分数
                    usage_score_nums = div.xpath("./tbody/tr[{}]/td[1]/text()".format(nums))[0].strip()
                    # 使用日期
                    try:
                        usage_date = div.xpath("./tbody/tr[{}]/td[2]/text()".format(nums))[0].strip()
                    except:
                        usage_date = "无"
                    # 使用情况
                    details = div.xpath("./tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    # 到期日

                    print("使用积分值:{}".format(usage_score_nums))
                    print("使用日期:{}".format(usage_date))
                    print("使用情况:{}".format(details))
            except:
                break

    # 订单信息
    def order_info(self):
        self.browser.find_element_by_xpath("//dd[@id='dd4']/a[@class='dispalyblock']").click()
        WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'search-bar-box')))

        #选择普通订单还是转赠订单
        self.browser.find_element_by_xpath("//div[@class='search-bar-box']/form/span[1]/a").click()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@class='search-bar-box']/form/span[1]//div[@class='search-bar-options']//a[2]").click()
        #点击选择查询多久时间内的订单
        self.browser.find_element_by_xpath("//div[@class='search-bar-box']/form/span[2]/a").click()
        sleep(0.1)
        self.browser.find_element_by_xpath("//div[@class='search-bar-box']/form/span[2]/div[@class='search-bar-options']//a[4]").click()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@class='search-bar-box']/form/input").click()
        # WebDriverWait(self.browser, 5, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'search-bar-box')))
        sleep(2)
        order_info_source = self.browser.page_source
        order_info_tree = etree.HTML(order_info_source)
        divs = order_info_tree.xpath("//table[@class='my-orders-table']")
        for nums in range(2, 100):
            try:
                for div in divs:
                    # 礼品信息
                    gift_info = div.xpath("./tbody/tr[{}]/td[1]/text()".format(nums))[0].strip()
                    # 订单积分
                    try:
                        order_score = div.xpath("./tbody/tr[{}]/td[2]/text()".format(nums))[0].strip()
                    except:
                        order_score = "无"
                    # 订单状态
                    order_status = div.xpath("./tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    # 操作
                    handle = div.xpath("./tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()

                    print("礼品信息:{}".format(gift_info))
                    print("订单积分:{}".format(order_score))
                    print("订单状态:{}".format(order_status))
                    print("操作:{}".format(handle))
            except:
                break

    def start_spider(self):
        t1 = time.time()
        # self.process_request()
        # t2 = time.time()
        # tres1 = t2 -t1
        # tres1 = round(tres1,2)
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 5, 0.5).until(EC.element_to_be_clickable((By.ID, 'btn_search')))
                self.browser.find_element_by_id("btn_search")
                print("登录成功")
                break
            except:
                pass
        t2 = time.time()
        tres1 = t2-t1
        tres1 = round(tres1,2)
        print("登录过程耗时:{}".format(tres1))

        #账户信息
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("获取账户信息耗时为:{}s".format(tres2))
        sleep(0.1)

        #获取可兑换积分信息数据
        self.score_info()
        t4 = time.time()
        tres3 = t4 - t3
        tres3 = round(tres3)

        print("可兑换积分耗时{}s".format(tres3))

        # 获取积分发放记录
        self.issue_record()
        t5 = time.time()
        tres4 = t5 - t4
        tres4 = round(tres4, 2)
        print("积分发放记录消耗时间:{}s".format(tres4))
        #
        # 获取积分使用记录
        self.usage_record()
        t6 = time.time()
        tres5 = t6 - t5
        tres5 = round(tres5, 2)
        print("积分使用账单耗时:{}s".format(tres5))
        #
        # 获取存款信息
        self.order_info()
        t7 = time.time()
        tres6 = t7 - t6
        tres6 = round(tres6, 2)
        print("登录过程耗时:{}".format(tres1))
        print("获取账户信息耗时为:{}s".format(tres2))
        print("可兑换积分耗时{}s".format(tres3))
        print("积分发放记录消耗时间:{}s".format(tres4))
        print("积分使用账单耗时:{}s".format(tres5))
        print("获取兑换账单耗时{}s".format(tres6))

        return tres1

if __name__ == '__main__':
    time1 = time.clock()
    runs = China_mobile()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2-tres1,2)
    print("总耗时:{}".format(time3))


