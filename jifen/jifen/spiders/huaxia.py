# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request, Spider
from selenium import webdriver
from jifen.items import ProductItem

class HuaxiaSpider(scrapy.Spider):
    name = 'huaxia'
    allowed_domains = ['creditshop.hxb.com.cn']
    start_urls = ['http://creditshop.hxb.com.cn/']

    def start_requests(self):
        start_urls = ['http://creditshop.hxb.com.cn/']
        yield Request(url=start_urls, callback=self.parse, dont_filter=True)


    def parse(self, response):
        products = response.xpath(".//div[@class='details_member_right']/div[@class='boundCarBox']")

        for product in products:
            item = ProductItem()
            # item['username'] =product.xpath(".//div[@class='details_member']//div[@class='boundCarBox']//div/b")
            item['integral'] =product.xpath(".//div/b")
            # item['bill'] =
            yield item



