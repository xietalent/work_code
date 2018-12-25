# -*- coding: utf-8 -*-
import scrapy
from videospider.items import VideospiderItem

class VideoSpider(scrapy.Spider):
    name = 'video'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):

        # 找到所有的电影
        table_list = response.xpath("//div[@class='co_content8']//table")
        # print(table_list)
        # 遍历所有的电影
        for table in table_list:
            # 当前页面中只能提取出name和movie_info这两个属性
            # 创建一个item对象
            item = VideospiderItem()
            # 在网页中提取name和info
            item['name'] = table.xpath(".//a[@class='ulink']/text()").extract_first()
            item['movie_info'] = table.xpath('.//tr[last()]/td/text()').extract_first()
            # 由于其他的属性都在二级页面中，在这里需要提取出其url然后访问取属性
            #获取电影的二级页面的链接
            movie_url = "http://www.dytt8.net" + table.xpath(".//a[@class='ulink']/@href").extract_first()

            # 在这里调用下载器对象对二级页面进行下载
            # item的内容是分两部分完成，当前函数里面完成一部分，二级页面里面完成一部分，这里就涉及到了如何把item带到二级页面的回调函数中
            # 在scrapy里面Request下载器是通过meta参数将上个页面中的数据传递给下个页面的回调函数的，meta是一个字典
            yield scrapy.Request(url=movie_url,callback=self.parse_info,meta={"movie_item":item})

    # 定义一个回调函数，用于解析二级页面
    def parse_info(self,response):
        # 接收上个页面中item
        item = response.meta["movie_item"]
        print("=======================")
        # print(item)
        item['image_url'] = response.xpath("//div[@id='Zoom']//img[1]/@src").extract_first()
        # item["story_info"]
        sel = response.xpath("//div[@id='Zoom']")
        item["story_info"] = sel.xpath('string(.)').extract_first()
        item["download_url"] = response.xpath("//td[@bgcolor='#fdfddf']/a/text()").extract_first()

        yield item

# 作业：把这些数据写入管道（写成json和csv）海报下载，尝试抓取多页里面的内容



