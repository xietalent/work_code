# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class JifenItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass

class ProductItem():
    collections = 'products'
    # username 用户名
    # integral 积分
    # bill 账单

    # username = Field()
    integral = Field()
    # bill = Field()




