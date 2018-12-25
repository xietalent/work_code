
from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from time import sleep
import lxml
from lxml import etree

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome()
        # self.browser.set_window_rect(1400,700)
        # self.browser.set_page_load_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser,self.timeout)

    # def __del__(self):
    #     self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")

        self.browser.get("https://www.zhihu.com/signup?next=%2F")
        sleep(3)

        self.browser.find_element_by_xpath(".//body[@class='EntrySign-body']//div[@class='SignContainer-switch']/span").click()
        sleep(3)


        page_html2 = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        response = etree.HTML(page_html2)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")




        self.browser.save_screenshot("zhihu001.png")
        sleep(1)
        # imgcode = input("请输入验证码:")
        # sleep(2)
        # self.browser.find_element_by_xpath(".//div[(@class='SignContainer-inner')]//div[(@class='SignFlowInput SignFlow-accountInputContainer')]//input/@value").send_keys("1598749576@qq.com")
        self.browser.find_element_by_xpath(".//div[(@class='SignContainer-inner')]//div[(@class='SignFlowInput SignFlow-accountInputContainer')]//input").send_keys("1598749576@qq.com")
        self.browser.find_element_by_xpath(".//div[(@class='SignContainer-inner')]//div[(@class='SignFlow-password')]//input").send_keys("zx150218")
        # self.browser.find_element_by_name("imgCode").send_keys("{}".format(imgcode))
        sleep(1)

       # 登录
        self.browser.find_element_by_xpath(".//div[(@class='SignContainer-inner')]//div[(@class='Login-content')]//button[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()
        sleep(3)

        page_html2 = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        response = etree.HTML(page_html2)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")

        self.browser.save_screenshot("zhihu001.png")
        sleep(1)
        imgcode = input("请输入验证码:")

        #验证码
        self.browser.find_element_by_xpath(".//div[(@class='SignContainer-inner')]//div[(@class='Input-wrapper')]//input").send_keys("{}".format(imgcode))
        sleep(1)


        #再登录
        self.browser.find_element_by_xpath(
            ".//div[(@class='SignContainer-inner')]//div[(@class='Login-content')]//button[@class='Button SignFlow-submitButton Button--primary Button--blue']").click()
        sleep(3)




#以下未解决





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
                "my_integral":my_integral,
            }
            items.append(item)
            print(my_integral)
            print(type(my_integral))
            print(items)

        #2  打开信用卡积分明细查询
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[2]/a").click()
        sleep(3)

        #点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen03.png")
        page_html2 = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        response = etree.HTML(page_html2)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            item = {}
            bill = div.xpath(".//div[@class='details_member']//div[@class='faqBox']/em/text()")

            item = {
                "bill": bill,
            }
            items.append(item)
            print(bill)
            print(type(bill))
            print(items)



        return page_html


    def parses(self,page_html):
        response = etree.HTML(page_html,etree.HTMLParser)
        # my_integral = response.xpath(".//div[@class='boundCarBox']/div").extract().strip()
        my_integral = response.xpath(".//b[contains(text(),_积分)]").extract().strip()
        print(my_integral)


if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()
    # s.parse()

