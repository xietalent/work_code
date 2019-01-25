
# Licensed to the Software Freedom Conservancy (SFC) under one

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from scrapy.http import HtmlResponse
from logging import getLogger
from aip import AipOcr
from time import sleep
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from lxml import etree
from urllib import request
from PIL import Image
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# from tools.zhaohang.keybord_DD import DD_input

import lxml
import urllib
import requests
import pytesseract
import pytesseract.pytesseract

import time

class Zhongshihua(object):
    def __init__(self,timeout=None):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()


    #发起请求
    def process_request(self):
        self.logger.debug('Ie is Starting')
        username = "chenhuicong2019"
        passwd = "123456abc"
        # im_code = 1234
        self.browser.set_window_size(1200,800)
        self.browser.get("https://www.saclub.com.cn/goodlist.do?bool=2")
        # self.browser.get("https://www.saclub.com.cn/")
        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'log_l')))
        im_code = self.get_img()
        self.browser.find_element_by_id("userName1").send_keys(username)
        # self.browser.find_element_by_id("userName").send_keys(username)
        sleep(0.1)
        self.browser.find_element_by_name("userPwd").send_keys(passwd)
        self.browser.find_element_by_name("mask").send_keys(im_code)
        sleep(0.2)
        self.browser.find_element_by_class_name("log_l").click()
        sleep(1)
        # if self.browser.find_element_by_xpath("//div[@class='shcon_r']/p[@class='prompt']/font/b") :
        #     self.process_request()
        # else:
            # self.inquire_score()



    #查询积分
    def inquire_score(self):
        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'f_con1-right')))
        # WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'account')))
        score_html = self.browser.page_source
        # with open(r"E:\code\spiders\text\zhongshihua\home_.html",'w+',encoding="utf8") as fp:
        #     fp.write(score_html)

        scoretree = etree.HTML(score_html)
        divs = scoretree.xpath(".//div[@class='gouwuche1']")
        # divs = scoretree.xpath(".//div[@class='useri_con']")
        # divs = scoretree.xpath(".//div[@class='header']")
        # username = scoretree.xpath("//li[@class='Landpage']/a/span/text()")[0].strip()
        score_items = []
        for div in divs :
            score_item = {}
            print("123")
            username = div.xpath("//div[@class='f_con1-right']/div/p[@class='op1']/b/text()")[0].strip()
            # username = div.xpath("//li[@class='Landpage']/a/span/text()")[0].strip()
            userlevel = div.xpath("//div[@class='f_con1-right']/div/p[@class='op2']/font/text()")[0].strip()
            # userlevel = div.xpath("//div[@class='account1']/p[@class='list2']/text()")[0].strip()
            # userlevel = div.xpath("//div[@class='account1']/p[contains(@class,'list2')]/text()")[0].strip()
            score_nums = div.xpath(".//div[@class='f_con1-right']/ul[@class='clearfix']/li[1]/b/a/text()")[0].strip()
            # score_nums = div.xpath("//div[@class='account2'][1]/p[@class='list1']/a/span/text()")[0].strip()
            used_nums = div.xpath(".//div[@class='f_con1-right']/ul[@class='clearfix']/li[2]/b/a/text()")[0].strip()
            # used_nums = div.xpath("//div[@class='account2'][2]/p[@class='list1']/text()")[0].strip()
            scored = div.xpath(".//div[@id='expiredPoints']/p/text()")[0].strip()
            # scored = div.xpath("//div[@class='account2'][3]/p[@class='list1']/text()")[0].strip()
            # a_to_expire = div.xpath("//div[@id='content']/ul/li[1]/text()")[0].strip()


            print("用户名:{}".format(username))
            print("用户等级:{}".format(userlevel))
            print("您当前可用积分数为:{}".format(score_nums))
            print("您当已用用积分数为:{}".format(used_nums))
            print("即将过期积分:{}".format(scored))
            # print("已过期积分:{}".format(a_to_expire))
        sleep(1)



    def redemption__record(self):
        self.browser.find_element_by_xpath("//div[@class='nav']/ul[@class='nav_ul wrap']/li[2]/a").click()
        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, 'list3')))

        self.browser.find_element_by_class_name("list3").click()
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.ID,'but_cl')))

        self.browser.find_element_by_id("but_cl").click()
        # WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'but_cl')))
        sleep(2)
        redemption_html = self.browser.page_source
        redemption_tree = etree.HTML(redemption_html)

        divs = redemption_tree.xpath("//div[@class='useri_con']")
        redemption_items = []
        for div in divs:
            redemption_item = {}
            # div  = divs.xpath("")






    def refuel_record(self):
        self.browser.find_element_by_class_name("list8").click()
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,"useri_query")))

        self.browser.find_element_by_xpath("//div[@class='useri_query']/input[4]").click()
        try:
            WebDriverWait(self.browser,5,0.5).until(EC.element_to_be_clickable((By.XPATH,"//tbody/tr[@class='bg']/td[1]")))
        except:
            print("最近三个月没有加油记录")
            pass

        sleep(5)
        refuel_html = self.browser.page_source
        refuel_tree = etree.HTML(refuel_html)

        divs = refuel_tree.xpath(".//div[@class='useri_con']")
        refuel_items = []
        for div in divs:
            refuel_item = {}
            #加油总数
            print("1")
            total_oil  = divs.xpath(".//p[@class='useri_txt2']/i[1]")
            #总金额
            # total_amount = divs.xpath("./p[@class='useri_txt2']/i[2]/text()")[0].strip()
            # #总交易次数
            # trans_nums  = divs.xpath("./p[@class='useri_txt2']/i[3]/text()")[0].strip()
            #
            # #交易号
            # nums  = divs.xpath("//tr[@class='bg']/td[1]/text()")[0].strip()
            # #日期
            # date = divs.xpath("//tr[@class='bg']/td[2]/text()")[0].strip()
            # #地点
            # location= divs.xpath("//tr[@class='bg']/td[3]/text()")[0].strip()
            # # 数量升)/型号
            # quantity_type = divs.xpath("//tr[@class='bg']/td[4]/text()")[0].strip()
            # #总价
            # amount  = divs.xpath("//tr[@class='bg']/td[5]/text()")[0].strip()
            # # 积分
            # score_of= divs.xpath("//tr[@class='bg']/td[6]/text()")[0].strip()
            # # 交易类型
            # type_of  = divs.xpath("//tr[@class='bg']/td[7]/text()")[0].strip()

            print("加油总量:{}".format(total_oil))
            # print("总消费金额:{}".format(total_amount))
            # print("总加油交易笔数:{}".format(trans_nums))
            #
            # print("交易号:{}".format(nums))
            # print("日期:{}".format(date))
            # print("地点:{}".format(location))
            # print("数量/型号:{}".format(quantity_type))
            # print("总价:{}".format(amount))
            # print("积分:{}".format(score_of))
            # print("交易类型:{}".format(type_of))

            sleep(1)



    def product_info(self):
        self.browser.find_element_by_xpath("//div[@class='nav']/ul[@class='nav_ul wrap']/li[3]/a").click()
        WebDriverWait(self.browser,10,0.5).until(EC.element_to_be_clickable((By.CLASS_NAME,"f_con4Center clearfix")))
        sleep(5)

    def get_img(self):
        print("get_image")
        t1 = time.time()
        # imgpage_html = self.browser.page_source
        # img_tree = etree.HTML(imgpage_html)
        # pic_url ="https://www.saclub.com.cn"+img_tree.xpath(".//div[@class='fdiv3']/a/img/@src")

        pic_url = self.browser.find_element_by_xpath(".//div[@class='fdiv3']/a/img").get_attribute('src')
        # print(pic_url1)
        # pic_url = "https://www.saclub.com.cn/{}".format(pic_url1)

        #urllib方法
        # resp = request.urlopen(pic_url)
        # raw = resp.read()
        #requests方法
        headers = {
            "Accept":"image / webp, image / apng, image / *, * / *;q = 0.8",
            "Accept - Encoding":"gzip, deflate, br",
            "Accept - Language":"zh - CN, zh;",
            "q = 0.9":"",
            "Connection":"keep - alive",
            "User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        }

        cooks = {
            "NTKF_T2D_CLIENTID":"guest316A67E3-41EB-BB51-DD84-16AD453687A3",
            "nTalk_CACHE_DATA":"{uid:kf_9507_ISME9754_guest316A67E3-41EB-BB,tid:1548310216488735}",
            "HttpOnly":"",
            "Hm_lvt_6df6f9d56598e7f5e729beb6c4558e60":"1546568681,1548310223",
            "Hm_lpvt_6df6f9d56598e7f5e729beb6c4558e60":"1548315714",
            "JSESSIONID":"8A5A314CF09A69401AB84AA56C83781B"
        }
        # pic_url = "https://www.saclub.com.cn/imgmerge?amp;text=%C8%C8%B5%E3%BE%DB%BD%B914675.0&imageFile=/new/img/f_yzm.jpg&x=24&y=24&fontColor=000000&fontStyle=bold&fontName=%CB%CE%CC%E5&fontSize=24"
        resp = requests.get(pic_url,cookies = cooks,headers = headers)
        # raw = resp.content()
        sleep(2)
        with open("./images/zhongshihua/imgcode.gif",'wb') as fp:
            for data in resp.iter_content(128):
                fp.write(data)

        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("checkimg").location
            self.browser.save_screenshot("./images/zhongshihua/login_imcode.png")
            page_snap_obj = Image.open("./images/zhongshihua/login_imcode.png")

            size = self.browser.find_element_by_id("checkimg").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save("./images/zhongshihua/zsh_imcode.png")
            # imgages.show()
            sleep(1)

            # 添加机器识别
            #获取图片后,进行识别,如果识别后数字的长度不为3,则更换验证码,重新截图
            # self.browser.find_element_by_id('img_code_text')
            # self.browser.find_element_by_id('imgvalicode').send_keys(img_code)
            # sleep(1)

            #点击验证码图片
            # self.browser.find_element_by_id("checkimg").click()
        except:
            pass
        finally:
            pass
        t2 = time.time()
        tres = t2 - t1
        tres = round(tres,2)
        img_code = input("请输入验证码:")
        print("验证码耗时:{}".format(tres))
        return img_code

    def start_spider(self):
        self.process_request()
        sleep(0.1)
        #查询积分,个人信息
        self.inquire_score()
        sleep(0.1)
        # 最近三个月兑换记录查询
        self.redemption__record()
        #最近三个月加油记录
        self.refuel_record()
        sleep(0.1)
        #积分商城商品信息
        self.product_info()
        sleep(0.1)
        #






if __name__ == '__main__':
    s = Zhongshihua()
    try:
        time.clock()
        ts6 = s.start_spider()
        # ts = time.clock()- ts6
        # ts = round(ts, 2)
        # print("总耗时为:{}s".format(ts))
    except:
        pass
    # finally:
        # del s