
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
        username = 4654545
        passwd = "123145cc"
        im_code = 1234
        self.browser.set_window_size(1200,800)
        self.browser.get("https://www.saclub.com.cn/goodlist.do?bool=2")
        sleep(4)
        im_code = self.get_img()

        self.browser.find_element_by_id("userName1").send_keys(username)
        sleep(0.1)
        self.browser.find_element_by_name("userPwd").send_keys(passwd)

        self.browser.find_element_by_name("mask").send_keys(im_code)
        sleep(0.2)

        self.browser.find_element_by_class_name("log_l").click()

        sleep(10)


    #查询积分
    def inquire_score(self):

        pass

    def get_img(self):
        print("getimg")
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
        print(545465)

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
            # self.browser.find_element_by_id('img_code_text')
            # self.browser.find_element_by_id('imgvalicode').send_keys(img_code)
            # sleep(1)
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
        self.inquire_score()
        sleep(5)


    pass



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