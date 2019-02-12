
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from  time import sleep
from logging import getLogger
from lxml import etree
from PIL import Image
from tools.zhaohang.keybord_DD import DD_input
from urllib import request
from aip import AipOcr

import selenium
import time
import pytesseract
import pytesseract.pytesseract
import requests


class abc_bank(object):
    def __init__(self,timeout=None,service_args=[]):
        self.browser = webdriver.Ie()
        self.logger = getLogger(__name__)
        self.timeout = timeout

    def __del__(self):
        self.browser.close()
        # self.browser.quit()

    def login_request(self):
        self.browser.get("https://perbank.abchina.com/EbankSite/startup.do?r=ED7A0F56C69E1DB5")
        sleep(3)
        # 输入用户名,密码
        username, passwd = self.user_info()
        # 验证码
        img_code = self.get_img()
        sleep(1)
        # 传入
        self.browser.find_element_by_id("username").send_keys(username)

        # 密码
        now_handle = self.browser.current_window_handle
        self.input_passwd(passwd, now_handle)
        # self.browser.find_element_by_id("username").send_keys(passwd)

        self.browser.find_element_by_id("code").send_keys(img_code)
        sleep(0.5)
        #登陆
        self.browser.find_element_by_id("logo").click()
        sleep(1)

    #查询
    def cridet_card(self):
        self.browser.find_element_by_xpath("//div[@class='nav']/ul/li[7]").click()
        sleep(0.5)

        #卡片信息
        self.browser.find_element_by_xpath("//div[@class='nav']/ul/li[7]/ul/li[1]").click()
        sleep(1)
        self.browser.switch_to.frame("contentFrame")
        sleep(0.2)
        cardinfo_html = self.browser.page_source
        cardinfo_tree = etree.HTML(cardinfo_html)
        divs = cardinfo_tree.xpath(".//div[@class='tabs']//div[@id='info']")
        for div in divs:
            card_nums = div.xpath("./div[@class='zhanghu']/ul[2]/li/span[1]/text()")[0].strip()
            unpaid = div.xpath("./div[@class='zhanghu']/ul[2]/li/span[3]/text()")[0].strip()
            repayment_date = div.xpath("./div[@class='zhanghu']/ul[2]/li/span[4]/text()")[0].strip()

            print("您的卡号是:{}".format(card_nums))
            print("您的未还余额是:{}".format(unpaid))
            print("您的还款日期是:{}".format(repayment_date))

    #信用卡账单查询
    def query_bill(self):
        self.browser.find_element_by_xpath("//div[@class='zhanghu_a']/a[1]").click()
        sleep(2)


        # sleep(5)


    #卡积分查询
    def card_score(self):
        # self.browser.switch_to.default_content()
        print("积分查询")
        self.browser.switch_to.parent_frame()
        self.browser.find_element_by_xpath("//div[@class='nav']/ul/li[7]/ul/li[3]").click()
        sleep(2)
        self.browser.switch_to.frame("contentFrame")
        sleep(0.2)
        card_score_html = self.browser.page_source
        card_score_tree = etree.HTML(card_score_html)
        divs = card_score_tree.xpath(".//div[@class='page-table']")
        for j in range(10):
            try:
                for div in divs:
                    card_type = div.xpath("./table/tbody/tr[{}]/td[1]/text()".format(j))[0].strip()
                    card_nums = div.xpath("./table/tbody/tr[{}]/td[2]/text()".format(j))[0].strip()
                    card_score = div.xpath("./table/tbody/tr[{}]/td[3]/text()".format(j))[0].strip()

                    print("卡类型为:{}".format(card_type))
                    print("卡号为:{}".format(card_nums))
                    print("卡积分数为:{}".format(card_score))

            except:
                pass

    #账户类型查询
    def account_type(self):
        self.browser.switch_to.parent_frame()
        sleep(0.2)
        self.browser.find_element_by_xpath("//div[@class='nav']/ul/li[2]").click()
        sleep(0.5)
        self.browser.find_element_by_xpath("//div[@class='nav']/ul/li[2]/ul/li[1]").click()
        sleep(1)
        self.browser.switch_to.frame("contentFrame")

        #借记卡
        account_type_html = self.browser.page_source
        account_type_tree = etree.HTML(account_type_html)
        divs = account_type_tree.xpath(".//div[@class='debitcardmin']")
        account_type_items = []
        try:
            for div in divs:
                account_type_item = {}
                #卡号
                # card_nums = div.xpath("./ul/li/span[@class='spanone1']/em/text()")[0].strip()
                card_nums = div.xpath("./ul/li/span[@class='spanone1']/em/child::node()[1]")[0].strip()
                #卡类型
                card_type = div.xpath("./ul/li/span[@class='spanSecond1']/em/child::node()[1]")[0].strip()
                #别名:
                alias = div.xpath("./ul/li/span[@class='spantwo1']/i/child::node()[1]")[0].strip()
                #余额
                balance = div.xpath("./ul/li/span[@class='spanthree1']/i/child::node()[1]")[0].strip()

                print("卡号为:{}".format(card_nums))
                print("账户类型为:{}".format(card_type))
                print("卡别名为:{}".format(alias))
                print("卡余额为:{}".format(balance))
        except:
            pass


    #信用卡
        self.browser.find_element_by_xpath(".//ul[@class='tabs-head']/li[2]/a").click()
        sleep(1)
        credit_account_type_html = self.browser.page_source
        credit_account_type_tree = etree.HTML(credit_account_type_html)
        divs = credit_account_type_tree.xpath(".//div[@class='zhanghu']")
        credit_account_type_items = []
        try:
            for div in divs:
                credit_account_type_item = {}
                # 卡号
                card_nums = div.xpath("./ul/li/span[1]/em/child::node()[1]")[0].strip()
                # 本期未还余额
                unpaid = div.xpath("./ul/li/span[3]/child::node()[1]")[0].strip()
                # 还款日为:
                # repay_date = div.xpath("./ul//li/span[4]/i/text()")[0].strip()
                repay_date = div.xpath("./ul/li/span[4]/i/child::node()[1]")[0].strip()
                print("卡号为:{}".format(card_nums))
                print("本期未还余额为:{}".format(unpaid))
                print("还款日为:{}".format(repay_date))
        except:
            pass

    def deposit_info(self):

        pass

    def user_info(self):
        username = "15071469916"
        passwd =r"zc006699"

        # username = input("请输入用户名:")
        # passwd = input("请输入密码:")
        return username,passwd

    def input_passwd(self,passwd,now_handle=None):
        # 获取窗口句柄
        # now_handle = self.browser.current_window_handle  # 获取当前窗口句柄
        print("当前窗口的句柄为:{}".format(now_handle))  # 输出当前获取的窗口句柄

        self.browser.switch_to.window(now_handle)
        # passwd = "465465464"
        self.browser.find_element_by_id("username").click()
        # 填写账号密码
        sleep(1)
        uname = DD_input()
        sleep(1)
        uname.dd_table()
        sleep(1)
        uname = DD_input()
        uname.dd(passwd)
        sleep(0.5)
        uname.dd_table()
        sleep(0.2)
        uname.dd_enter()

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
            location = self.browser.find_element_by_id("vCode").location
            self.browser.save_screenshot("./images/abcbank/login_imcode.png")
            page_snap_obj = Image.open("./images/abcbank/login_imcode.png")

            size = self.browser.find_element_by_id("vCode").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save("./images/abcbank/cb_imcode.png")
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
        print("验证码耗时:{}".format(tres))
        return img_code

    def start_spider(self):
        t1 = time.time()
        while True:
            self.login_request()
            sleep(3)
            try:
                self.browser.find_element_by_id("menuNav")
                print("登录成功")
                break
            except:
                pass
        t2 = time.time()
        tres1 = t2-t1
        tres1 = round(tres1,2)
        print("登录请求耗时为:{}s".format(tres1))

        #获取信用卡信息
        self.cridet_card()
        t3 = time.time()
        tres2 = t3 - t2
        tres2 = round(tres2,2)
        print("获取信用卡信息耗时为:{}s".format(tres2))
        sleep(0.1)

        self.query_bill()
        t31 = time.time()
        tres22 = t31-t2
        tres22 = round(tres22)
        print("获取信用卡账单耗时{}s".format(tres22))

        #获取卡片积分信息
        self.card_score()
        t4 = time.time()
        tres3 = t4-t31
        tres3 = round(tres3,2)
        print("获取卡片积分信息耗时:{}s".format(tres3))

        #获取账户信息
        self.account_type()
        t5 = time.time()
        tres4 = t5 - t4
        tres4 = round(tres4,2)
        print("获取账户信息消耗时间:{}s".format(tres4))

        #获取存款信息
        self.deposit_info()
        t6 = time.time()
        tres5 = t6-t5
        tres5 = round(tres5,2)
        print("查询存款信息耗时:{}s".format(tres5))


if __name__ == '__main__':
    res = abc_bank()
    time.clock()
    res.start_spider()
    my_time = time.clock()
    print("爬取总耗时:{}s".format(my_time))
    # del res