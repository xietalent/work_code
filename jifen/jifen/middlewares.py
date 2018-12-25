# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
# from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
from scrapy.http import HtmlResponse
from logging import getLogger
from time import sleep


class SeleniumMiddleware():
    def __init__(self,timeout=5,service_args=[]):
        self.logger = getLogger(__name__)
        # self.timeout = timeout
        self.browser = webdriver.PhantomJS()
        # self.browser.set_window_rect(1400,700)
        # self.browser.set_page_load_timeout(self.timeout)
        # self.wait = WebDriverWait(self.browser,self.timeout)

    def __del__(self):
        self.browser.close()

    def process_request(self,request,spider):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get('page', 1)
        try:
            self.browser.get(request.url)
            # self.browser.get("http://creditshop.hxb.com.cn/")
            sleep(4)
            self.browser.save_screenshot("jifen001.png")
            sleep(2)
            imgcode = input("请输入验证码:")
            sleep(2)
            self.browser.find_element_by_id("doLogin_loginNumber").send_keys("6259691129820511")
            self.browser.find_element_by_id("doLogin_loginPwd").send_keys("zc006688")
            self.browser.find_element_by_name("imgCode").send_keys("{}".format(imgcode))
            sleep(1)
            # driver.find_element_by_link_text("登录")[0].click()
            # driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[5]").click()
            # driver.find_element_by_xpath("//div[(@class='details_register_2')]//input/@src").click()

            # 登录
            self.browser.find_element_by_id("doLogin_0").click()


            # 点击查询
            self.browser.find_element_by_class_name("inputBoxSubmit").click()

            self.browser.save_screenshot("jifen02.png")
            return HtmlResponse(url=request.url, body=self.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)

        # @classmethod
        # def from_crawler(cls, crawler):
        #     return cls(timeout=crawler.settings.get('SELENIUM_TIMEOUT'),
        #                service_args=crawler.settings.get('PHANTOMJS_SERVICE_ARGS'))




# class ProxyMiddleWare(object):





class JifenSpiderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, dict or Item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Response, dict
        # or Item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class JifenDownloaderMiddleware(object):
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
