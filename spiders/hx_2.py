from selenium import webdriver
from logging import getLogger
from aip import AipOcr
from time import sleep
from lxml import etree
from urllib import request
from PIL import Image
# from .models import Card_score
from threading import Thread

import pymysql
import lxml
import pytesseract
import pytesseract.pytesseract


class SeleniumMiddleware():
    # def __init__(self, name, passwd, img_code=None,timeout=None, service_args=[]):
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.name = name
        # self.passwd = passwd
        # self.img_code = img_code
        self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
        self.browser.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(2)
        page_html2 = self.browser.page_source

        # 截取验证码的截图
        location = self.browser.find_element_by_id("imgCode").location
        self.browser.save_screenshot("feng.png")
        page_snap_obj = Image.open("feng.png")

        size = self.browser.find_element_by_id("imgCode").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        images = page_snap_obj.crop((left, top, right, bottom))
        # sleep(1)
        # images.save("imcode.png")
        # image1 = images.save("./static/img/imgcode.png")
        images.save("./static/img/imgcode.png")
        # images.show()
        brows = self.browser
        sleep(20)
        print("继续爬取")
        # print("brows的type:"+ type(brows))
        return  Logindo()


class Logindo():
    def __init__(self,name,passwd,img_number,brows):
    # def __init__(self,brows):
        self.name = name
        self.passwd = passwd
        self.img_number = img_number
        self.browser = brows

    def process_req(self):
        "select * from test_limit order by id DESC limit 1;"
        # 读取图片
        img_number =self.img_number
        # img_number = input("请输入验证码:")
        self.browser.save_screenshot("jifen001.png")

        sleep(1)
        # imgcode = input("请输入验证码:{}".format(result))
        sleep(2)
        self.browser.find_element_by_id("doLogin_loginNumber").send_keys("{}".format(self.name))
        # self.browser.find_element_by_id("doLogin_loginNumber").send_keys("6259691129820511")
        # self.browser.find_element_by_id("doLogin_loginPwd").send_keys("zc006688")
        self.browser.find_element_by_id("doLogin_loginPwd").send_keys("{}".format(self.passwd))
        self.browser.find_element_by_name("imgCode").send_keys("{}".format(img_number))

        sleep(5)


        # 登录
        self.browser.find_element_by_id("doLogin_0").click()
        sleep(3)

        # 我的积分
        self.browser.find_element_by_id("leftMenu1").click()
        sleep(2)

        # 1  打开可用积分查询栏
        # self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a/@href").click()
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a").click()
        sleep(3)

        # 点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen02.png")
        page_html = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        items = []
        response = etree.HTML(page_html)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            item = {}
            my_integral = div.xpath(".//div[@class='boundCarBox']//div/b/text()")[0]

            item = {
                "my_integral": my_integral,
            }

            items.append(item)
            print(my_integral)
            print(type(my_integral))
            print(items)

        # 2  打开信用卡积分明细查询
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[2]/a").click()
        sleep(3)
        # 点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen03.png")
        page_html2 = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        response = etree.HTML(page_html2)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            # item = {}
            bill = div.xpath(".//div[@class='details_member']//div[@class='faqBox']/em/text()")
            item = {
                "bill": bill,
            }
            items.append(item)
            print(bill)
            # print(type(bill))
            # print(items)
            # 存入字典
            print(items)
            # insert_ = Integral.objects.create(**items)
            # return items

        items = [{'my_integral': '0积分'}, {'bill': []}]
        # score = items[0]['my_integral']
        # record = items[1]['bill']
        # if record == []:
        #     record = "暂无消费记录"
        #
        # items = {
        #     "score":score,
        #     "record": record,
        # }
        # print(items)
        # insert_ = Card_score.objects.create(items)

        # 创建线程存储数据
        score = items[0]['my_integral']
        # print("my_in"+my_integral)
        record = items[1]['bill']
        if record == []:
            record = "当前没有消费记录"
        ss = Mysql_input()
        t2 = Thread(target=ss.set_data, args=(score, record,))
        print("启动线程2")
        t2.start()

        # insert_ = Card_score.objects.create(**items)
        return page_html


class Mysql_input(object):
    def __init__(self, host="47.97.217.36", user="root", password="root", database="user", port=3306, charset="utf8"):
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
        sql_2 = "select * from user1 order by id DESC limit 1;"
        self.cursor.execute(sql_2)
        res = self.cursor.fetchone()
        return res

    def set_data(self, my_integral="900", bill="12月消费100积分"):
        self.connect()
        try:
            sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral, bill)
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


# class  Runs():
#     def __init__(self,page_html):
#         self.page_html = page_html
#
#     def page_htm(self):
#
#         print(self.page_html)


if __name__ == '__main__':
    s = SeleniumMiddleware("6259691129820511","zc006688")
    # my_integral, bill = s.process_request()
    s.process_request()
