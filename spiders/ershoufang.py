
from lxml import etree
from requests.packages import urllib3
from collections import OrderedDict
from time import sleep


import re
import json
import urllib
import requests
import urllib.request

class Ershoufang():
    def __init__(self,num):
        self.url = "https://sz.lianjia.com/ershoufang/pg{}/".format(num)
        self.headers={
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }


    def parses(self):
        page_html = requests.get(self.url,headers=self.headers)
        print(page_html.text)
        response = etree.HTML(page_html.text)
        print(type(response))

        fangs = response.xpath(".//div[@class='content']/div[@class='leftContent']/ul[@class='sellListContent']")
        # fangs = page_html.xpath(".//div[@class='content']/div[@class='leftContent']")
        print(fangs)
        items =[]
        for fang in fangs:
            item={}
            title = fang.xpath(".//div[@class='title']").strip()
            print(title)

            item["title"] = title
            items.append(item)
            # print(item)
        print(items)
        sleep(3)




if __name__ == '__main__':
    for num in range(100):
        req = Ershoufang(num)
        req.parses()
