
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
import PIL

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
        sleep(4)
        # 输入用户名密码
        username,passwd = self.user_info()

        self.browser.find_element_by_id("txt_username_79443").send_keys(username)
        sleep(0.2)
        self.browser.find_element_by_id("input_div_password_79445").click()
        sleep(4)
        # 输入密码
        self.browser.find_element_by_id("input_txt_50531_740884").send_keys(passwd)
        sleep(0.1)
        # 获取验证码
        img_code = self.get_img()
        sleep(0.1)
        # self.browser.find_element_by_id("dijit_form_ValidationTextBox_1").send_keys(img_code)
        self.browser.find_element_by_id("txt_captcha_740885").send_keys(img_code)
        sleep(1.5)
        # self.browser.find_element_by_class_name("btn-r").click()
        self.browser.find_element_by_xpath("//li[@class='clearfix mb0']//a[@id='btn_49_740887']/span").click()

    def account_info(self):
        sleep(1)
        account_html = self.browser.page_source
        with open(r"E:\code\spiders\text\china_bank\account_html.txt",'w+',encoding='utf-8') as fp:
            fp.write(account_html)
            fp.close()

            account_etree = etree.HTML(account_html)
        divs = account_etree.xpath(".//div[contains(@class,'tb-box')]")
        for div in divs:
            card_num = div.xpath("//table[@class='tb']/tbody/tr[1]/td[1]/text()")[0].strip()
            card_name = div.xpath("//table[@class='tb']/tbody/tr[2]/td[1]/text()")[0].strip()
            #启用日期
            s_date = div.xpath("//table[@class='tb']/tbody/tr[3]/td[1]/text()")[0].strip()
            #账单日
            billing_date = div.xpath("//table[@class='tb']/tbody/tr[4]/td[1]/text()")[0].strip()
            #信用额度
            credits = div.xpath("//table[@class='tb']/tbody/tr[5]/td[1]/div/text()")[0].strip()
            #年费减免情况
            nianfei_date = div.xpath("//table[@class='tb']/tbody/tr[6]/td[1]/text()")[1].strip()
            # card_num = div.xpath("./table[@class='tb']//td[@class='wp30']/text()")[0].strip()

            print("卡号:{}".format(card_num))
            print("产品名称:{}".format(card_name))
            print("启用日期:{}".format(s_date))
            print("账单日:{}".format(billing_date))
            print("信用额度:{}".format(credits))
            print("年费减免情况:免费至{}".format(nianfei_date))

    def billed(self):
        # self.browser.find_element_by_class_name("user_but01").click()
        self.browser.find_element_by_xpath("//div[@id='cardMain']//li[@id='div_billedtrans_740846']/span[@class='tabs-m']").click()
        sleep(4)
        for i in range(1,4):
            print(i)
            self.browser.find_element_by_xpath("//div[@class='item-con']//span[@class='title']/label[@class='txt']/a").click()
            sleep(0.5)
            self.browser.find_element_by_xpath('//*[@id="sel_outaccountmonth_740750"]/ul/li[{}]'.format(i)).click()
            sleep(0.5)
            self.browser.find_element_by_class_name("btn-r").click()
            sleep(5)

            billed_html = self.browser.page_source
            with open(r"E:\code\spiders\text\china_bank\billed_html.txt", 'w+', encoding='utf-8') as fp:
                fp.write(billed_html)
                fp.close()
            billed_tree = etree.HTML(billed_html)
            sleep(1)
            divs = billed_tree.xpath(".//div[@class='card-mh313']")
            #还款存根
            for div in divs:
                card_nums = div.xpath("//li[contains(@class,'clearfix')][1]/div[@class='item-con']/text()")[1].strip()
                #信用卡账项记录
                billing_date = div.xpath("//li[contains(@class,'clearfix')][2]/div[@class='item-con']/text()")[1].strip()
                #到期还款日
                repay_date = div.xpath("//li[contains(@class,'clearfix')][3]/div[@class='item-con']/text()")[0].strip()
                #欠款
                arrears = div.xpath("//li[contains(@class,'clearfix')][4]/span[@class='mr5']/text()")[0].strip()

                print("信用卡号:{}".format(card_nums))
                print("账单日:{}".format(billing_date))
                print("到期还款日:{}".format(repay_date))
                print("欠款:{}".format(arrears))
                pass
            #个人信息:
            for div in divs:

                pass
            #信用卡账项记录
            for div in divs:
                amount = div.xpath("//div[@id='billed_trans_detail']/div[@class='tb-box'][1]/table[@class='tb']/tbody/tr[@class='odd']/td[@class='tar'][1]/text()")[0].strip()
                print("额度为:{}".format(amount))
                pass
            #交易明细表
            for div in divs:

                pass
            #积分奖励计划
            for div in divs:

                pass

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
        username = "6259064895839489"
        passwd = "419078"
        return username,passwd

    def get_img(self):
        print("get_image")
        t1 = time.time()
        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("captcha_creditCard").location
            print("img获取成功")
            self.browser.save_screenshot(r"E:\code\spiders\images\china_bank\cb_login2.png")
            page_snap_obj = Image.open(r"E:\code\spiders\images\china_bank\cb_login2.png")

            size = self.browser.find_element_by_id("captcha_creditCard").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))
            # 获取到验证码截图
            imgages.save(r"E:\code\spiders\images\china_bank\cb_imcode2.png")
            sleep(0.5)
            # t验证码处理
            image = PIL.Image.open(r"E:\code\spiders\images\china_bank\cb_imcode2.png")
            # image=PIL.Image.open(r"C:\Users\Administrator\Desktop\5107.jfif")
            # pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
            # 灰度化
            image = image.convert('L')
            # 杂点清除掉。只保留黑的和白的。返回像素对象
            data = image.load()
            w, h = image.size
            for i in range(w):
                for j in range(h):
                    if data[i, j] > 125:
                        data[i, j] = 255  # 纯白
                    else:
                        data[i, j] = 0  # 纯黑
            image.save(r"E:\code\spiders\images\china_bank\cb_img.png")
            # image.show()

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
            sleep(5)
            try:
                self.browser.find_element_by_class_name("tabs-m")
                print("登陆成功了")
                break
            except:
                pass
        ts2 = time.time()
        tss1 = ts2-ts1
        tss1 = round(tss1,2)
        print("登陆阶段耗时:{}".format(tss1))
        sleep(0.1)
        # 获取我的账户信息
        self.account_info()
        ts3 = time.time()
        tss2 = ts3 - ts2
        tss2 = round(tss2, 2)
        print("获取账户信息耗时:{}".format(tss2))
        sleep(0.1)
        #获取订单信息
        self.billed()
        ts4 = time.time()
        tss3 = ts4-ts3
        tss3 = round(tss3,2)
        print("已出账单信息查询耗时:{}",format(tss3))
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



