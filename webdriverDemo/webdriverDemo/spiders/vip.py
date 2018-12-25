# -*- coding: utf-8 -*-
import scrapy


class VipSpider(scrapy.Spider):
    name = 'vip'
    allowed_domains = ['vip.com']
    start_urls = ['https://category.vip.com/suggest.php?keyword=%E9%9D%A2%E8%86%9C&ff=235|12|1|1']

    def parse(self, response):
        # print(response)
        div_list = response.xpath("//div[starts-with(@id,'J_pro')]")

        print(div_list)


        pass
