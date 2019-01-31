
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from logging import getLogger
from aip import AipOcr
from time import sleep
from selenium.webdriver.chrome.options import Options
import lxml
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
# from tools.zhaohang.keybord_DD import DD_input

import time
import requests

class China_bank():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def login_request(self):
        self.logger.debug('Ie is Starting')
        self.browser.get("https://ebsnew.boc.cn/boc15/login.html")
        sleep(3)
        # 获取验证码
        # img_code = self.get_img()
        username,passwd = self.user_info()
        #输入密码
        # self.input_passwd(passwd)

        sleep(0.5)
        sleep(1)
        self.browser.find_element_by_id("txt_username_79443").send_keys(username)
        self.browser.find_element_by_id("input_div_password_79445").send_keys(passwd)
        sleep(0.1)
        #输入密码
        # self.input_passwd(passwd)
        sleep(0.1)
        # 获取验证码

        sleep(0.1)
        self.browser.find_element_by_class_name("btn-r").click()
        # page_html2 = self.browser.page_source
        # print("当前网址"+self.browser.page_source)
        # return page_html
        sleep(1)

        # img_code = self.get_img()
        sleep(0.1)
        # self.browser.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys(img_code)
        self.browser.find_element_by_id("txt_captcha_79449").send_keys("4512")
        sleep(1)
        self.browser.find_element_by_class_name("btn-r").click()

    def my_score(self):
        self.browser.find_element_by_xpath('//li[@id="menu3"]/a').click()
        sleep(3)

        score_html = self.browser.page_source
        with open(r"E:\code\spiders\text\china_bank\score_html.txt",'w+',encoding='utf-8') as fp:
            fp.write(score_html)
            fp.close()

        score_etree = etree.HTML(score_html)
        divs = score_etree.xpath(".//div[@id='user_content']")
        for div in divs:
            all_score = div.xpath('./div[@class="user_info"]/dl//span[1]/text()')[0].strip()
            able_score = div.xpath('./div[@class="user_info"]/dl//span[1]/text()')[1].strip()
            # able_score =div.xpath('./div[@class="user_info"]/dl/dd[2]/span/text()')[0].strip()

            print("全部积分:{}".format(all_score))
            print("当前可用积分:{}".format(able_score))

    def order_query(self):
        # self.browser.find_element_by_class_name("user_but01").click()
        self.browser.find_element_by_xpath("//div[@class='user_gnlist']/dl[1]/dt/span/input").click()
        sleep(3)
        order_html = self.browser.page_source
        with open(r"E:\code\spiders\text\china_bank\order_html.txt", 'w+', encoding='utf-8') as fp:
            fp.write(order_html)
            fp.close()

    def score_h_query(self):
        #积分管理
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[2]/a").click()
        sleep(3)
        #个人消息管理
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[3]/a").click()
        sleep(3)
        #查询增值服务
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[4]/a").click()
        sleep(3)
        #注销用户
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[5]/a").click()
        sleep(3)
        #可选服务包
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[6]/a").click()
        sleep(3)
        #other
        # self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[7]/a").click()
        # sleep(3)

    def personal_info(self):
        #电子邮箱
        #固话
        self.browser.find_element_by_xpath("").click()
        pass

    def user_info(self):
        # username = input("请输入用户名:")
        # passwd = input("请输入登录密码:")
        username = "13728647735"
        passwd = "qwe123456"
        return username,passwd

    def input_passwd(self,passwd):
        now_handle = self.browser.current_window_handle  # 获取当前窗口句柄
        print("当前窗口的句柄为:{}".format(now_handle))
        my_passwd = DD_input()
        self.browser.find_element_by_id("textfield").click()
        # passw.dd_enter()
        sleep(0.5)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        # my_passwd.dd_table()
        # sleep(0.1)
        sleep(1)
        my_passwd.dd_table()
        sleep(0.5)
        my_passwd.dd(passwd)
        sleep(0.2)

    def get_img(self):
        print("get_image")
        t1 = time.time()
        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("captcha").location
            self.browser.save_screenshot("./images/china_bank/login_imcode2.png")
            page_snap_obj = Image.open("./images/china_bank/login_imcode2.png")

            size = self.browser.find_element_by_id("captcha").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save("./images/china_bank/cb_imcode2.png")
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
        print("开始")
        #尝试登陆
        ts1 = time.time()
        while True:
            self.login_request()
            sleep(0.1)
            try:
                self.browser.find_element_by_id("denglu")
                print("登陆成功了")
                break
            except:
                pass
        ts2 = time.time()
        tss1 = ts2-ts1
        tss1 = round(tss1,2)
        print("登陆阶段耗时:{}".format(tss1))
        sleep(0.1)
        # #获取我的积分信息
        # self.my_score()
        # ts3 = time.time()
        # tss2 = ts3-ts2
        # tss2 = round(tss2,2)
        # print("获取积分信息耗时:{}".format(tss2))
        # sleep(0.1)
        # #获取订单信息
        # self.order_query()
        # ts4 = time.time()
        # tss3 = ts4-ts3
        # tss3 = round(tss3,2)
        # print("获取订单信息耗时:{}",format(tss3))
        # sleep(0.1)
        # #历史积分查询
        # self.score_h_query()
        # sleep(0.5)
        # ts5= time.time()
        # tss4 = ts5-ts4
        # tss4 = round(tss4,2)
        # print("历史积分查询耗时:{}".format(tss4))


if __name__ == '__main__':
    tsa = time.clock()
    res = China_bank()
    res.start_spider()
    tsa2 = time.clock()
    tsa2 = round(tsa2,2)
    print("爬取总耗时为:{}".format(tsa2))
    sleep(5)
    del res



