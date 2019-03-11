
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


browser = webdriver.Chrome()
browser.set_window_size(1200,800)
browser.get("https://www.sasa.com/account/login")

try:
    sleep(1)
    browser.find_element_by_xpath("//div[@class='signupbox']//li[1]/span/input").send_keys("19128324901")
    sleep(0.1)
    # browser.find_element_by_xpath("//div[@class='signupbox']//li[2]/span/input").send_keys("zc006699")
    browser.find_element_by_xpath("//div[@class='signupbox']//li[2]/span/inp").send_keys("zc006699")
    sleep(0.1)
    img_code = input("请输入图形验证码:")
    browser.find_element_by_xpath("//div[@class='signupbox']//li[3]/span/input").send_keys(img_code)
    sleep(0.1)

    browser.find_element_by_xpath("//span[@class='form-act']/button").click()
except Exception as e:
    print(e)


sleep(10)
browser.quit()