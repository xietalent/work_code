# -*- coding: utf-8 -*-

from selenium import webdriver
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
from selenium.webdriver.common.action_chains import ActionChains
from threading import Thread

import pymysql
import time
import re


class Xingye_C():
    def __init__(self,timeout=None):
    # def __init__(self,phone_num,passwd,timeout=None):
        self.logger = getLogger(__name__)
        self.timeout = timeout

        chrome_options = Options()
        # 设置chrome浏览器无界面模式
        # chrome_options.add_argument('--headless')
        # self.browser = webdriver.Chrome(chrome_options=chrome_options)
        self.browser = webdriver.Chrome()

        # self.phone_num = phone_num
        # self.passwd = passwd

    def __del__(self):
        self.browser.close()
        # self.browser.quit()

    def card_num(self):
        print("卡号登录")
        # card_nums = input("请输入卡号:")
        # passwd = input("请输入登录密码:")

        card_nums = "5240707969398113"
        passwd = "zy760209"
        self.logger.debug('Chrome is Starting')
        self.browser.get("https://personalbank.cib.com.cn/pers/main/login.do")

        self.browser.find_element_by_xpath(".//div[@class='wrap']//form[@id='loginForm']//li[2]/label").click()
        self.browser.find_element_by_id("loginNameTemp").send_keys(card_nums)
        sleep(2)
        self.browser.find_element_by_id("loginNextBtn").click()
        sleep(2)
        self.browser.find_element_by_id("iloginPwd").send_keys(passwd)
        self.browser.find_element_by_id("loginSubmitBtn").click()

        page_html = self.browser.page_source
        return page_html

    def username(self):
        print("将通过登录名+密码的方式登录")
        # username = input("请输入登录名:")
        username = "15071469916"
        # passwd = input("请输入登录密码:")
        passwd = "zc006688"
        self.logger.debug('Ie is Starting')
        self.browser.get("https://personalbank.cib.com.cn/pers/main/login.do")

        sleep(3)
        # location = self.browser.find_element_by_id("imgCode").location
        my_cookie = self.browser.get_cookies()
        # print(my_cookie)
        # self.browser.find_element_by_class_name('login-type-label').click()
        self.browser.find_element_by_xpath(".//div[@class='wrap']//form[@id='loginForm']//li[3]/label").click()
        sleep(2)
        self.browser.save_screenshot("./images/xylogin1.png")
        # self.browser.find_element_by_xpath('j_username').send_keys(username)
        self.browser.find_element_by_id('loginNameTemp').send_keys(username)

        # self.browser.find_elements_by_link_text()
        sleep(3)
        buttons = self.browser.find_element_by_id('iloginPwd').send_keys(passwd)
        # sleep(5)
        # for button in buttons:
        #     if button.text == "Post":
        #         button.click()
        # sleep(3)
        # 验证码
        # ver_code = input("请输入验证码:")
        # self.browser.find_element_by_id('check_code').send_keys(ver_code)
        # self.browser.find_element_by_id('mobilecaptchafield').send_keys(ver_code)

        self.browser.find_element_by_id('loginSubmitBtn').click()
        # next
        sleep(3)
        self.browser.save_screenshot("./images/jifen_page.png")
        page_html = self.browser.page_source
        return page_html

    def phone_num(self):
        print("将通过手机号+验证码+登录密码的方式登录")
        # ph_num = input("请输入手机号码:")
        # spasswd = 760209
        # passwd = input("请输入密码:")

        # ph_num = "13929902965"
        # passwd = "00233"

        ph_num = "15071469916"
        passwd = "00233"

        self.logger.debug('Chrome is Starting')
        self.browser.get("https://personalbank.cib.com.cn/pers/main/login.do")

        self.browser.find_element_by_id("loginNameTemp").send_keys(ph_num)
        # self.browser.
        try:
            print("验证码")
            # 截取验证码的截图
            location = self.browser.find_element_by_class_name("yardimg").location
            print("ok")
            self.browser.save_screenshot("./images/xingye/xy_login1.png")
            page_snap_obj = Image.open("./images/xingye/xy_login1.png")

            size = self.browser.find_element_by_class_name("yardimg").size
            left = location['x']
            top = location['y']
            right = location['x'] + size['width']
            bottom = location['y'] + size['height']
            imgages = page_snap_obj.crop((left, top, right, bottom))

            # 获取到验证码截图
            imgages.save("./images/xingye/xy_imcode.png")
            imgages.show()
            sleep(1)


            # 添加机器识别
            img_code = input("请输入图形验证码:")
            # self.browser.find_element_by_id('mobilecaptchafield')
            self.browser.find_element_by_id('mobilecaptchafield').send_keys(img_code)
            sleep(1)
        except Exception as e:
            print(e.args)

        finally:
            print("图形验证码ok")
        try:
            self.browser.find_element_by_id("btnSendSms").click()
            ver_code = input("请输入手机验证码:")
            self.browser.find_element_by_id("mobLogin_sendsms").send_keys(ver_code)
            sleep(3)
        except Exception  as e:
            print(e.args)
        finally:
            pass


        page_html = self.browser.page_source
        return page_html

    def process_request(self):
        login_method = input("登录方式(卡号/登录名/手机号):")
        # login_method = "卡号"
        if login_method == "卡号":
            t1 = time.time()
            page_html = self.card_num()
            t2 = time.time()
            t3 = t2-t1
            print("登录:{}".format(t3))

        elif login_method == "登录名":
            page_html = self.username()

        elif login_method =="手机号":
            page_html = self.phone_num()

        else:
            print("登录方式不对,请重新输入")
            self.process_request()

        sleep(4)
        #积分余额
        t4 = time.time()
        self.browser.find_element_by_id("FIN09").click()
        sleep(2)
        article1 = self.browser.find_element_by_id("FIN09_08")
        ActionChains(self.browser).move_to_element(article1).perform()
        sleep(3)
        article2 = self.browser.find_element_by_id("FIN09_08_03")
        ActionChains(self.browser).move_to_element(article2).perform()
        sleep(1)
        article3 = self.browser.find_element_by_id("FIN09_08_03_01").click()
        # ActionChains(self.browser).move_to_element(article3).perform()
        sleep(2)
        self.browser.switch_to.frame("workframe")


        page_html2 = self.browser.page_source
        #https://personalbank.cib.com.cn/pers/main/welcome.do

        # with open(r"E:\code\spiders\text\page_html12.txt", "w+",encoding="utf8") as fp:
        #     fp.write(page_html2)
        #     fp.close()
        # html = page_html2.decode('utf-8')
        html = page_html2

        htmls = etree.HTML(html)
        # print(type(htmls))

        divs = htmls.xpath(".//div[@id='main']")
        items=[]
        for div in divs:
            item={}
            print(div)
            # date = div.xpath(".//div[@class='ui-jqgrid-hbox']/table//th/div[@id='jqgh_pointDate']/text()")
            # 信用卡号
            card_num = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[1]/td/text()")[0].strip()

            # 客户名称
            name = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[2]/td/text()")[0].strip()

            # 累计总积分
            all_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[3]/td/text()")[0].strip()

            # 账户可兑换积分
            usable_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[4]/td/text()")[0].strip()

            # 本期已兑换积分
            used_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[5]/td/text()")[0].strip()

            # 本期新增积分
            add_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[6]/td/text()")[0].strip()

            # 本期调整积分
            c_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[7]/td/text()")[0].strip()
            # 积分是否冻结
            about_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[8]/td/text()")[0].strip()
            # 积分到期日
            expire_date = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[9]/td/text()")[0].strip()

            print("信用卡号:{}".format(card_num))
            print("客户名称:{}".format(name))
            print("账户累计总积分:{}".format(all_score))
            print("账户可兑换积分:{}".format(usable_score))
            print("本期已兑换积分:{}".format(used_score))
            print("本期新增积分:{}".format(add_score))
            print("本期调整积分:{}".format(c_score))
            print("积分是否冻结:{}".format(about_score))
            print("积分到期日期:{}".format(expire_date))
            item["card_num"] = card_num
            item["name"] = name
            item["all_score"] = all_score
            item["usable_score"] = usable_score
            item["used_score"] = used_score
            item["add_score"] = add_score
            item["c_score"] = c_score
            item["about_score"] = about_score
            item["expire_date"] = expire_date
            items.append(item)
        print(items)
        t5 = time.time()
        t6 = t5-t4
        print("积分余额{}".format(t6))


        # pattern = r'(<th>[\u4e00-\u9fa5]*：</th>)|(<td>((\d*)|([\u4e00-\u9fa5]*))</td>)|(^[0-9]{4}-[1-12]{1,2}-[1-31]{1,2}$)'
        # # pattern = r'<tr><td>(\d?)</td></tr>'
        #
        # slist = re.findall(pattern, html)
        # print(slist)
        # ['5240707969398113', '957397', '957397', '0', '0', '0']

        xlist = []



        # response = etree.HTML(page_html2)
        #
        # divs = response.xpath("")
        t7 = time.time()
        self.browser.switch_to.default_content()
        #积分明细
        sleep(1)
        article1 = self.browser.find_element_by_id("FIN09_08")
        ActionChains(self.browser).move_to_element(article1).perform()
        sleep(1)
        article2 = self.browser.find_element_by_id("FIN09_08_03")
        ActionChains(self.browser).move_to_element(article2).perform()
        sleep(1)
        article3 = self.browser.find_element_by_id("FIN09_08_03_02").click()


        # article3 = self.browser.find_element_by_id("form_6").click()
        # ActionChains(self.browser).move_to_element(article3).perform()
        sleep(2)
        # self.browser.switch_to.frame("workframe")

        sleep(0.2)
        # self.browser.find_element_by_class_name("ui-button-text").click()
        self.browser.find_element_by_xpath("//*[@id='mainframe']/div[8]/div[3]/div/button/span").click()

        sleep(0.2)

        self.browser.switch_to.frame("workframe")


        #自由选择查询时间
        # self.browser.find_element_by_class_name("ui-datepicker-trigger").click()
        # sleep(0.5)
        # self.browser.find_element_by_class_name("ui-datepicker-year").click()

        # print(20)
        #
        # sleep(0.5)
        # self.browser.find_element_by_link_text("2014").click()
        # print("2014")
        # sleep(0.5)
        # self.browser.find_element_by_class_name("ui-datepicker-month").click()
        # sleep(0.5)
        # self.browser.find_element_by_link_text("二").click()

        # self.browser.find_element_by_class_name("ui-state-default").click()
        # sleep(0.5)
        # article3 = self.browser.find_element_by_id("form_0").click()



        article3 = self.browser.find_element_by_id("form_6").click()
        sleep(3)


        page_html3 = self.browser.page_source
        # with open(r"E:\code\spiders\text\page_html03.txt","w+",encoding="utf8") as fp:
        #     fp.write(page_html3)
        #     fp.close()


        # print(page_html3)

        items = []
        # response = etree.HTML(page_html3)
        # html = page_html3
        print("ht3的格式:{}".format(type(page_html3)))

        htmls = etree.HTML(page_html3)

        divs = htmls.xpath(".//div[@class='ui-jqgrid-view']")

        for div in divs:
            print(div)
            # date = div.xpath(".//div[@class='ui-jqgrid-hbox']/table//th/div[@id='jqgh_pointDate']/text()")
            date = div.xpath(".//table[@id='detailList']//td[1]/text()")[0].strip()
            deal = div.xpath(".//table[@id='detailList']//td[2]/text()")[0].strip()
            amount = div.xpath(".//table[@id='detailList']//td[3]/text()")[0].strip()
            score_change = div.xpath(".//table[@id='detailList']//td[4]/text()")[0].strip()
            detail = div.xpath(".//table[@id='detailList']//td[5]/text()")[0].strip()
            # riqi = div.xpath(".//div[@class=['ui-jqgrid-hbox']/table/thead/tr/th/div[@id='jqgh_pointDate']/text()")
            print("日期:" + date)
            print("交易:" + deal)
            print("交易额:" + amount)
            print("积分变动:" + score_change)
            print("交易描述:" + detail)

        # pattern = r'<td>(\d*)</td>'
        # # pattern = r'<tr><td>(\d?)</td></tr>'
        #
        # slist = re.findall(pattern, html)
        # print(slist)
        t8 = time.time()
        t9 = t8-t7
        print("积分明细时间:{}".format(t9))

        #账单查询
        #账单日查询
        t10 = time.time()
        self.browser.switch_to.default_content()

        sleep(1)
        article4 = self.browser.find_element_by_id("FIN09_08")
        ActionChains(self.browser).move_to_element(article4).perform()
        sleep(1)
        article5 = self.browser.find_element_by_id("FIN09_08_02")
        ActionChains(self.browser).move_to_element(article5).perform()
        sleep(1)
        article6 = self.browser.find_element_by_id("FIN09_08_02_03").click()
        sleep(1)

        self.browser.switch_to.frame("workframe")
        trans_html = self.browser.page_source
        # with open(r"E:\code\spiders\text\trans_html.html", "w+", encoding="utf8") as fp:
        #     fp.write(trans_html)
        #     fp.close()

        trans_tree = etree.HTML(trans_html)

        divs = trans_tree.xpath(".//div[@id='main']")
        trans_items = []
        for div in divs:
            item = {}
            card_num = div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr/td/text()")[0].strip()
            user_name = div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr/td[2]/text()")[0].strip()
            trans_date = div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr[2]/td/text()")[0].strip()
            item["card_num"] = card_num
            item["user_name"] = user_name
            item["trans_date"] = trans_date

            trans_items.append(item)
            print("卡号是:{}".format(card_num))
            print("持卡人姓名:{}".format(user_name))
            print("账单日期为:{}".format(trans_date))
        print(trans_items)
        t11 = time.time()
        t12= t11-t10
        print("账单日查询时间{}".format(t12))


        t13 = time.time()
        #信用卡账户信息
        self.browser.switch_to.default_content()
        sleep(1)
        article4 = self.browser.find_element_by_id("FIN09_08")
        ActionChains(self.browser).move_to_element(article4).perform()
        sleep(1)
        article5 = self.browser.find_element_by_id("liFIN09_08_01").click()
        # ActionChains(self.browser).move_to_element(article5).perform()
        sleep(2)
        # article6 = self.browser.find_element_by_id("FIN09_08_02_03").click()
        # sleep(1)
        self.browser.switch_to.frame("workframe")


        xinxi_html = self.browser.page_source
        with open(r"E:\code\spiders\text\xinxi_html.html", "w+", encoding="utf8") as fp:
            fp.write(xinxi_html)
            fp.close()

        xinxi_tree = etree.HTML(xinxi_html)
        divs = xinxi_tree.xpath(".//div[@id='page_content']")
        for div in divs:
            card_xinxi = div.xpath(".//div[@class='info-show']/span/text()")

            card_num = card_xinxi[1].strip()
            user_name = card_xinxi[3].strip()
            card_leixing = card_xinxi[5].strip()
            print(card_num)
            print(user_name)
            print(card_leixing)

        for div in divs:
            zhanghu_xinxi = div.xpath(".//table/tbody//text()")

            for i in range(300):
                try:
                    item = zhanghu_xinxi[i].strip()
                    print(item)
                except:
                    pass

        #存款余额查询
        sleep(1)
        self.browser.switch_to.default_content()
        self.browser.find_element_by_xpath("//div[@id='wrap']/div[@id='nav']//li[@id='liFIN01']/a[@id='FIN01']").click()
        sleep(1)
        self.browser.find_element_by_id("FIN01_01").click()
        sleep(1)
        self.browser.switch_to.frame("workframe")
        sleep(0.2)
        for i in range(1,10):
            try:
                self.browser.find_element_by_id("jqg_accountList_{}".format(i)).click()
                sleep(0.2)
            except:
                print("一共{}张信用卡".format(i))
        self.browser.find_element_by_id("form__batchQueryBalance").click()
        sleep(2)

        # self.browser.switch_to.frame("workframe")
        #存款余额
        deposits_html = self.browser.page_source
        # with open(r"E:\code\spiders\text\deposits_html.html", "w+", encoding="utf8") as fp:
        #     fp.write(deposits_html)
        #     fp.close()

        deposits_tree = etree.HTML(deposits_html)

        divs = deposits_tree.xpath(".//div[@id='page_margin']//div[@id='page_content']")

        for div in divs:
            zhanghu_items = []
            for i in range(1, 20):
                try:
                    item = {}
                    # 账户信息
                    zhanghu_xinxi = div.xpath("./form[@id='form']/div[@class='info-show'][{}]/span/text()".format(i))
                    # print(type(zhanghu_xinxi))
                    zhanghu_leixing = zhanghu_xinxi[0]
                    # print(zhanghu_leixing)
                    zhanghu_huming = zhanghu_xinxi[1]
                    # print(zhanghu_huming)
                    zhanghu_nums = zhanghu_xinxi[2]
                    zhanghu_zhuangtai = zhanghu_xinxi[3]
                    item["账户类型"] = zhanghu_leixing
                    item["账户户名"] = zhanghu_huming
                    item["账号"] = zhanghu_nums
                    item["账户状态"] = zhanghu_zhuangtai
                    zhanghu_items.append(item)

                    # 存款信息
                    cunkuan_xinxi = div.xpath("./form[@id='form']/table[{}]//tr/td/text()".format(i))
                    items = []
                    for j in range(0, 10):
                        try:
                            strs = {}
                            # str = cunkuan_xinxi[i].strip()
                            xuhao = cunkuan_xinxi[0 + 11 * j].strip()
                            chuzhong = cunkuan_xinxi[1 + 11 * j].strip()
                            bizhong = cunkuan_xinxi[2 + 11 * j].strip()
                            chaohui = cunkuan_xinxi[3 + 11 * j].strip()
                            yu_e = cunkuan_xinxi[4 + 11 * j].strip()
                            keyong_yue = cunkuan_xinxi[5 + 11 * j].strip()
                            kaihuriqi = cunkuan_xinxi[6 + 11 * j].strip()
                            cunqi = cunkuan_xinxi[7 + 11 * j].strip()
                            daoqiriqi = cunkuan_xinxi[8 + 11 * j].strip()
                            xucuncunqi = cunkuan_xinxi[9 + 11 * j].strip()
                            zhuangtai = cunkuan_xinxi[10 + 11 * j].strip()
                            # caozuo= cunkuan_xinxi[11+11*i].strip()

                            strs["序号"] = xuhao
                            strs["储种"] = chuzhong
                            strs["币种"] = bizhong
                            strs["钞汇"] = chaohui
                            strs["余额"] = yu_e
                            strs["可用余额"] = keyong_yue
                            strs["开户日期"] = kaihuriqi
                            strs["存期"] = cunqi
                            strs["到期日期"] = daoqiriqi
                            strs["续存存期"] = xucuncunqi
                            strs["状态"] = zhuangtai
                            # strs["操作"] =caozuo
                            # print(strs)
                            items.append(strs)
                        except:
                            pass

                    card_num = item["账号"]
                    print(card_num)
                    ss = Mysql_input()
                    ss.set_data2(i,items,card_num)

                    # ss = Mysql_input()
                    # t2 = Thread(target=ss.set_data2, args=(i,items,card_num))
                    # print("启动线程2")
                    # t2.start()
                    print("卡{}余额信息:{}".format(i, items))

                except:
                    # print("没找到")
                    pass
        print("账户信息:{}".format(zhanghu_items))

        t14 = time.time()
        t15 = t14 - t13
        print("余额及账户信息查询:{}".format(t15))






