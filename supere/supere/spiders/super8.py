# -*- coding: utf-8 -*-
import scrapy


# class Super8Spider(scrapy.Spider):
#     name = 'super8'
#     allowed_domains = ['super8.com.cn']
#     start_urls = ['http://super8.com.cn/']
#
#     def parse(self, response):
#         pass




from scrapy import Spider, Request
from selenium import webdriver


class MySpider(Spider):
    name = "super8"

    def __init__(self):
        self.browser = webdriver.Chrome()
        self.browser.set_page_load_timeout(30)

    def closed(self, spider):
        print("爬虫关闭")
        self.browser.close()

    def start_requests(self):
        start_urls = ['http://club.haval.com.cn/forum.php?mod=toutiao&mobile=2'.format(str(i)) for i in range(1, 2, 2)]
        for url in start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, response):
        domain = response.url.split("/")[-2]
        filename = '{}.html'.format(domain)
        with open(filename, 'wb') as f:
            f.write(response.body)
        print('------------------------over---------------------------')
