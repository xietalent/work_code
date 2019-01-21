
from lxml import etree
from time import sleep

import os

with open(r'E:\code\spiders\text\zhaohang\zhaohang_homepage.txt', 'r', encoding="utf-8") as f:
    html = f.read()

homepage_tree = etree.HTML(html)


divs = homepage_tree.xpath(".//div[@class='page-panel']")

zhanghu_items = []
#账户信息
for  div in divs:
    zhanghu_item = {}
    xinyong_edu_rmb = div.xpath(".//table/tbody/tr[@id='trxyed']//span[@id='RMBXYED']/text()")[0].strip()
    xinyong_edu_doller = div.xpath(".//table/tbody/tr[@id='trxyed']//span[@id='USXYED']/text()")[0].strip()
    keyong_edu_rmb = div.xpath(".//table/tbody/tr[@id='trkyed']//span[@id='RMBKYED']/text()")[0].strip()
    keyong_edu_doller=  div.xpath(".//table/tbody/tr[@id='trkyed']//span[@id='USKYED']/text()")[0].strip()
    #未出账本金
    wcz_principal=  div.xpath(".//table/tbody/tr[@id='trwczfq']//span[@id='RMBWCZFQ']/text()")[0].strip()
    #预借现金可借额度
    yjxianjin_rmb = div.xpath(".//table/tbody/tr[@id='tryjxj']//span[@id='RMBYJXJ']/text()")[0].strip()
    yjxianjin_doller = div.xpath(".//table/tbody/tr[@id='tryjxj']//span[@id='RMBYJXJ']/text()")[0].strip()

    #账单日
    billing_day=  div.xpath(".//table/tbody/tr[@id='myzdr']//span[@id='MYZD']/text()")[0].strip()

    #账单类型
    billing_type =div.xpath(".//table/tbody/tr//span[@id='ZDLX']/text()")[0].strip()
    #账务提醒时间
    remind_date =div.xpath(".//table/tbody/tr[@id='trzwtxsj']//span[@id='ZWTXSJ']/text()")[0].strip()
    # xinyong_edu = div.xpath("")[0].strip()

    print("信用额度为:{}人民币,即{}美元".format(xinyong_edu_rmb,xinyong_edu_doller))
    print("可用额度:{}元人民币,{}美元".format(keyong_edu_rmb,keyong_edu_doller))
    print("未出账分期本金:{}".format(wcz_principal))
    print("预借现金额度:{}人民币,{}美元".format(yjxianjin_rmb,yjxianjin_doller))
    print("账单日:{}".format(billing_day))
    print("账单类型:{}".format(billing_type))
    print("账务提醒时间:{}".format(remind_date))

    # print(":{}".format())
divs = homepage_tree.xpath(".//div[@class='page-panel']//div[@class='page-panel-content']")
huankuan_items = []
for  div in divs:
    huankuan_item = {}
    bq_repayment_date = div.xpath("//tr[@id='trDQHQ']//span[@id='DQHQ']/text()")[0].strip()

    #本期账单金额
    bq_bill_amount_r = div.xpath("//tr[@id='trLiterRMBZDJE']//span[@id='LiterRMBZDJE']/text()")[0].strip()
    bq_bill_amount_d = div.xpath("//tr[@id='trLiterRMBZDJE']//span[@id='LiterUSBZDJE']/text()")[0].strip()
    #本期剩余应还
    bq_yinghuan_amount_r= div.xpath("//tr[@id='trLiterRMBBQJE']//span[@id='LiterRMBBQJE']/text()")[0].strip()
    bq_yinghuan_amount_d = div.xpath("//tr[@id='trLiterRMBBQJE']//span[@id='LiterUSBQJE']/text()")[0].strip()
    #本期剩余最低还款金额
    bq_less_amount_r = div.xpath("//tr[@id='trzdje']//span[@id='RMBZDJE']/text()")[0].strip()
    bq_less_amount_d = div.xpath("//tr[@id='trzdje']//span[@id='USZDJE']/text()")[0].strip()


    print("----------------------------------------------")
    print("本期到期还款日:{}".format(bq_repayment_date))
    print("本期账单金额:{}rmb".format(bq_bill_amount_r))
    print("本期账单金额:{}美元".format(bq_bill_amount_d))
    print("本期剩余应还:{}人民币,{}美元".format(bq_yinghuan_amount_r,bq_yinghuan_amount_d))
    print("本期剩余最低还款金额:{}人民币,{}美元".format(bq_less_amount_r,bq_less_amount_d))
    # print("{}".format())




with open(r'E:\code\spiders\text\zhaohang\billed_html.txt', 'r', encoding="utf-8") as f:
    billed_html = f.read()

billed_tree = etree.HTML(billed_html)

divs = billed_tree.xpath("")

for div in divs:

    pass