#数据库连接
class Mysql_input(object):
    def __init__(self,host="47.97.217.36",user = "root",password="root",database="user",port = 3306,charset="utf8"):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.port = port
        self.charset = charset


    def connect(self):
        self.conn = pymysql.connect(host = self.host,user = self.user,password = self.password,database = self.database,port = self.port,charset = self.charset)
        self.cursor = self.conn.cursor()

    def set_data(self,my_integral="900",bill="12月消费100积分"):
        self.connect()
        try:
            # sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
            sql_1 = "INSERT INTO card_score VALUES(null,'{}','{}');".format(my_integral,bill)
            self.cursor.execute(sql_1)
            self.conn.commit()
            print("成功添加至数据库!")
            res = self.cursor.fetchall()
            if res != None:
                self.close()
                return res
        except:
            self.conn.rollback()


    def set_data2(self,i,items,card_num):
        self.connect()
        for sa in range(10):
            try:
                my_item = items[sa]
                xuhao=my_item["序号"]
                chuzhong = my_item["储种"]
                bizhong= my_item["币种"]
                chaohui= my_item["钞汇"]
                yu_e= my_item["余额"]
                keyong_yue= my_item["可用余额"]
                kaihuriqi= my_item["开户日期"]
                cunqi= my_item["存期"]

                daoqiriqi= my_item["到期日期"]
                xucuncunqi= my_item["续存存期"]
                zhuangtai= my_item["状态"]
                print(my_item)
                print(yu_e)
                # print(zhuangtai)

                print("连接数据库")
                try:
                    # sql_1 = "INSERT INTO balance_info VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}',null,'{}',null,null});".format(card_num,xuhao,chuzhong,bizhong,chaohui,yu_e,keyong_yue,kaihuriqi,daoqiriqi)
                    sql_1 = "INSERT INTO balance_info VALUES(null,'{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}','{}');".format(card_num,xuhao,chuzhong,bizhong,chaohui,yu_e,keyong_yue,kaihuriqi,cunqi,daoqiriqi,xucuncunqi,zhuangtai)
                    self.cursor.execute(sql_1)
                    self.conn.commit()
                    print("{}卡的余额信息成功添加至数据库!".format(i))
                    res = self.cursor.fetchall()
                    # if res != None:
                    #     self.close()
                    #     return res
                except:
                    self.conn.rollback()
            except:
                pass


    def close(self):
        self.cursor.close()
        self.conn.close()



if __name__ == '__main__':
    t1 = time.clock()
    zx = Xingye_C()
    zx.process_request()
    t2 = time.clock()
    t3 = round(t2,2)
    print("本次数据获取耗时:{}s".format(t3))
    #50s左右

