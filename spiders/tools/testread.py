
import re
from lxml import etree

with open(r'E:\code\spiders\text\page_html12.txt' ,'r',encoding="utf-8") as f:
    html = f.read()


htmls = etree.HTML(html)
print(type(htmls))

divs = htmls.xpath(".//div[@id='main']")

for div in divs:
    print(div)
    # date = div.xpath(".//div[@class='ui-jqgrid-hbox']/table//th/div[@id='jqgh_pointDate']/text()")
    #信用卡号
    card_num = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[1]/td/text()")[0].strip()

    #客户名称
    name = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[2]/td/text()")[0].strip()

    #累计总积分
    all_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[3]/td/text()")[0].strip()

    #账户可兑换积分
    usable_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[4]/td/text()")[0].strip()

    #本期已兑换积分
    used_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[5]/td/text()")[0].strip()

    #本期新增积分
    add_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[6]/td/text()")[0].strip()

    #本期调整积分
    c_score= div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[7]/td/text()")[0].strip()
    #积分是否冻结
    about_score = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[8]/td/text()")[0].strip()
    # 积分到期日
    expire_date = div.xpath(".//div[@id='page_content']//table[@id='bonusTbl']//tr[9]/td/text()")[0].strip()

    # print("信用卡号:{}".format(card_num))
    # print("客户名称:{}".format(name))
    # print("账户累计总积分:{}".format(all_score))
    # print("账户可兑换积分:{}".format(usable_score))
    # print("本期已兑换积分:{}".format(used_score))
    # print("本期新增积分:{}".format(add_score))
    # print("本期调整积分:{}".format(c_score))
    # print("积分是否冻结:{}".format(about_score))
    # print("积分到期日期:{}".format(expire_date))

# print(html)

# pattern = r'<th>[\S]*</th>(. | \n)*?<td>(\d*)</td>'
# pattern = r'<\s*(td)(\s[^>]*)?>[\S]*</th>(. | \n)*?<td>(\d*)</td>'
# pattern = r'^<th>[\u4e00-\u9fa5]*：</th>(. | \n)*?<td>(\d*)</td>'
# pattern = r'<th>[\u4e00-\u9fa5]*：</th>'
# pattern = r'([\u4e00-\u9fa5]*：)|(<td>(\d*)?</td>)'
# pattern = r'(<th>[\u4e00-\u9fa5]*：</th>)|(<td>((\d*)|([\u4e00-\u9fa5]*))</td>)|(^[0-9]{4}-[1-12]{1,2}-[1-31]{1,2}$)'
# pattern = r'<td>(\d*)?</td>'
# pattern = r'<(S*?)[^>]*>.*?|<.*?/> '
# pattern = r'<[^>]*>'
# pattern = r'[\u4e00-\u9fa5]*'

# pattern = r'<th>(.*)</th>(.*)<td>(\d*)</td>'

# slist = re.findall(pattern,html,re.S)
# print(slist)






#交易信息
with open(r'E:\code\spiders\text\page_html03.txt' ,'r',encoding="utf-8") as f:
    html = f.read()
# print(html)

# pattern = r'(. | \n)*?>(\d*)</td>'
# pattern = r'>[\u4e00-\u9fa5]*<span | >(\d*)</td>'
# pattern = r'<\s*(\S+)(\s[^>]*)?>[\s\S]*<\s*\/\1\s*>'
# pattern = r'<\s*(td)(\s[^>]*)?>[\S]*</td>'
# pattern = r'<\s*(td)(\s[^>]*)?>[\u4e00-\u9fa5]*</td>'
# pattern = r'<th>[\u4e00-\u9fa5]*：</th>(.*)<td>(\d*)</td>'
# pattern = r'[\u4e00-\u9fa5]*'

