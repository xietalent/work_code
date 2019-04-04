
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

    # print("信用额度为:{}人民币,即{}美元".format(xinyong_edu_rmb,xinyong_edu_doller))
    # print("可用额度:{}元人民币,{}美元".format(keyong_edu_rmb,keyong_edu_doller))
    # print("未出账分期本金:{}".format(wcz_principal))
    # print("预借现金额度:{}人民币,{}美元".format(yjxianjin_rmb,yjxianjin_doller))
    # print("账单日:{}".format(billing_day))
    # print("账单类型:{}".format(billing_type))
    # print("账务提醒时间:{}".format(remind_date))

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

    #
    # print("----------------------------------------------")
    # print("本期到期还款日:{}".format(bq_repayment_date))
    # print("本期账单金额:{}rmb".format(bq_bill_amount_r))
    # print("本期账单金额:{}美元".format(bq_bill_amount_d))
    # print("本期剩余应还:{}人民币,{}美元".format(bq_yinghuan_amount_r,bq_yinghuan_amount_d))
    # print("本期剩余最低还款金额:{}人民币,{}美元".format(bq_less_amount_r,bq_less_amount_d))
    # print("{}".format())



with open(r'E:\code\spiders\text\zhaohang\billed_html.txt', 'r', encoding="utf-8") as f:
    billed_html = f.read()

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

    #依次为:账单月份,人民币应还总额,人民币最低还款额,美元应还总额,美元最低还款额
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date1[0],date1[1],date1[2],date1[3],date1[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date2[0],date2[1],date2[2],date2[3],date2[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date3[0],date3[1],date3[2],date3[3],date3[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date4[0],date4[1],date4[2],date4[3],date4[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date5[0],date5[1],date5[2],date5[3],date5[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date6[0],date6[1],date6[2],date6[3],date6[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date7[0],date7[1],date7[2],date7[3],date7[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date8[0], date8[1], date8[2], date8[3], date8[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date9[0],date9[1],date9[2],date9[3],date9[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date10[0],date10[1],date10[2],date10[3],date10[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date11[0],date11[1],date11[2],date11[3],date11[4]))
    print("{}期账单为:人民币应还总额:{},人民币最低还款额:{},美元应还总额:{},美元最低还款额:{}".format(date12[0],date12[1],date12[2],date12[3],date12[4].strip('$')))

    print("{}期账单为:{}".format(date1[0],date1))
    print("{}期账单为:{}".format(date2[0],date2))
    print("{}期账单为:{}".format(date3[0],date3))
    print("{}期账单为:{}".format(date4[0],date4))
    print("{}期账单为:{}".format(date5[0],date5))
    print("{}期账单为:{}".format(date6[0],date6))
    print("{}期账单为:{}".format(date7[0],date7))
    print("{}期账单为:{}".format(date8[0],date8))
    print("{}期账单为:{}".format(date9[0],date9))
    print("{}期账单为:{}".format(date10[0],date10))
    print("{}期账单为:{}".format(date11[0],date11))
    print("{}期账单为:{}".format(date12[0],date12))


# with open(r'E:\code\spiders\text\zhaohang\test22.txt', 'r', encoding="utf-8") as f:
#     unbilled_html = f.read()
#
# unbilled_tree= etree.HTML(unbilled_html)
#
# divs = unbilled_tree.xpath(".//div[@class='page-panel-content']")
#
# for div in divs:
#     try:
#         res1 = div.xpath("")
#
#     except:
#         print("未查询到您当前未出账单交易记录。")

print("{}先生/女士,您过去一年已出账单为:".format("陈慧聪"))


