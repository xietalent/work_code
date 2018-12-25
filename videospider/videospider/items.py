# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideospiderItem(scrapy.Item):

    name = scrapy.Field() # 电影名字
    movie_info = scrapy.Field() # 电影简介
    image_url = scrapy.Field()# 海报链接
    story_info = scrapy.Field() # 剧情简介
    download_url = scrapy.Field() # 下载地址