# pattern = r'((\d*))|(-(\d*))'
# pattern = r'<div\sclass="ui-jqgrid(.*)</div>'
# pattern = r'<(S*?)[^>]*>.*?|<.*? /> '
# slist = re.findall(pattern,html,re.S)
# print(slist)
# pattern = r'[\u4e00-\u9fa5]*：.*<td>(\d*)</td>'
# ss = "<tr> \n <th>账户可兑换积分：</th>  \n <td>957397</td>  	</tr>"
# ress = re.findall(pattern,ss,re.S)
# print(ress)
# print(type(html))
htmls = etree.HTML(html)
# print(type(htmls))

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
    # print("日期:"+date)
    # print("交易:"+deal)
    # print("交易额:"+amount)
    # print("积分变动:"+score_change)
    # print("交易描述:"+detail)




#账单日
with open(r'E:\code\spiders\text\trans_html.txt', 'r', encoding="utf-8") as f:
    html = f.read()

trans_tree = etree.HTML(html)
divs = trans_tree.xpath(".//div[@id='main']")
trans_items = []
for div in divs:
    item = {}
    card_num = div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr/td/text()")[0].strip()
    user_name =div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr/td[2]/text()")[0].strip()
    trans_date = div.xpath(".//div[@id='col3']//div[@id='page_margin']//table[@class='table-v']/tbody/tr[2]/td/text()")[0].strip()
    item["card_num"] = card_num
    item["user_name"] = user_name
    item["trans_date"] = trans_date

#     trans_items.append(item)
# #     print("卡号是:{}".format(card_num))
# #     print("持卡人姓名:{}".format(user_name))
# #     print("账单日期为:{}".format(trans_date))
# # print(trans_items)

with open(r'E:\code\spiders\text\deposits_html.txt',"r", encoding="utf-8") as f:
    html = f.read()

deposits_tree = etree.HTML(html)

divs = deposits_tree.xpath(".//div[@id='page_margin']//div[@id='page_content']")

for div in divs:
    zhanghu_items=[]
    for i in range(1,20):
        try:
            item={}
            #账户信息
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
            item["账户状态"] =  zhanghu_zhuangtai
            zhanghu_items.append(item)


            #存款信息
            cunkuan_xinxi = div.xpath("./form[@id='form']/table[{}]//tr/td/text()".format(i))
            items=[]
            for j in range(0,10):
                try:
                    strs = {}
                    # str = cunkuan_xinxi[i].strip()
                    xuhao = cunkuan_xinxi[0+11*j].strip()
                    chuzhong = cunkuan_xinxi[1+11*j].strip()
                    bizhong= cunkuan_xinxi[2+11*j].strip()
                    chaohui= cunkuan_xinxi[3+11*j].strip()
                    yu_e= cunkuan_xinxi[4+11*j].strip()
                    keyong_yue= cunkuan_xinxi[5+11*j].strip()
                    kaihuriqi= cunkuan_xinxi[6+11*j].strip()
                    cunqi= cunkuan_xinxi[7+11*j].strip()
                    daoqiriqi= cunkuan_xinxi[8+11*j].strip()
                    xucuncunqi= cunkuan_xinxi[9+11*j].strip()
                    zhuangtai= cunkuan_xinxi[10+11*j].strip()
                    # caozuo= cunkuan_xinxi[11+11*i].strip()

                    strs["序号"] = xuhao
                    strs["储种"] = chuzhong
                    strs["币种"] =bizhong
                    strs["钞汇"] =chaohui
                    strs["余额"] =yu_e
                    strs["可用余额"] =keyong_yue
                    strs["开户日期"] =kaihuriqi
                    strs["存期"] =cunqi
                    strs["到期日期"] =daoqiriqi
                    strs["续存存期"] =xucuncunqi
                    strs["状态"] =zhuangtai
                    # strs["操作"] =caozuo
                    # print(strs)
                    items.append(strs)
                except:
                    pass
            print("卡{}余额信息:{}".format(i, items))

            # print(items)
            # print(cunkuan_xinxi)
        except:
            # print("没找到")
            pass
print("账户信息:{}".format(zhanghu_items))


# for div in divs:
#     bizhong = div.xpath(".//tbody//td/text()").strip()
#
#
#     print(bizhong)


with open(r'E:\code\spiders\text\xinxi_html.txt',"r", encoding="utf-8") as f:
    html = f.read()

xinxi_tree = etree.HTML(html)

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
            # print(item)
        except:
            pass

    # print(zhanghu_xinxi)
