
import time
import requests
import asyncio


from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

class Proxy_try(object):
    def __init__(self):
        chromeOptions = webdriver.ChromeOptions()
        # 设置代理
        chromeOptions.add_argument("--proxy-server=http://124.16.79.176:1080")
        # 一定要注意，=两边不能有空格，不能是这样--proxy-server = http://202.20.16.82:10152
        self.browser = webdriver.Chrome(chrome_options=chromeOptions)

    def test(self):
        # 查看本机ip，查看代理是否起作用
        self.browser.get("http://httpbin.org/ip")
        print(self.browser.page_source)

    def start(self):
        self.test()

if __name__ == '__main__':
    run = Proxy_try()
    run.start()

# requests.get()