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

class china_telecom(object):
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
        sleep(1)
        score_tree = etree.HTML(score_source)
        # divs = score_tree.xpath("//div[@class='contright']")
        divs = score_tree.xpath("//div[@class='mainConplus']")
        for div in divs:
            # 可用积分
            login_nums = div.xpath("//div[@class='loginNumplus']/div/em[@id='loginNumberN']/text()")[0].strip()
            #积分余额
            # score_balance = div.xpath("//div[@class='fl'][2]/div[@class='tablecell']/p/i/text()")[0].strip()
            print("登录号码为:{}".format(login_nums))
            sleep(10)
            # print("积分余额为:{}".format(score_balance))

    #我的套餐
    def my_package(self):
        issue_source = self.browser.page_source
        issue_tree = etree.HTML(issue_source)
        sleep(20)
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

    #我的消费
    def my_consum(self):
        # self.browser.find_element_by_xpath(".//li[@id='2']/span[@class='dispalyinlineblock']").click()
        # WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.ID, "JF_JFXX_SY_CX")))
        # self.browser.find_element_by_xpath("//div[@id='2']//span[@id='show']/a[@class='dispalyblock']").click()
        # sleep(0.2)
        # self.browser.find_element_by_xpath("//div[@id='2']//div[@class='search-bar-options']/a[3]").click()
        # sleep(0.2)
        # self.browser.find_element_by_xpath("//div[@id='2']//a[@id='JF_JFXX_SY_CX']").click()
        # sleep(2)
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

        while True:
            self.process_request()
            # sleep()
            try:
                WebDriverWait(self.browser, 8, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'titleplus')))
                self.browser.find_element_by_class_name("titleplus")
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
        self.my_info()
        t4 = time.time()
        tres3 = t4 - t3
        tres3 = round(tres3)

        print("可兑换积分耗时{}s".format(tres3))

        # 获取我的套餐
        self.my_package()
        t5 = time.time()
        tres4 = t5 - t4
        tres4 = round(tres4, 2)
        print("积分发放记录消耗时间:{}s".format(tres4))
        #
        # 获取我的消费
        self.my_consum()
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
    runs = china_telecom()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2-tres1,2)
    print("总耗时:{}".format(time3))