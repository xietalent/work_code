# -*- coding: utf-8 -*-
import scrapy

from HelloScrapy.items import LabItem, LabDetailItem


class LabSpider(scrapy.Spider):
    name = 'lab'
    allowed_domains = ['lab.scrapyd.cn']
    start_urls = ['http://lab.scrapyd.cn/']

    def parse(self, response):

        next_url = response.xpath('//div[@id="main"]/ol[@class="page-navigator"]/li[@class="next"]/a/@href').extract_first()

        if next_url:

            print(next_url)

            yield scrapy.Request(url=next_url, callback=self.parse)

        quotes = response.xpath('//div[@id="main"]/div[@class="quote post"]')

        for quote in quotes:
            item = LabItem()
            text = quote.xpath('./span[@class="text"]/text()').extract_first()
            author = quote.xpath('./span/small[@class="author"]/text()').extract_first()
            detail = quote.xpath('./span/a/@href').extract_first()

            yield scrapy.Request(url=detail, callback=self.parse_detail)

            item["text"] = text
            item["author"] = author
            item["detail"] = detail

            yield item


    def parse_detail(self, response):

        title = response.xpath('//div[@id="main"]/article[@class="post"]/h1[@class="post-title"]/a/text()').extract_first()
        content = response.xpath('//div[@id="main"]/article[@class="post"]/div[@class="post-content"]').extract_first()

        item = LabDetailItem()
        item["title"] = title
        item["content"] = content

        yield item