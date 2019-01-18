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

import time
import pymysql
import lxml


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

        self.browser.get("https://creditcard.pingan.com.cn/financing/login.screen?sid_source=CreditcardCP")

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


        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        # self.browser.save_screenshot("./images/pingan/pingan_login1.png")

        self.browser.find_element_by_id('j_username').send_keys(username)
        sleep(0.1)
        self.browser.find_element_by_class_name("f30").click()
        sleep(0.5)
        self.browser.find_element_by_id('j_password').send_keys(passwd)
        sleep(0.2)
        print("密码")

        # self.browser.find_element_by_class_name("pa_ui_keyboard_close pa_ui_keyboard_key").click()
        # sleep(1)
        # print("ok")

        # self.browser.find_element_by_id('j_password').send_keys(passwd)
        # 获取验证码
        location = self.browser.find_element_by_id("validateImg").location
        self.browser.save_screenshot("./images/pingan/pingan_login.png")
        page_snap_obj = Image.open("./images/pingan/pingan_login.png")

        size = self.browser.find_element_by_id("validateImg").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        images = page_snap_obj.crop((left, top, right, bottom))
        # sleep(1)
        # images.save("imcode.png")
        # image1 = images.save("./static/img/imgcode.png")
        images.save("./images/pingan/pingan_imgcode.png")
        # sleep(0.2)
        # images.show()

        sleep(1)





        #验证码
        ver_code = input("请输入验证码:")

        self.browser.find_element_by_id('check_code').send_keys(ver_code)

        self.browser.find_element_by_id('loginlink').click()

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
        sleep(18)
        # self.browser.switch_to.frame("body")

        try:
            # self.browser.switch_to.frame("header")
            # sleep(0.5)
            # self.browser.switch_to.default_content()
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
            credits = div.xpath(".//div[@class='pa_con01_c']//p[2]/span/text()")[0].strip()
            # # 本期账单日
            # current_billing_data = div.xpath('//div[2]/div[2]/div[1]/div[1]/p[1]/b/text()')
            current_billing_data = div.xpath(".//div[contains(@class,'pa_con02_ltime')]//p[1]/b/text()")[0].strip()
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

            print("用户名:{}".format(username))
            print("可用额度:{}".format(able_credit))
            print("信用额度:{}".format(credits))
            print("本期账单日:{}".format(current_billing_data))
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

        # sleep(10)




if __name__ == '__main__':
    zx = Pingan_C()
    t1 = time.clock()
    zx.process_request()
    t2 = time.clock()
    print("z最终耗时:{}".format(t2))

