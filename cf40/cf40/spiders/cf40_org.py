# -*- coding: utf-8 -*-
import scrapy


class Cf40OrgSpider(scrapy.Spider):
    name = 'cf40.org'
    allowed_domains = ['cf40.org.cn']
    start_urls = ['http://cf40.org.cn/']

    def parse(self, response):

        pass
