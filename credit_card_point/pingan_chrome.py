# -*- coding: utf-8 -*-

import time
import pymysql
import lxml
import os

from threading import Thread
from selenium import webdriver
from logging import getLogger
from aip import AipOcr
from time import sleep
from selenium.webdriver.chrome.options import Options
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class Pingan_C():
    def __init__(self,timeout=None):
    # def __init__(self,phone_num,passwd,timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()

        # 设置chrome浏览器无界面模式
        # chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(chrome_options=chrome_options)

        self.browser = webdriver.Chrome()
        # self.browser = webdriver.Ie()
        # self.phone_num = phone_num
        # self.passwd = passwd

    def __del__(self):
        self.browser.close()

    def process_request(self):
        ta = time.time()
        # username = input("请输入用户名:")
        # username = "15071469916"
        username = "13728647735"
        # username = "530328199502132116"
        # username = "张雄"
        # passwd = input("请输入一账通密码:")
        passwd = "419078CHU"
        # passwd = "zc006688"
        self.logger.debug('Chrome is Starting')
        self.browser.get("https://creditcard.pingan.com.cn/financing/login.screen?")
        sleep(3)
        #切换至iframe
        self.browser.switch_to.frame("toalogin")

        # #获取验证码
        # location = self.browser.find_element_by_id("validateImg").location
        # self.browser.save_screenshot("./images/pingan/pingan_login.png")
        # page_snap_obj = Image.open("./images/pingan/pingan_login.png")
        #
        # size = self.browser.find_element_by_id("validateImg").size
        # left = location['x']
        # top = location['y']
        # right = location['x'] + size['width']
        # bottom = location['y'] + size['height']
        #
        # images = page_snap_obj.crop((left, top, right, bottom))
        # # sleep(1)
        # # images.save("imcode.png")
        # # image1 = images.save("./static/img/imgcode.png")
        # images.save("./images/pingan/pingan_imgcode.png")
        # sleep(0.2)
        # images.show()

        sleep(0.1)
        # location = self.browser.find_element_by_id("imgCode").location
        # self.browser.save_screenshot("./images/pingan/pingan_login1.png")

        self.browser.find_element_by_id('j_username').send_keys(username)
        sleep(0.1)
        self.browser.find_element_by_class_name("f30").click()
        sleep(0.5)
        self.browser.find_element_by_id('j_password').send_keys(passwd)
        sleep(0.2)
        print("密码")

        read = Read_image(self.browser)
        read.read_img_name()

        # 获取验证码
        # location = self.browser.find_element_by_id("validateImg").location
        # self.browser.save_screenshot("./images/pingan/pingan_login.png")
        # page_snap_obj = Image.open("./images/pingan/pingan_login.png")
        #
        # size = self.browser.find_element_by_id("validateImg").size
        # left = location['x']+50
        # top = location['y']+170
        # right = location['x'] + size['width']+55
        # bottom = location['y'] + size['height']+200
        #
        # images = page_snap_obj.crop((left, top, right, bottom))
        # # sleep(1)
        # # images.save("imcode.png")
        # # image1 = images.save("./static/img/imgcode.png")
        # images.save("./images/pingan/pingan_imgcode.png")
        # # sleep(0.2)
        # images.show()
        # sleep(1)
        #
        # #验证码
        # ver_code = input("请输入验证码:")
        # self.browser.find_element_by_id('check_code').send_keys(ver_code)
        # self.browser.find_element_by_id('loginlink').click()
        tb = time.time()

        tc = tb-ta
        tc = round(tc,2)
        print("验证码耗时:{}".format(tc))

        #登录时间
        t1 = time.time()
        try:
            WebDriverWait(self.browser, 25).until(lambda x: self.browser.find_element_by_xpath('//frame[@id="body"]'))
            # WebDriverWait(self.browser, 25).until(lambda x: self.browser.find_element_by_xpath('//frame[@id="body"]'))
        except:
            print("超时,获取积分失败")
            # self.browser.close()
        finally:
            pass

        self.browser.switch_to.frame("body")

        try:
            WebDriverWait(self.browser, 10).until(lambda x: self.browser.find_element_by_xpath('//frame[@id="wait"]'))
        except:
            print("超时,获取积分失败")
            # self.browser.close()
        finally:
            pass
        # self.browser.switch_to.frame("body")

        #next
        # sleep(15)
        sleep(1)
        # self.browser.switch_to.frame("body")

        try:
            sleep(0.5)
            self.browser.switch_to.frame("body1")
        except:
            pass
        t2 = time.time()
        t3 = t2 - t1
        t3 = round(t3, 2)
        print("登录耗时:{}".format(t3))


        #解析
        page_html = self.browser.page_source
        # 下载html
        # with open(r"E:\code\spiders\text\pinan_home_html2.txt", "w+",encoding="utf8") as fp:
        #     fp.write(page_html)
        #     fp.close()

        # sleep(1)
        html_tree = etree.HTML(page_html)

        divs = html_tree.xpath(".//div[@id='context']")
        items = []
        for div in divs:
            item = {}
            username = div.xpath(".//div[@class='pa_name']/div[contains(@class,'fl') and contains(@class,'m_l15') and contains(@class,'w126')]/h2/text()")[0].strip()
            # 可用额度
            able_credit = div.xpath(".//div[@class='pa_con01_c']//p[1]/span/text()")[0].strip()
            # # 信用额度
            credit = div.xpath(".//div[@class='pa_con01_c']//p[2]/span/text()")[0].strip()
            # # 本期账单日
            # current_billing_data = div.xpath('//div[2]/div[2]/div[1]/div[1]/p[1]/b/text()')
            current_billing_date = div.xpath(".//div[contains(@class,'pa_con02_ltime')]//p[1]/b/text()")[0].strip()
            # #本期还款日
            current_repayment_date = div.xpath(".//div[contains(@class,'pa_con02_ltime')]//p[2]/b/text()")[0].strip()
            # #本期应还额
            new_balance = div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[1]/td[2]/span/text()")[0].strip()
            # #本期最低应还
            minimum_return = div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[2]/td[2]/span/text()")[0].strip()
            # #本期剩余应还
            remainder = div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[3]/td[2]/text()")[0].strip()
            # #本期剩余最低应还额
            remainder_minimum_return =div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[4]/td[2]/text()")[0].strip()

            item["username"] = username
            item["able_credit"] = able_credit
            item["credit"] = credit
            item["current_billing_date"] = current_billing_date
            item["current_repayment_date"] = current_repayment_date
            item["new_balance"] =new_balance
            item["minimum_return"] = minimum_return
            item["remainder"] = remainder
            item["remainder_minimum_return"] = remainder_minimum_return
            items.append(item)
            print(items)

            # username=item["username"]
            # able_credit=item["able_credit"]
            # credit=item["credit"]
            # current_billing_date=item["current_billing_date"]
            # current_repayment_date=item["current_repayment_date"]
            # new_balance=item["new_balance"]
            # minimum_return=item["minimum_return"]
            # remainder=item["remainder"]
            # remainder_minimum_return=item["remainder_minimum_return"]
            #连接数据库
            sql_conn = Mysql_input()
            # sql_conn.set_data(username,able_credit,credit,current_billing_date,current_repayment_date,new_balance,minimum_return,remainder,remainder_minimum_return)
            th2 = Thread(target=sql_conn.set_data, args=(username,able_credit,credit,current_billing_date,
                                                         current_repayment_date,new_balance,minimum_return,remainder,remainder_minimum_return))
            th2.start()

            print("用户名:{}".format(username))
            print("可用额度:{}".format(able_credit))
            print("信用额度:{}".format(credit))
            print("本期账单日:{}".format(current_billing_date))
            print("本期还款日{}".format(current_repayment_date))
            print("本期应还额:{}".format(new_balance))
            print("本期最低应还:{}".format(minimum_return))
            print("本期剩余应还:{}".format(remainder))
            print("本期剩余最低应还额:{}".format(remainder_minimum_return))

        #获取积分信息:
        print("获取积分信息")
        sleep(1)
        event2 =self.browser.find_element_by_xpath("//ul[@id='nav_child']/li[4]/a")
        ActionChains(self.browser).move_to_element(event2).perform()
        sleep(0.5)
        # event2 = self.browser.find_element_by_xpath("//ul[@class='nav_ul_li02']/li[1]/a[1]")
        # ActionChains(self.browser).move_to_element(event2).perform()
        # sleep(1)
        self.browser.find_element_by_xpath("//ul[@id='nav_child']/li[4]/ul[@class='nav_ul_li02']/li[1]/a[1]").click()

        t4 = time.time()
        try:
            WebDriverWait(self.browser, 25).until(lambda x: self.browser.find_element_by_xpath('//div[@id="id_qwpdZ"]/div/p'))
        except:
            print("超时,获取积分失败")
            self.browser.close()
        finally:
            pass

        t5 = time.time()
        t6 = t5-t4
        print('获取万里通积分页面耗时:{}'.format(t6))
        t6 = round(t6,2)
        # sleep(6)
        # 下载html
        page_html2 = self.browser.page_source

        # with open(r"E:\code\spiders\text\pingan_bank\score_html.txt", "w+",encoding="utf8") as fp:
        #     fp.write(page_html2)
        #     fp.close()

        html_tree2 = etree.HTML(page_html2)

        divs = html_tree2.xpath(".//div[@class='right_box']")

        wanli_items = []
        for div in divs:
            wanli_item={}
            # 截止目前万里通积分总数
            all_score = div.xpath(".//div[@id='id_qwpdZ']/div/p/text()")[0].strip()
            # 本期余额
            benqi_yue = div.xpath(".//div[@id='id_qwpdL']//tr/td[2]/text()")[0].strip()
            # 本期新增
            benqi_xinzeng = div.xpath(".//div[@id='id_qwpdL']//tr/td[4]/text()")[0].strip()
            # 本期调整
            benqi_tiaozheng = div.xpath(".//div[@id='id_qwpdL']//tr[2]/td[4]/text()")[0].strip()
            # 即将失效
            about_to_fail = div.xpath(".//div[@id='id_qwpdL']//tr[2]/td[4]/text()")[0].strip()

            print("目前万里通积分总数:{}".format(all_score))
            print("本期余额:{}".format(benqi_yue))
            print("本期新增:{}".format(benqi_xinzeng))
            print("本期调整:{}".format(benqi_tiaozheng))
            print("即将失效积分数:{}".format(about_to_fail))
        t7 = time.time()
        t8 = t7-t4
        t8 = round(t8,2)
        print("积分获取总耗时:{}".format(t8))

        #携程积分信息:
        sleep(0.5)
        event3 = self.browser.find_element_by_xpath('//a[@id="_$_sub4"]')
        ActionChains(self.browser).move_to_element(event3).perform()
        sleep(1)
        # event2 = self.browser.find_element_by_xpath("//ul[@class='nav_ul_li02']/li[1]/a[1]")
        # ActionChains(self.browser).move_to_element(event2).perform()
        # sleep(1)
        self.browser.find_element_by_xpath('//body/div[2]/div[1]/div/div[2]/ul[4]/li[2]/a').click()
        # sleep(6)

        t9 = time.time()
        try:
            WebDriverWait(self.browser, 25).until(lambda x: self.browser.find_element_by_xpath('//div[@id="main"]/div[2]/div/div/h1'))
        except:
            print("超时,获取积分失败")
            self.browser.close()
        finally:
            pass

        # 下载html
        page_html3 = self.browser.page_source
        #
        xiecheng_tree = etree.HTML(page_html3)
        sleep(0.2)
        # with open(r"E:\code\spiders\text\pingan_bank\score_html.txt", "w+", encoding="utf8") as fp:
        #     fp.write(page_html3)
        #     fp.close()
        divs = xiecheng_tree.xpath("//div[@class='right_box']")

        for div in divs:
            #     #截止目前携程积分明细
            #     #交易日期:
            #     trans_date = div.xpath("")
            #     # 入账日期
            #     all_score = div.xpath("")
            #     #积分类型
            #     all_score = div.xpath("")
            #     # 币种
            #     all_score = div.xpath("")
            #     #交易本金
            #     all_score = div.xpath("")
            #     #积分累积
            #     all_score = div.xpath("")
            #     #卡号末四位
            #     all_score = div.xpath("")

            # 没有记录
            no_record = div.xpath('//*[@id="jfForm"]/div[2]/div[2]/p/text()')[0].strip()

            # print(':{}'.format(trans_date))
            # print(':{}'.format())
            # print(':{}'.format())
            # print(':{}'.format())
            # print(':{}'.format())
            # print(':{}'.format())
            print('你好:{}'.format(no_record))
        t10 = time.time()
        t11 = t10-t9
        t11 = round(t11,2)
        print("携程积分页耗时:{}".format(t11))

