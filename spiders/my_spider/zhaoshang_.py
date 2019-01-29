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

from tools.zhaohang.keybord_DD import DD_input

import lxml
import pytesseract
import pytesseract.pytesseract

import time


class Zhanoshang_bank():
    def __init__(self, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        # self.browser = webdriver.PhantomJS()
        # self.browser = webdriver.Chrome()
        # self.browser_url = r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'
        # 'User-Agent'='Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE'
        # self.options = webdriver.ChromeOptions()
        # self.options.add_argument('User-Agent="Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36 QIHU 360SE"')
        # self.chrome_options = Options()
        # self.chrome_options.binary_location = self.browser_url
        # self.browser = webdriver.Chrome(chrome_options=self.chrome_options)
        # self.browser = webdriver.Chrome360(chrome_options=self.options)
        self.browser = webdriver.Ie()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        self.logger.debug('Ie is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
        # self.browser.get("https://user.cmbchina.com/User/Login")
        # self.browser.get("https://pbsz.ebank.cmbchina.com/CmbBank_GenShell/UI/GenShellPC/Login/Login.aspx?logintype=C")
        self.browser.get("https://pbsz.ebank.cmbchina.com/CmbBank_GenShell/UI/GenShellPC_EN/Login/Login.aspx")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(5)

        # html = self.browser.execute_script("return document.documentElement.outerHTML")
        # html = self.browser.find_element_by_xpath("//*").get_attribute("outerHTML")
        # print(html)

        self.input_user()
        sleep(5)

        # 输入手机验证码
        try:
            self.browser.find_element_by_id('btnSendCode').click()
            sleep(0.2)
            self.browser.find_element_by_id('btnSendCode').click()

            nums_code = input("请输入手机验证码:")

            self.browser.find_element_by_id('txtSendCode').send_keys(nums_code)
            sleep(0.2)

            self.browser.find_element_by_id('btnVerifyCode').click()
        except:
            pass
        # 登录成功

        sleep(5)
        self.browser.find_element_by_xpath(
            '//table[@id="mainTable"]/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/a[1]').click()
        sleep(2)
        self.browser.find_element_by_id('imgCreditCard').click()
        sleep(4)

        # 切换到信息页面
        self.browser.switch_to.frame("mainWorkArea")
        sleep(0.5)

        homepage_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)

        # with open(r"E:\code\spiders\text\zhaohang\zhaohang_homepage.txt", "w+",encoding="utf8") as fp:
        #         #     fp.write(homepage_html)
        #         #     fp.close()

        homepage_tree = etree.HTML(homepage_html)
        divs = homepage_tree.xpath(".//div[@class='page-panel']")

        zhanghu_items = []
        # 账户信息
        for div in divs:
            zhanghu_item = {}
            xinyong_edu_rmb = div.xpath(".//table/tbody/tr[@id='trxyed']//span[@id='RMBXYED']/text()")[0].strip()
            xinyong_edu_doller = div.xpath(".//table/tbody/tr[@id='trxyed']//span[@id='USXYED']/text()")[0].strip()
            keyong_edu_rmb = div.xpath(".//table/tbody/tr[@id='trkyed']//span[@id='RMBKYED']/text()")[0].strip()
            keyong_edu_doller = div.xpath(".//table/tbody/tr[@id='trkyed']//span[@id='USKYED']/text()")[0].strip()
            # 未出账本金
            wcz_principal = div.xpath(".//table/tbody/tr[@id='trwczfq']//span[@id='RMBWCZFQ']/text()")[0].strip()
            # 预借现金可借额度
            yjxianjin_rmb = div.xpath(".//table/tbody/tr[@id='tryjxj']//span[@id='RMBYJXJ']/text()")[0].strip()
            yjxianjin_doller = div.xpath(".//table/tbody/tr[@id='tryjxj']//span[@id='RMBYJXJ']/text()")[0].strip()

            # 账单日
            billing_day = div.xpath(".//table/tbody/tr[@id='myzdr']//span[@id='MYZD']/text()")[0].strip()

            # 账单类型
            billing_type = div.xpath(".//table/tbody/tr//span[@id='ZDLX']/text()")[0].strip()
            # 账务提醒时间
            remind_date = div.xpath(".//table/tbody/tr[@id='trzwtxsj']//span[@id='ZWTXSJ']/text()")[0].strip()
            # xinyong_edu = div.xpath("")[0].strip()

            print("信用额度为:{}人民币,即{}美元".format(xinyong_edu_rmb, xinyong_edu_doller))
            print("可用额度:{}元人民币,{}美元".format(keyong_edu_rmb, keyong_edu_doller))
            print("未出账分期本金:{}".format(wcz_principal))
            print("预借现金额度:{}人民币,{}美元".format(yjxianjin_rmb, yjxianjin_doller))
            print("账单日:{}".format(billing_day))
            print("账单类型:{}".format(billing_type))
            print("账务提醒时间:{}".format(remind_date))

        # 还款信息
        divs = homepage_tree.xpath(".//div[@class='page-panel']//div[@class='page-panel-content']")
        huankuan_items = []
        for div in divs:
            huankuan_item = {}
            bq_repayment_date = div.xpath("//tr[@id='trDQHQ']//span[@id='DQHQ']/text()")[0].strip()

            # 本期账单金额
            bq_bill_amount_r = div.xpath("//tr[@id='trLiterRMBZDJE']//span[@id='LiterRMBZDJE']/text()")[0].strip()
            bq_bill_amount_d = div.xpath("//tr[@id='trLiterRMBZDJE']//span[@id='LiterUSBZDJE']/text()")[0].strip()
            # 本期剩余应还
            bq_yinghuan_amount_r = div.xpath("//tr[@id='trLiterRMBBQJE']//span[@id='LiterRMBBQJE']/text()")[0].strip()
            bq_yinghuan_amount_d = div.xpath("//tr[@id='trLiterRMBBQJE']//span[@id='LiterUSBQJE']/text()")[0].strip()
            # 本期剩余最低还款金额
            bq_less_amount_r = div.xpath("//tr[@id='trzdje']//span[@id='RMBZDJE']/text()")[0].strip()
            bq_less_amount_d = div.xpath("//tr[@id='trzdje']//span[@id='USZDJE']/text()")[0].strip()

            print("----------------------------------------------")
            print("本期到期还款日:{}".format(bq_repayment_date))
            print("本期账单金额:{}rmb".format(bq_bill_amount_r))
            print("本期账单金额:{}美元".format(bq_bill_amount_d))
            print("本期剩余应还:{}人民币,{}美元".format(bq_yinghuan_amount_r, bq_yinghuan_amount_d))
            print("本期剩余最低还款金额:{}人民币,{}美元".format(bq_less_amount_r, bq_less_amount_d))

        # self.browser.switch_to.default_content()
        sleep(1)

    def billed(self):
        # 已出账单查询
        self.browser.find_element_by_xpath('//div[@class="page-header-link"]//a').click()
        sleep(5)
        try:
            self.browser.switch_to.frame("mainWorkArea")
        except:
            pass

        sleep(0.5)

        billed_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)
        # with open(r"E:\code\spiders\text\zhaohang\billed_html.txt", "w+", encoding="utf8") as fp:
        #     fp.write(billed_html)
        #     fp.close()

        billed_tree = etree.HTML(billed_html)
        divs = billed_tree.xpath(".//div[@class='page-panel-content']")
        items = []
        for div in divs:
            item = {}
            date1 = div.xpath(".//tbody/tr[2]/td/text()")
            date2 = div.xpath(".//tbody/tr[3]/td/text()")
            date3 = div.xpath(".//tbody/tr[4]/td/text()")
            date4 = div.xpath(".//tbody/tr[5]/td/text()")
            date5 = div.xpath(".//tbody/tr[6]/td/text()")
            date6 = div.xpath(".//tbody/tr[7]/td/text()")
            date7 = div.xpath(".//tbody/tr[8]/td/text()")
            date8 = div.xpath(".//tbody/tr[9]/td/text()")
            date9 = div.xpath(".//tbody/tr[10]/td/text()")
            date10 = div.xpath(".//tbody/tr[11]/td/text()")
            date11 = div.xpath(".//tbody/tr[12]/td/text()")
            date12 = div.xpath(".//tbody/tr[13]/td/text()")

            # 依次为:账单月份,人民币应还总额,人民币最低还款额,美元应还总额,美元最低还款额
            print("{}先生/女士,您过去一年已出账单为:".format("陈慧聪"))
            print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date1[0], date1[1], date1[2], date1[3],
                                                                              date1[4]))
            print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date2[0], date2[1], date2[2], date2[3],
                                                                              date2[4]))
            # print("{}期账单为:{}".format(date2[0], date2))
            print("{}期账单为:{}".format(date3[0], date3))
            print("{}期账单为:{}".format(date4[0], date4))
            print("{}期账单为:{}".format(date5[0], date5))
            print("{}期账单为:{}".format(date6[0], date6))
            print("{}期账单为:{}".format(date7[0], date7))
            print("{}期账单为:{}".format(date8[0], date8))
            print("{}期账单为:{}".format(date9[0], date9))
            print("{}期账单为:{}".format(date10[0], date10))
            print("{}期账单为:{}".format(date11[0], date11))
            print("{}期账单为:{}".format(date12[0], date12))

    def unbilled(self):
        # # 未出账单查询
        self.browser.find_element_by_xpath("//div[@class='page-header-link']/div/span[1]/a").click()
        sleep(5)
        try:
            self.browser.switch_to.frame("mainWorkArea")
        # sleep(0.2)
        # self.browser.switch_to.frame("ExplainPageFrame")
        except:
            pass
        unbilled_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)
        #
        # with open(r"E:\code\spiders\text\zhaohang\unbilled_html.txt", "w+", encoding="utf8") as fp:
        #     fp.write(unbilled_html)
        #     fp.close()
        unbilled_tree = etree.HTML(unbilled_html)
        divs = unbilled_tree.xpath(".//div[@class='page-panel-content']")

        for div in divs:
            try:
                res1 = div.xpath(".//span[@class='page-panel-nohistdeal-fund1']/text()")
                print(res1)

            except:
                print("未查询到您当前未出账单交易记录。---")
        # self.score_query()

    def score_query(self):
        self.browser.switch_to.default_content()
        sleep(0.2)
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[8]/a").click()

        sleep(0.2)
        # 积分查询
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[8]/ul/li[2]").click()
        # sleep(5)
        try:
            WebDriverWait(self.browser, 15).until(
                lambda x: self.browser.switch_to.frame("mainWorkArea").find_element_by_xpath(
                    "//tr[@class='dgHeader']/th[@class=['dgHeader']"))
        except:
            print("超时,获取积分信息失败")
            # self.browser.close()
        finally:
            pass
        try:
            self.browser.switch_to.frame("mainWorkArea")
            sleep(0.2)
            # self.browser.switch_to.frame("ExplainPageFrame")
        except:
            pass

        score_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)
        with open(r"E:\code\spiders\text\zhaohang\score_html.txt", "w+", encoding="utf8") as fp:
            fp.write(score_html)
            fp.close()
        score_tree = etree.HTML(score_html)
        divs = score_tree.xpath(".//div[@id='UpdatePanel2']")
        items = []
        for div in divs:
            item = {}
            score_name = div.xpath(".//tbody/tr[2]/td/text()")

            print("我的积分信息为:{}".format(score_name))

    def score_history(self):
        self.browser.switch_to.default_content()
        sleep(0.2)
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[8]/a").click()
        sleep(0.2)
        # 积分查询
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[8]/ul/li[3]").click()
        try:
            WebDriverWait(self.browser, 15).until(
                lambda x: self.browser.switch_to.frame("mainWorkArea").find_element_by_xpath("//input[@id='BtnQuery']"))
        except:
            print("超时,获取历史积分信息失败")
            # self.browser.close()
        finally:
            pass
        try:
            self.browser.switch_to.frame("mainWorkArea")
            sleep(0.2)
            # self.browser.switch_to.frame("ExplainPageFrame")
        except:
            pass

        self.browser.find_element_by_class_name("chosen-single").click()
        sleep(0.5)
        # month = input("要查询的月份(1-11):")
        month = "6"
        # self.browser.find_element_by_xpath("//select[@id='ddlYearMonthList']/option[@value='{}']".format(month)).click()
        self.browser.find_element_by_xpath("//ul[@class='chosen-results']/li[@class='active-result'][{}]".format(month)).click()
        sleep(0.5)
        self.browser.find_element_by_id("BtnQuery").click()
        sleep(3)
        his_score_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)
        with open(r"E:\code\spiders\text\zhaohang\his_score_html.txt", "w+", encoding="utf8") as fp:
            fp.write(his_score_html)
            fp.close()
        his_score_tree = etree.HTML(his_score_html)
        divs = his_score_tree.xpath(".//div[@id='UpdatePanel2']")
        items = []
        for div in divs:
            item = {}
            score_name = div.xpath(".//tbody/tr[2]/td/text()")

            print("我的历史积分信息为:{}".format(score_name))

    def transaction_record(self):
        self.browser.switch_to.default_content()
        sleep(0.1)
        self.browser.find_element_by_id("imgCommonCard").click()
        sleep(5)
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[1]/a").click()
        sleep(0.2)
        self.browser.find_element_by_xpath(".//ul[@id='menu']/li[1]/ul/li[2]/a").click()
        sleep(5)
        try:
            WebDriverWait(self.browser, 15).until(
                lambda x: self.browser.switch_to.frame("mainWorkArea").find_element_by_xpath("//div[@class='page-panel-content']"))
        except:
            print("超时,获取交易记录失败")
            # self.browser.close()
        finally:
            pass
        try:
            self.browser.switch_to.frame("mainWorkArea")
        except:
            pass
        #点击交易查询
        try:
            self.browser.find_element_by_xpath("//div[@class='page-panel-header']/sapn[@class='page-panel-header-more']/a[2]").click()
        except:
            self.browser.find_element_by_link_text("交易查询").click()
        else:
            print("查询记录错误")
        sleep(5)
        try:
            self.browser.switch_to.frame("mainWorkArea")
        except:
            pass
        #查询最近一年的交易记录
        self.browser.find_element_by_id("DateSpan_12").click()
        sleep(12)
        record_html = self.browser.page_source
        with open(r"E:\code\spiders\text\zhaohang\record_html.txt", "w+", encoding="utf8") as fp:
            fp.write(record_html)
            fp.close()
            record_tree = etree.HTML(record_html)
        divs = record_tree.xpath(".//div[@class='page-panel-content']")
        items = []
        for div in divs:
            item = {}
            record_name = div.xpath(".//tbody/tr/td/text()")
            # record_name = div.xpath(".//tbody/tr/td/text() | //tbody/tr/td/span/text()")
            record_amount = div.xpath(".//tbody/tr/td/span/text()")

            print("我的交易记录为:{}".format(record_name))
            print("我的交易金额为:{}".format(record_amount))



    def input_user(self):
        user_name = "13728647735"
        passwd = "419078"
        # 获取窗口句柄
        now_handle = self.browser.current_window_handle  # 获取当前窗口句柄
        print("当前窗口的句柄为:{}".format(now_handle))  # 输出当前获取的窗口句柄
        # 填写账号密码
        sleep(1)
        uname = DD_input()
        uname.dd(user_name)
        sleep(1)
        uname.dd_table()
        sleep(1)
        uname = DD_input()
        uname.dd(passwd)
        sleep(0.5)
        uname.dd_table()
        sleep(0.2)
        uname.dd_enter()

    def start_spider(self):
        t1 = time.time()
        self.process_request()
        t2 = time.time()
        sleep(0.5)
        self.billed()
        print("已出账单查询结束----------------------------")
        t3 = time.time()
        sleep(0.5)
        self.unbilled()
        print("未出账单查询结束----------------------------")
        t4 = time.time()
        sleep(0.5)
        self.score_query()
        print("积分信息查询结束----------------------------")
        t5 = time.time()
        sleep(0.5)
        self.score_history()
        print("历史积分查询完毕----------------------------")
        t6 = time.time()
        ts1 = t2 - t1
        ts1 = round(ts1, 2)
        print("登录阶段耗时为:{}s".format(ts1))

        ts2 = t3 - t2
        ts2 = round(ts2, 2)
        print("查询已出账单耗时:{}s".format(ts2))

        ts3 = t4 - t3
        ts3 = round(ts3, 2)
        print("查询未出账单耗时:{}s".format(ts3))

        ts4 = t5 - t4
        ts4 = round(ts4, 2)
        print("查询积分信息耗时:{}s".format(ts4))

        ts5 = t6 - t5
        ts5 = round(ts5, 2)
        print("查询历史积分耗时:{}".format(ts5))

        t7 = time.time()
        self.transaction_record()
        t8 = time.time()
        ts6 = t8-t7
        ts6 = round(ts6,2)
        print("最近一年的交易记录查询时间为:{}".format(ts6))

        return ts6


if __name__ == '__main__':
    s = Zhanoshang_bank()
    try:
        time.clock()
        ts6 = s.start_spider()
        ts = time.clock()- ts6
        ts = round(ts, 2)
        print("总耗时为:{}s".format(ts))
    except:
        pass
    del s
