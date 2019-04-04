
import os
from lxml import etree
from time import sleep


with open(r'E:\code\spiders\text\pinan_home_html2.txt', 'r', encoding="utf-8") as f:
    html = f.read()

html_tree = etree.HTML(html)
# divs1 = html_tree.xpath(".//div[@id='context']//div[@id='nav']/ul[@id='nav_child'][1]//ul[@class='nav_ul_li02']/li[1]/a[1]/text()")
divs1 = html_tree.xpath("//ul[@id='nav_child']/li[4]/ul[@class='nav_ul_li02']/li[1]/a[1]/text()")
# divs1 = html_tree.xpath('//*[@id="liChild"]/li[1]/a/text()')

print(divs1)


divs = html_tree.xpath(".//div[@id='context']")
items = []
for div in divs:
    item = {}
    # username = div.xpath(".//div[@class='pa_name']")
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
    minimum_return =div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[2]/td[2]/span/text()")[0].strip()
    # #本期剩余应还
    remainder = div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[3]/td[2]/text()")[0].strip()
    # #本期剩余最低应还额
    remainder_minimum_return = div.xpath(".//div[contains(@class,'pa_con02_ltext')]/table/tbody/tr[4]/td[2]/text()")[0].strip()

    # print("用户名:{}".format(username))
    # print("可用额度:{}".format(able_credit))
    # print("信用额度:{}".format(credits))
    # print("本期账单日:{}".format(current_billing_data))
    # print("本期还款日{}".format(current_repayment_date))
    # print("本期应还额:{}".format(new_balance))
    # print("本期最低应还:{}".format(minimum_return))
    # print("本期剩余应还:{}".format(remainder))
    # print("本期剩余最低应还额:{}".format(remainder_minimum_return))


with open(r'E:\code\spiders\text\pingan_bank\score_html.txt', 'r', encoding="utf-8") as f:
    html = f.read()

html_tree2 = etree.HTML(html)


# html_tree2 = etree.HTML(page_html2)
print(html_tree2)
divs = html_tree2.xpath(".//div[@class='right_box']")

# for div in divs:
    #截止目前万里通积分总数
    # all_score = div.xpath(".//div[@id='id_qwpdZ']/div/p/text()")[0].strip()
    # # 本期余额
    # benqi_yue = div.xpath(".//div[@id='id_qwpdL']//tr/td[2]/text()")[0].strip()
    # #本期新增
    # benqi_xinzeng = div.xpath(".//div[@id='id_qwpdL']//tr/td[4]/text()")[0].strip()
    # # 本期调整
    # benqi_tiaozheng= div.xpath(".//div[@id='id_qwpdL']//tr[2]/td[4]/text()")[0].strip()
    # #即将失效
    # about_to_fail = div.xpath(".//div[@id='id_qwpdL']//tr[2]/td[4]/text()")[0].strip()

    # print("目前万里通积分总数:{}".format(all_score))
    # print("本期余额:{}".format(benqi_yue))
    # print("本期新增:{}".format(benqi_xinzeng))
    # print("本期调整:{}".format(benqi_tiaozheng))
    # print("即将失效积分数:{}".format(about_to_fail))




with open(r'E:\code\spiders\text\pingan_bank\score_html.txt', 'r', encoding="utf-8") as f:
    html = f.read()


html_tree3 = etree.HTML(html)


divs = html_tree3.xpath("//div[@class='right_box']")

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

    #没有记录
    no_record = div.xpath('//*[@id="jfForm"]/div[2]/div[2]/p/text()')[0].strip()

    # print(':{}'.format(trans_date))
    # print(':{}'.format())
    # print(':{}'.format())
    # print(':{}'.format())
    # print(':{}'.format())
    # print(':{}'.format())
    print('你好:{}'.format(no_record))
#
#
