# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

import requests
import json
import threading
import queue
import random

from lxml import etree
from time import sleep
from threading import Lock
from urllib.error import URLError

# 创建两个队列
#爬虫
spider_queue = queue.Queue()

#解析
parse_queue = queue.Queue()

#设置解析线程的退出标志
parse_exit_flag = False

#基础url
base_url = "https://www.qiushibaike.com/8hr/page/{}/"

#文件操作锁
lock = threading.Lock()

#请求头构建
UserAgent_list = [
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.4; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2225.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2224.3 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 4.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2049.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1985.67 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.3319.102 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2309.372 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.2117.157 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1866.237 Safari/537.36",
]

class SpiderThread(threading.Thread):
    def __init__(self,id,s_queue,p_queue,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.id = id
        self.spider_queue = s_queue
        self.parse_queue = p_queue

    def run(self):
        print("{}线程开始执行".format(self.id))
        #循环爬取数据
        while True:
            #数据为空时,终止
            if self.spider_queue.empty():
                break
            #取数据
            page = self.spider_queue.get()

            #url
            url = base_url.format(page)
            print(url)

            #尝试次数
            times = 3
            while times > 0:
                try:
                    response = requests.get(url=url,headers={'Usesr-Agent':random.choice(UserAgent_list)})
                    #数据加入解析队列
                    self.parse_queue.put(response.text)
                    # print(response.text)
                    sleep(1)
                    print("{}线程取出了第{}页数据".format(self.id,page))

                    #通知队列数据已取出
                    self.spider_queue.task_done()
                    #成功,退出
                    break
                except URLError as e:
                    print("网络错误")
                finally:
                    times -= 1

class ParseThread(threading.Thread):
    def __init__(self,id,p_queue,fp,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.id = id
        self.parse_queue = p_queue
        self.fp = fp

    def run(self):
        global parse_exit_flag
        #循环取数据
        while True:
            #解析退出标志为True时,退出
            if parse_exit_flag:
                break
            try:
                # 从解析队列中取数据, 注意设置成False
                data = self.parse_queue.get(block=False)
                # print(data)
                #解析数据,封装成一个函数
                self.parse(data)
                print("{}线程解析数据成功".format(self.id))
                #告诉队列取完了数据
                self.parse_queue.task_done()
            except Exception as e:
                # print(e,"解析错误")
                pass


    def parse(self,data):
        global parse_num
        # 数据保存到一个文件中。
        # 先解析数据
        # 创建etree对象
        html = etree.HTML(data)
        # 找出页面上所有的段子div
        div_list = html.xpath('//li[contains(@id,"qiushi_tag_")]')
        # 对div_list中的每一个div进行数据解析
        results = []
        for div in div_list:
            # 头像的url
            head_shot = div.xpath('.//img/@src')[0]
            # 作者名字
            name = div.xpath('.//span[@class="recmd-name"]')[0].text
            # 内容
            content = div.xpath('.//a[@class="recmd-content"]')[0].text.strip('\n')
            # 保存到一个字典中
            item = {
                'head_shot': head_shot,
                'name': name,
                'content': content
            }
            results.append(item)
            # 保存到文件中，并且加锁
        json_result = {
            'msg': 'ok',
            'status': 200,
            'data': results
        }
        with lock:
            self.fp.write(json.dumps(results, ensure_ascii=False) + '\n')

def main():
    print('--------------任务开始-----------------')
    # 假设爬10页数据。往爬虫队列中写入10个数
    for page in range(1, 11):
        spider_queue.put(page)

    # 1. 创建爬虫进程，并启动
    # 创建3个爬虫线程
    for i in range(3):
        SpiderThread(i, spider_queue, parse_queue).start()

    # 2. 创建解析进程并启动。
    # 创建3个解析线程，并保存解析的内容
    # 数据保存到一个文件中
    fp = open('./qiu.txt', 'w', encoding='utf-8')
    for i in range(3):
        ParseThread(i, parse_queue, fp).start()

    # 3. 队列锁，保证任务执行结束。
    spider_queue.join()
    parse_queue.join()

    # 4. 设置关闭退出标志。
    global parse_exit_flag
    parse_exit_flag = True

    # 关闭文件
    fp.close()

    print('--------------任务完成---------------')

if __name__ == '__main__':
    main()