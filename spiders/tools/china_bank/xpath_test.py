import os
from lxml import etree
from time import sleep


with open(r"E:\code\spiders\text\china_bank\score_html.txt",'r',encoding="utf-8") as fp:
    score_html = fp.read()


score_etree = etree.HTML(score_html)

divs = score_etree.xpath(".//div[@id='user_content']")
for div in divs:
    all_score = div.xpath('./div[@class="user_info"]/dl//span[1]/text()')[0].strip()
    # able_score =div.xpath('./div[@class="user_info"]/dl//span[1]/text()')[1].strip()
    able_score =div.xpath('./div[@class="user_info"]/dl//span/text()')

    print("全部积分:{}".format(all_score))
    print("当前可用积分:{}".format(able_score))


for i in range(20):
    print(i)
    while True:
        sleep(0.1)
        print("获取数据")
        # if i ==0:
        #     print("15")
        break

