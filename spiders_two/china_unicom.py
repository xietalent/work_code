# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import  By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from logging import  getLogger
from lxml import etree
from aip import  AipOcr

from PIL import Image
from urllib import request,response
# from tools.keybord_DD import DD_input

import time
import lxml
import requests
import ctypes
import urllib
import urllib3
import pytesseract
import pytesseract.pytesseract

class China_unicom(object,timeout = None):
    def __init__(self):
        self.timeout = timeout
        self.logger = getLogger(__name__)
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    def process_request(self):
        pass

    def start_spider(self):
        pass
    pass


if __name__ == '__main__':
    time1 = time.clock()
    runs = China_unicom()
    tres1 = runs.start_spider()
    time2 = time.clock()
    time3 = round(time2 - tres1, 2)
    print("总耗时:{}".format(time3))