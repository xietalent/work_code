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

class China_telecom(object):
    def __init__(self,timeout= None):
        self.timeout=timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.logger.debug('Chrome is Starting')
        self.browser.set_window_size(1200,900)
        # self.browser.get("https://login.189.cn/web/login")
        # self.browser.get("https://gd.189.cn/common/login.htm?")
        self.browser.get("https://gd.189.cn/common/newLogin/newLogin/login.htm?v=3&SSOArea=0755&SSOAccount=&SSOProType=&SSORetryTimes=&SSOError=&uamError=&SSOCustType=0&loginOldUri=&SSOOldAccount=&SSOProTypePre=")
        # WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID ,'srh2')))
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID ,'t_login')))
        # sleep(5)
        self.login_request()

    #登录
    def login_request(self):
        # loginway = input("请选择登录方式(随机密码/客户密码):")
        # self.browser.switch_to.frame("")
        loginway = "1"
        # username = input("请输入用户名:")
        username = "19128324901"
        # if loginway == "服务密码":
        if loginway == "1":
            self.servie_passwd(username)
        else:
            self.random_passwd(username)
        sleep(0.2)
        self.get_img()
        sleep(0.1)
        self.browser.find_element_by_class_name("btnSty").click()
        return username

    #客户密码登录
    def servie_passwd(self,username):

        # passwd = input("请输入服务密码:")
        self.browser.find_element_by_xpath("//div[@id='l_pwType']/span[2]/label").click()
        sleep(1)
        self.browser.find_element_by_id("account").send_keys(username)
        passwd = "150219"
        sleep(0.1)
        self.browser.find_element_by_id("password").send_keys(passwd)
        sleep(0.2)
        # self.browser.
        return  passwd

    #随机密码
    def random_passwd(self,username):
        self.browser.find_element_by_id("account").send_keys(username)
        try:
            self.browser.find_element_by_id("getPW2").click()
            ver_code = input("请输入收到的短信验证码:")
            sleep(0.1)
            self.browser.find_element_by_id("password").send_keys(ver_code)
            sleep(0.2)
        except:
            pass

    def get_img(self):
        print("get_image")
        t1 = time.time()
        # requests方法
        headers = {
            "Accept": "image / webp, image / apng, image / *, * / *;q = 0.8",
            "Accept - Encoding": "gzip, deflate, br",
            "Accept - Language": "zh - CN, zh;",
            "q = 0.9": "",
            "Connection": "keep - alive",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }
        cooks = {
            "NTKF_T2D_CLIENTID": "guest316A67E3-41EB-BB51-DD84-16AD453687A3",
            "nTalk_CACHE_DATA": "{uid:kf_9507_ISME9754_guest316A67E3-41EB-BB,tid:1548310216488735}",
            "HttpOnly": "",
            "Hm_lvt_6df6f9d56598e7f5e729beb6c4558e60": "1546568681,1548310223",
            "Hm_lpvt_6df6f9d56598e7f5e729beb6c4558e60": "1548315714",
            "JSESSIONID": "8A5A314CF09A69401AB84AA56C83781B"
        }
        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("loginCodeImage").location
            self.browser.save_screenshot(r"E:\code\spiders_two\images\china_telecom\login_imcode.png")
            page_snap_obj = Image.open(r"E:\code\spiders_two\images\china_telecom\login_imcode.png")

            size = self.browser.find_element_by_id("loginCodeImage").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save(r"E:\code\spiders_two\images\china_telecom\cb_imcode.png")
            # imgages.show()
            sleep(1)

            # 添加机器识别
            # 获取图片后,进行识别,如果识别后数字的长度不为3,则更换验证码,重新截图
            # self.browser.find_element_by_id('img_code_text')
            # self.browser.find_element_by_id('imgvalicode').send_keys(img_code)
            # sleep(1)
            # 点击验证码图片
            # self.browser.find_element_by_id("checkimg").click()
        except:
            pass
        finally:
            pass
        t2 = time.time()
        tres = t2 - t1
        tres = round(tres, 2)
        img_code = input("请输入验证码:")
        self.browser.find_element_by_id("loginCodeRand").send_keys(img_code)
        print("验证码耗时:{}".format(tres))
        return img_code

    def account_info(self):
        # self.browser.find_element_by_xpath("//li[@class='listHover']//a").click()
        # WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'adress-title ')))
        sleep(0.2)
        account_source = self.browser.page_source
        with open(r"E:\code\spiders_two\templates\china_telecom\index.txt","w+",encoding="utf-8") as fp:
            fp.write(account_source)
        #我的信息
        # self.my_info()
        #我的套餐
        # self.my_package()
        #我的消费
        # self.my_consum()

    #我的信息
    def my_info(self):
        print("我的信息")
        # WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,'mainConplus')))
        score_source = self.browser.page_source
        sleep(3)
        score_tree = etree.HTML(score_source)
        # divs = score_tree.xpath("//div[@class='contright']")
        divs = score_tree.xpath("//div[@class='mainConplus']")
        for div in divs:
            # 可用积分
            login_nums = div.xpath("//div[@class='loginNumplus']/div/em[@id='loginNumberN']/text()")[0].strip()
            #我的余额
            my_balance = div.xpath("//ul[@class='ulTwo']/li[1]/em/text()")[0].strip()
            # my_balance = div.xpath("//ul[@class='ulTwo']/li[@class='clearfix'][1]/em/text()")[0].strip()
            # my_balance = div.xpath("//ul[@class='ulTwo']/li[@class='clearfix'][1]/em[contains(@class,'BalanceNum')]/text()")[0].strip()
            # 我的话费
            my_phone_bill = div.xpath("//ul[@class='ulTwo']/li[2]/em/text()")[0].strip()
            # my_phone_bill = div.xpath("//ul[@class='ulTwo']/li[@class='clearfix'][2]/em/text()")[0].strip()
            #我的积分
            # "li[contains(@class,'last')]"
            # my_scores = div.xpath("//ul[@class='ulTwo']/li[4]/em[@id='usableIntegral']/text()")[0].strip()
            my_scores = div.xpath("//ul[@class='ulTwo']/li[contains(@class,'last')]/em/text()")[0].strip()
            # my_scores = div.xpath("//ul[@class='ulTwo']/li[contains(@class,'last')]/em[@id='usableIntegral']/text()")[0].strip()

            print("登录号码为:{}".format(login_nums))
            print("我的余额为:{}".format(my_balance))
            print("我的话费为:{}".format(my_phone_bill))
            print("我的积分为:{}".format(my_scores))
            sleep(0.1)


    #我的套餐
    def my_package(self):
        # self.browser.set_window_size(1000,500)
        # sleep(10)
        issue_source = self.browser.page_source
        issue_tree = etree.HTML(issue_source)
        sleep(0.1)
        divs = issue_tree.xpath("//div[@class='contright']")

        try:
            for div in divs :
                # 我的套餐
                score_type = div.xpath("./div[@id='myTc']/p[contains(@class,'tcName')]/span/text()")[0].strip()
                # 已用流量
                score_nums = div.xpath(".//p[@id='bxlUsedFlow2']/text()")[0].strip()
                # 语音已用
                release_date = div.xpath(".//div[@class='annTb']/p[@class='annTxt2'][1]/text()")[0].strip()
                # 语音剩余
                try:
                    expiry_date = div.xpath(".//div[@class='annTb']/p[@class='annTxt2'][2]/text()")[0].strip()
                    # 备注
                except:
                    expiry_date = "空"
                # remarks = div.xpath("./tbody/tr[{}]/td[5]/text()".format(nums))[0].strip()

                print("我的套餐:{}".format(score_type))
                print("已用流量:{}".format(score_nums))
                print("语音已用:{}".format(release_date))
                print("语音剩余:{}".format(expiry_date))
                    # print("备注为:{}".format(remarks))
        except:
            pass

    #我的消费
    def my_consum(self):
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
        self.browser.find_element_by_xpath("//div[@class='menuMod']/ul/li[@class='clearfix'][5]/a").click()
        try:
            WebDriverWait(self.browser,18, 0.5).until(EC.element_to_be_clickable((By.ID,'myorder_orderList_head')))
        except:
            pass

        #三个月内订单
        order_info_source = self.browser.page_source
        order_info_tree = etree.HTML(order_info_source)
        divs = order_info_tree.xpath("//div[@class='tabCon']")
        for nums in range(2, 50):
            try:
                for div in divs:
                    # 产品信息
                    product_info = div.xpath(".//table[@class='tbl']/tbody/tr[{}]/td[@class='tl']/p[@class='orderTit']/text()".format(nums))[0].strip()
                    # 业务类型
                    try:
                        order_type = div.xpath(".//table[@class='tbl']/tbody/tr[{}]/td[2]/text()".format(nums))[0].strip()
                    except:
                        order_type = "无"
                    # 受理渠道
                    order_channel = div.xpath(".//table[@class='tbl']/tbody/tr[{}]/td[3]/text()".format(nums))[0].strip()
                    # 订单状态
                    order_status = div.xpath(".//table[@class='tbl']/tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()
                    #业务操作
                    # handle = div.xpath("./tbody/tr[{}]/td[4]/text()".format(nums))[0].strip()


                    print("产品信息:{}".format(product_info))
                    print("业务类型:{}".format(order_type))
                    print("受理渠道:{}".format(order_channel))
                    print("订单状态:{}".format(order_status))
                    # print("业务操作:{}".format(handle))
            except:
                break

            #三个月前订单
            # self.browser.find_element_by_xpath("//li[@id='myorder_qryTime_l2']/a").click()
            # sleep(5)


    def start_spider(self):
        t1 = time.time()
        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser,12, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'titleplus')))
                self.browser.find_element_by_class_name("titleplus")
                print("登录成功")
                break
            except:
                pass
        t2 = time.time()
        tres1 = t2-t1
        tres1 = round(tres1,2)
        print("登录过程耗时:{}".format(tres1))
        sleep(3)

        #账户信息
        self.account_info()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2, 2)
        print("获取账户信息耗时为:{}s".format(tres2))
        sleep(0.1)

        #获取个人信息
        self.my_info()
        t4 = time.time()
        tres3 = t4 - t3
        tres3 = round(tres3)

        print("我的信息耗时{}s".format(tres3))

        # 获取我的套餐
        self.my_package()
        t5 = time.time()
        tres4 = t5 - t4
        tres4 = round(tres4, 2)
        print("我的套餐消耗时间:{}s".format(tres4))
        #
        # 获取我的消费
        self.my_consum()
        t6 = time.time()
        tres5 = t6 - t5
        tres5 = round(tres5, 2)
        print("我的消费耗时:{}s".format(tres5))
        #
        # 获取订单信息
        self.order_info()
        t7 = time.time()
        tres6 = t7 - t6
        tres6 = round(tres6, 2)
        print("登录过程耗时:{}".format(tres1))
        print("获取账户信息耗时为:{}s".format(tres2))
        print("我的信息耗时:{}s".format(tres3))
        print("我的套餐消耗时间:{}s".format(tres4))
        print("我的消费耗时:{}s".format(tres5))
        print("获取我的订单耗时{}s".format(tres6))
        return tres1

if __name__ == '__main__':
    time1 = time.clock()
    runs = China_telecom()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2-tres1,2)
    print("总耗时:{}".format(time3))