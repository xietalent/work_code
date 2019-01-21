
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
from  tools.zhaohang.keybord_DD import DD_input

import lxml
import pytesseract
import pytesseract.pytesseract



import time

class SeleniumMiddleware():
    def __init__(self,timeout=None,service_args=[]):
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

    # def process_request(self,request,spider):
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

        user_name = "13728647735"
        passwd = "419078"

        sleep(1)
        uname = DD_input()
        uname.dd(user_name)
        sleep(2)

        uname.dd_table()
        sleep(1)
        uname = DD_input()
        uname.dd(passwd)
        sleep(0.5)

        uname.dd_table()
        sleep(0.2)

        uname.dd_enter()

        sleep(5)


        #输入手机验证码
        self.browser.find_element_by_id('btnSendCode').click()
        sleep(0.2)
        self.browser.find_element_by_id('btnSendCode').click()

        nums_code = input("请输入手机验证码:")

        self.browser.find_element_by_id('txtSendCode').send_keys(nums_code)
        sleep(0.2)

        self.browser.find_element_by_id('btnVerifyCode').click()
        #登录成功

        sleep(5)
        self.browser.find_element_by_xpath('//table[@id="mainTable"]/tbody/tr[1]/td/table/tbody/tr[1]/td[2]/table/tbody/tr[1]/td/table/tbody/tr/td/a[1]').click()
        sleep(2)
        self.browser.find_element_by_id('imgCreditCard').click()
        sleep(4)

        #切换到信息页面
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


        #还款信息
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
        # 已出账单查询
        self.browser.find_element_by_xpath('//div[@class="page-header-link"]//a').click()
        sleep(5)

        billed_html = self.browser.page_source
        # print("当前网址" + self.browser.page_source)
        with open(r"E:\code\spiders\text\zhaohang\billed_html.txt", "w+",encoding="utf8") as fp:
                    fp.write(billed_html)
                    fp.close()


        # # 未出账单查询
        # unbilled_html = self.browser.page_source
        # # print("当前网址" + self.browser.page_source)
        #
        # with open(r"E:\code\spiders\text\zhaohang\unbilled_html.txt", "w+", encoding="utf8") as fp:
        #     fp.write(unbilled_html)
        #     fp.close()






if __name__ == '__main__':
    s = SeleniumMiddleware()
    s.process_request()
    del s



