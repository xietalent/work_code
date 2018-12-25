# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HelloscrapyItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


class LabItem(scrapy.Item):
    text = scrapy.Field()
    author = scrapy.Field()
    detail = scrapy.Field()


class LabDetailItem(scrapy.Item):
    title = scrapy.Field()
    content = scrapy.Field()