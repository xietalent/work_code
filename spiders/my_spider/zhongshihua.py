# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

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
    def __init__(self, timeout=None):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()

    # 发起请求
    def process_request(self):
        self.logger.debug('Ie is Starting')
        username = "chenhuicong2019"
        passwd = "123456abc"
        # im_code = 1234
        self.browser.set_window_size(1400, 900)
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

    # 查询积分
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
        for div in divs:
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
        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.ID, 'but_cl')))

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
        WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "useri_query")))
        self.browser.find_element_by_xpath("//div[@class='useri_query']/input[4]").click()
        try:
            WebDriverWait(self.browser, 5, 0.5).until(
                EC.element_to_be_clickable((By.XPATH, "//tbody/tr[@class='bg']/td[1]")))
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
            # 加油总数
            # print("1")
            total_oil = div.xpath(".//p[@class='useri_txt2']/i[1]/text()")[0].strip()
            # 总金额
            total_amount = div.xpath("./p[@class='useri_txt2']/i[2]/text()")[0].strip()
            # 总交易次数
            trans_nums = div.xpath("./p[@class='useri_txt2']/i[3]/text()")[0].strip()

            # 交易号
            nums = div.xpath("//tr[@class='bg']/td[1]/text()")[0].strip()
            # 日期
            date = div.xpath("//tr[@class='bg']/td[2]/text()")[0].strip()
            # 地点
            location = div.xpath("//tr[@class='bg']/td[3]/text()")[0].strip()
            # 数量升)/型号
            quantity_type = div.xpath("//tr[@class='bg']/td[4]/text()")[0].strip()
            # 总价
            amount = div.xpath("//tr[@class='bg']/td[5]/text()")[0].strip()
            # 积分
            score_of = div.xpath("//tr[@class='bg']/td[6]/text()")[0].strip()
            # 交易类型
            type_of = div.xpath("//tr[@class='bg']/td[7]/text()")[0].strip()

            refuel_item["加油总数"] = total_oil
            refuel_item["总金额"] = total_amount
            refuel_item["总交易次数"] = trans_nums
            refuel_item["交易号"] = nums
            refuel_item["日期"] = date
            refuel_item["地点"] = location
            refuel_item["数量/型号"] = quantity_type
            refuel_item["总价(元)"] = amount
            refuel_item["积分"] = score_of
            refuel_item["交易类型"] = type_of

            refuel_items.append(refuel_item)

            print("加油总量:{}".format(total_oil))
            print("总消费金额:{}".format(total_amount))
            print("总加油交易笔数:{}".format(trans_nums))

            print("交易号:{}".format(nums))
            print("日期:{}".format(date))
            print("地点:{}".format(location))
            print("数量/型号:{}".format(quantity_type))
            print("总价:{}".format(amount))
            print("积分:{}".format(score_of))
            print("交易类型:{}".format(type_of))
            sleep(1)
        print(refuel_items)

    def product_info(self):
        self.browser.find_element_by_xpath("//div[@class='nav']/ul[@class='nav_ul wrap']/li[3]/a").click()
        # WebDriverWait(self.browser, 10, 0.5).until(EC.element_to_be_clickable((By.CLASS_NAME, "f_con4Center clearfix")))
        sleep(3)
        # js = "var q=document.documentElement.scrollTop=10000"
        # self.browser.execute_script(js)
        # target = self.browser.find_element_by_xpath("//div[@class='gouwuche1']/div[@class='f_con2 clearfix']/ul/li[1]")
        # self.browser.execute_script("arguments[0].focus();", target)
        # self.goods_info()
        product_html = self.browser.page_source
        product_tree = etree.HTML(product_html)
        divs = product_tree.xpath("//div[contains(@class,'f_con4Center')]")
        product_items = []
        for div in divs:
            product_item = {}
            # print("product")
            # image_url = div.xpath("//div[@class='f_con4Center clearfix']/dl[1]/dt/a/img/@src")
            for _ in range(100):
                try:
                    image_url = "https://www.saclub.com.cn" + \
                                div.xpath("//div[contains(@class,'f_con4Center')]/dl/dt/a/img/@src")[+\
                                int("{}".format(_))].strip()
                    goods_name = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/h3/a/text()")[+\
                                int("{}".format(_))].strip()
                    score_need = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/p[@class='p1']/span/text()")[+ \
                        int("{}".format(_))].strip()
                    limit_nums = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/p[@class='p1'][1]/text()")[+ \
                        int("{}".format((_*3)+2))].strip()
                    print(image_url)
                    print(goods_name)
                    print("所需积分数:{}".format(score_need))
                    print(limit_nums)
                    try:
                        pic = requests.get(image_url,timeout=5)

                        # file_name = "iamge" + str(_) + ".jpg"  # 图片名
                        with open((r"E:\code\spiders\text\zhongshihua\img\{}.jpg".format(goods_name)), 'wb') as fp:
                            fp.write(pic.content)
                            fp.close()
                    except requests.exceptions.ConnectionError:
                        print("无法下载当前图片")
                        continue

                except:
                    pass
            # image_url = "https://www.saclub.com.cn"+div.xpath("//div[contains(@class,'f_con4Center')]/dl[1]/dt/a/img/@src")[0].strip()\\
        for page in range(2,6):
            print(page)
            jscode = "var q=document.documentElement.scrollTop=100000"
            self.browser.execute_script(jscode)

            self.browser.find_element_by_xpath("//span[@class='tdh3']/select[@class='input_olive_redeem']").click()
            self.browser.find_element_by_xpath("//span[@class='tdh3']/select[@class='input_olive_redeem']/option[{}]".format(page)).click()
            self.goods_info()

            sleep(2)

    def goods_info(self):
        product_html = self.browser.page_source
        product_tree = etree.HTML(product_html)
        divs = product_tree.xpath("//div[contains(@class,'f_con4Center')]")
        product_items = []
        for div in divs:
            product_item = {}
            # print("product")
            # image_url = div.xpath("//div[@class='f_con4Center clearfix']/dl[1]/dt/a/img/@src")
            for _ in range(100):
                try:
                    #图片地址
                    image_url = "https://www.saclub.com.cn" + \
                                div.xpath("//div[contains(@class,'f_con4Center')]/dl/dt/a/img/@src")[+\
                                int("{}".format(_))].strip()
                    #商品名称
                    goods_name = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/h3/a/text()")[+\
                                int("{}".format(_))].strip()
                    #所需积分
                    score_need = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/p[@class='p1']/span/text()")[+ \
                        int("{}".format(_))].strip()
                    #兑换限制
                    limit_nums = div.xpath("//div[@class='f_con4Center clearfix']/dl/dd/p[@class='p1'][1]/text()")[+ \
                        int("{}".format((_ * 3) + 2))].strip()
                    print(image_url)
                    print(goods_name)
                    print("所需积分数:{}".format(score_need))
                    print(limit_nums)
                    try:
                        pic = requests.get(image_url,timeout=5)
                        # file_name = "iamge" + str(_) + ".jpg"  # 图片名
                        with open((r"E:\code\spiders\text\zhongshihua\img\{}.jpg".format(goods_name)), 'wb') as fp:
                            fp.write(pic.content)
                            fp.close()
                    except requests.exceptions.ConnectionError:
                        print("无法下载当前图片")
                        continue
                except:
                    pass
            # image_url = "https://www.saclub.com.cn"+div.xpath("//div[contains(@class,'f_con4Center')]/dl[1]/dt/a/img/@src")[0].strip()

    def get_img(self):
        print("get_image")
        t1 = time.time()
        # imgpage_html = self.browser.page_source
        # img_tree = etree.HTML(imgpage_html)
        # pic_url ="https://www.saclub.com.cn"+img_tree.xpath(".//div[@class='fdiv3']/a/img/@src")

        pic_url = self.browser.find_element_by_xpath(".//div[@class='fdiv3']/a/img").get_attribute('src')
        # print(pic_url1)
        # pic_url = "https://www.saclub.com.cn/{}".format(pic_url1)

        # urllib方法
        # resp = request.urlopen(pic_url)
        # raw = resp.read()
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
        # pic_url = "https://www.saclub.com.cn/imgmerge?amp;text=%C8%C8%B5%E3%BE%DB%BD%B914675.0&imageFile=/new/img/f_yzm.jpg&x=24&y=24&fontColor=000000&fontStyle=bold&fontName=%CB%CE%CC%E5&fontSize=24"
        resp = requests.get(pic_url, cookies=cooks, headers=headers)
        # raw = resp.content()
        sleep(2)
        with open("./images/zhongshihua/imgcode.gif", 'wb') as fp:
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
        self.process_request()
        sleep(0.1)
        t2 = time.time()
        ts1 = t2-t1
        ts1 = round(ts1,2)
        print("请求及登录耗时:{}".format(ts1))
        # 查询积分,个人信息
        self.inquire_score()
        sleep(0.1)
        t3 = time.time()
        ts2 = t3-t2
        ts2 = round(ts2, 2)
        print("查询积分耗时:{}".format(ts2))
        # 最近三个月兑换记录查询
        self.redemption__record()
        t4 = time.time()
        ts3 = t4-t3
        ts3 = round(ts3,2)
        print("最近三个月兑换查询记录耗时:{}".format(ts3))
        # 最近三个月加油记录
        self.refuel_record()
        sleep(0.1)
        t5 = time.time()
        ts4 = t5-t4
        ts4 = round(ts4,2)
        print("最近三个月加油记录:{}".format(ts4))
        # 积分商城商品信息
        self.product_info()
        sleep(0.1)
        t6 = time.time()
        ts5 = t6-t5
        ts5 = round(ts5,2)
        print("请求及登录耗时:{}s".format(ts1))
        print("查询积分耗时:{}s".format(ts2))
        print("最近三个月兑换查询记录耗时:{}s".format(ts3))
        print("最近三个月加油记录:{}s".format(ts4))
        print("积分商城商品信息获取耗时:{}s".format(ts5))
        return ts1,ts5

    @classmethod
    def myclass(cls):
        return 0

    @staticmethod
    def mystatic():
        pass

if __name__ == '__main__':
    s = Zhongshihua()
    try:
        ts11 = time.clock()
        ts1,ts5 = s.start_spider()
        ts12 = time.clock()- ts11
        ts13 = round(ts12, 2)-ts5
        ts14 = round(ts12, 2)-ts1
        print("抓取总耗(除去获取商品信息)时为:{}s".format(ts13))
        print("抓取总耗时(除去登录时间)为:{}s".format(ts14))
    except:
        pass
    finally:
        del s
