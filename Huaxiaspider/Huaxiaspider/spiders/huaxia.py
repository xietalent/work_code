# -*- coding: utf-8 -*-
import scrapy


class HuaxiaSpider(scrapy.Spider):
    name = 'huaxia'
    allowed_domains = ['creditshop.hxb.com.cn']
    start_urls = ['http://creditshop.hxb.com.cn/']

    def parse(self, response):
        pass