class Read_image():
    def __init__(self,browser,timeout=None):
        self.timeout = timeout
        self.browser = browser

    def read_img_name(self):
        image_format_list = [".jpg", ".png", ".bmp", ".jpeg", ".tiff", ".psd", ".swf", ".svg", ".tga", ".pcd", ".jfif",".webp", ".Png-8", ".png-24"]
        try:
            location = self.browser.find_element_by_id("validateImg").location
            self.browser.save_screenshot("./images/pingan/pingan_login.png")
            page_snap_obj = Image.open("./images/pingan/pingan_login.png")

            size = self.browser.find_element_by_id("validateImg").size
            left = location['x'] + 50
            top = location['y'] + 170
            right = location['x'] + size['width'] + 55
            bottom = location['y'] + size['height'] + 200

            images = page_snap_obj.crop((left, top, right, bottom))

            images.save("./images/pingan/pingan_imgcode.png")
            # sleep(0.2)
            images.show()
            sleep(0.1)

            all_image = os.listdir(r".\images\pingan")
            for im_name in all_image:
                # 辨别是否是图片格式
                a, b = os.path.splitext(im_name)
                if b in image_format_list:
                    image0 = im_name
                    print(image0)
                    image1 = r".\images\pingan\{}".format(image0)
                    image = Image.open(image1)
                    try:
                        self.read_p(image0, image)
                    except:
                        break
                    finally:
                        pass
                    # 添加至已完成list
                    # self.completed_list.append(image0)
                else:
                    pass
            # print(self.completed_list)
        except:
            pass

    def read_p(self, image0, image):
        # 你的 APPID AK SK
        APP_ID = '15193395'
        API_KEY = 'HWeCszHYYnbWxcVGFLosY0KS'
        SECRET_KEY = 'FoXrkDDgoqL3gi2ynmnhtm8bjiSiiIe6'

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        """ 读取图片 """

        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        # 调用通用文字识别（高精度版）
        # client.basicAccurate(image)

        """ 如果有可选参数 """
        # options = {
        #     "detect_direction":"true",
        #     "probability":"true"
        # }
        options = {}
        options["recognize_granularity"] = "big"
        options["language_type"] = "CHN_ENG"
        options["detect_direction"] = "true"
        options["detect_language"] = "true"
        options["vertexes_location"] = "true"
        options["probability"] = "true"

        # 灰度化
        image = image.convert('L')
        # 杂点清除掉。只保留黑的和白的。返回像素对象
        data = image.load()
        w, h = image.size
        for i in range(w):
            for j in range(h):
                if data[i, j] > 180:
                    data[i, j] = 255  # 纯白
                else:
                    data[i, j] = 0  # 纯黑

        # s = input("是否显示处理后图片:")
        s = "否"
        if s == "是":
            image.show()
            # sleep(5)
            # image.close()
        else:
            pass
        #保存处理后图片
        image.save(r'images\pingan\clean_captcha.png')
        image2 = get_file_content(r"images\pingan\clean_captcha.png")

        # 带参数调用通用文字识别(高精度版)
        result = client.basicAccurate(image2, options)
        res = result["words_result"]
        # print("识别结果为:")
        s2 = image0.split("\\")[-1]
        s3 = s2.split('.')[0]

        # 写入文件
        # for res1 in res:
        #     with open(r'识别结果\{}.txt'.format(s3), "a", ) as fp:
        #         fp.write(res1["words"])
        #         fp.close()
        print("该图片的识别结果为:" + result["words_result"][0]["words"])
        # 验证码
        ver_code = input("请输入验证码:")
        self.browser.find_element_by_id('check_code').send_keys(ver_code)
        self.browser.find_element_by_id('loginlink').click()

