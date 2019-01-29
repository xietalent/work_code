
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
from tools.zhaohang.keybord_DD import DD_input

import time
import requests

class China_bank():
    def __init__(self,timeout=None,service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def login_request(self):
        self.logger.debug('Ie is Starting')
        self.browser.get("https://jf365.boc.cn/BOCGIFTORDERNET/toLoginJsp.do?")
        sleep(3)
        # 获取验证码
        # img_code = self.get_img()
        username,passwd = self.user_info()

        #输入密码
        # self.input_passwd(passwd)
        sleep(0.5)


        sleep(1)
        self.browser.find_element_by_id("textfield").send_keys(username)
        # self.browser.find_element_by_id("textfield").send_keys(passwd)
        sleep(0.1)
        #输入密码
        self.input_passwd(passwd)
        sleep(0.1)
        # 获取验证码
        img_code = self.get_img()
        sleep(0.1)
        self.browser.find_element_by_id("textfield4").send_keys(img_code)
        sleep(0.1)
        self.browser.find_element_by_id("button").click()
        # page_html2 = self.browser.page_source
        # print("当前网址"+self.browser.page_source)
        # return page_html

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
        self.browser.find_element_by_xpath("//div[@id='user_content']/div[@class='tag_div']/ul/li[7]/a").click()
        sleep(3)

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
        # imgpage_html = self.browser.page_source
        # img_tree = etree.HTML(imgpage_html)
        # pic_url ="https://www.saclub.com.cn"+img_tree.xpath(".//div[@class='fdiv3']/a/img/@src")

        # pic_url = self.browser.find_element_by_xpath(".//div[@class='fdiv3']/a/img").get_attribute('src')
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
        # resp = requests.get(pic_url, cookies=cooks, headers=headers)
        # raw = resp.content()
        # sleep(2)
        # with open("./images/china_bank/imgcode.gif", 'wb') as fp:
        #     for data in resp.iter_content(128):
        #         fp.write(data)

        try:
            # 截取验证码的截图
            location = self.browser.find_element_by_id("imgID").location
            self.browser.save_screenshot("./images/china_bank/login_imcode.png")
            page_snap_obj = Image.open("./images/china_bank/login_imcode.png")

            size = self.browser.find_element_by_id("imgID").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save("./images/china_bank/cb_imcode.png")
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
        self.login_request()
        sleep(0.1)
        self.my_score()
        sleep(0.1)
        self.order_query()
        sleep(0.1)
        self.score_h_query()
        sleep(0.5)



if __name__ == '__main__':
    tsa = time.clock()
    res = China_bank()
    res.start_spider()
    tsa2 = time.clock()
    tsa2 = round(tsa2,2)
    print("爬取总耗时为:{}".format(tsa2))
    sleep(5)
    del res



