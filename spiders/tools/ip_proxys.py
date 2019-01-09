
import re
import lxml
import socket
import selenium
import urllib3
import requests
import urllib.request

from lxml import etree
from time import sleep

class Xici_proxys():
    pass

def get_proxy(page):
    url = 'https://www.xicidaili.com/wn/{}'.format(page)
    header = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }
    req = urllib.request.Request(url=url,headers=header)
    response = urllib.request.urlopen(req)
    html = response.read()
    # print(html)


    #xpath 解析
    # sel = input("输入匹配规则(1/2):")
    sel = "1"
    if sel =="1":
        html = html.decode('utf-8')
        pattern = r'<td>(\d+\.\d+\.\d+\.\d+)</td>(.|\n)*?<td>(\d+)</td>'
        # pattern = r'<td>(\d+\.\d+\.\d+\.\d+)</td>(.|\n)*?<td>(\d+)</td>(.|\n)*?<td>HTTPS</td>'
        srclist = re.findall(pattern,html)
        print(srclist)
        xlist = []
        for item in srclist:
            print(item)
            # xlist.append((item[3], item[1], item[3]))
            xlist.append((item[2], item[0]))
        print(xlist[1][0])
        # print(xlist)

    else:
        mytree = etree.HTML(html)
        print(mytree)
        divs = mytree.xpath(".//div[@id='wrapper']/div[@id='body']/table[@id='ip_list']")
        items = []
        print(divs)
        for div in divs:
            print(div)
            item = {}
            ips =div.xpath(".//tbody/tr/td[2][1]/text()")
            ports =div.xpath("./tbody/tr/td[3]/text()")
            print(ips)
            print(ports)
            item["ips"] = ips
            item["ports"] = ports
            print(item)
            items.append(item)
        print(items)
        xlist = items

    sleep(4)
    return xlist

def test_proxy(item):
    # proxy = urllib.request.ProxyHandler({'https':"{}:{}".format(item[0],item[1])})
    # opener = urllib.request.build_opener(proxy)
    # s =socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        # testUrl = 'http://httpbin.org/ip'
        # testUrl = 'http://2017.ip138.com/ic.asp'
        # req = urllib.request.Request(testUrl)
        # res  = urllib.request.urlopen(req,timeout=2).read()

        ports = item[0]
        print(ports)
        ips = item[1]
        print(ips)
        # s.connect(ips,int(ports))
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        requests.get('https://www.baidu.com/',headers=headers, proxies={"https": "https://{}:{}".format(ips,ports)})

        print("****该ip可用:{}-----".format(item))

        with open(r"E:\code\spiders\text\proxy.txt","a") as f:
            f.write("{}:{}\n".format(item[0],item[1]))
            f.close()
    except Exception as e:
        print("{}:{}是废弃ip,{}".format(item[0],item[1],e))
    sleep(1)


def start():

    # get_proxy(1)
    for page in range(2,10):
        xlist = get_proxy(page)
        for item in xlist:
            test_proxy(item)






if __name__ == '__main__':
    Xici_proxys()
    start()