class Mysql_input(object):
    def __init__(self, host="47.97.217.36", user="root", password="root", database="bank", port=3306, charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset

    def connect(self):
        self.conn = pymysql.connect(host=self.host, user=self.user, password=self.password, database=self.database,port=self.port, charset=self.charset)
        self.cursor = self.conn.cursor()

    def get_data(self):
        self.connect()
        sql_2 = "select * from pingan_bank order by id DESC limit 1;"
        self.cursor.execute(sql_2)
        res = self.cursor.fetchone()
        return res

    def set_data(self,username,able_credit,credit,current_billing_date,current_repayment_date,new_balance, minimum_return,remainder,remainder_minimum_return):
        self.connect()
        try:
            # sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral, bill)
            sql_1 = "INSERT INTO pingan_bank VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(username, able_credit, credit, current_billing_date, current_repayment_date,new_balance, minimum_return,remainder,remainder_minimum_return)
            self.cursor.execute(sql_1)
            self.conn.commit()
            print("添加成功")
            res = self.cursor.fetchall()
            if res != None:
                self.close()
                return res
        except:
            self.conn.rollback()

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    pingan = Pingan_C()
    t1 = time.clock()
    pingan.process_request()
    t2 = time.clock()
    print("z最终耗时:{}".format(t2))
    del pingan

    # sql_1 = Mysql_input()
    # sql_1.set_data("陈慧聪 ","¥-8,238.26","¥-8,238.26","123","123","123","123","123","123")

    # read = Read_image()
    # read.read_img_name()

# [{'username': '陈慧聪', 'able_credit': '¥-8,238.26', 'credit': '¥22,000.00', 'current_billing_date': '2019.03.17', 'current_repayment_date': '2019.04.05', 'new_balance': '¥30,638.33', 'minimum_return': '¥9,852.33', 'remainder': '¥0.00', 'remainder_minimum_return': '¥0.00'}]