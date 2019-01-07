
import pandas as pd
import numpy as np
import matplotlib as plt

from selenium import webdriver
import time

# browser=webdriver.Chrome()
# # browser.get("https://www.zhihu.com/explore")
# browser.get("https://creditcard.ecitic.com/citiccard/ucweb/entry.do")
# print(browser.get_cookies())
# browser.add_cookie({"name":"name","domain":"www.zhihu.com","value":"germey"})
# print(browser.get_cookies())
# browser.delete_all_cookies()
# print(browser.get_cookies())
# time.sleep(5)
# browser.close()

# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# import time
#
# driver = webdriver.Chrome360()
# driver.get('http://www.baidu.com')
# driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)
# time.sleep(3)
# driver.quit()

from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

import os

__browser_url="C:\\Users\\THINK\\AppData\\Roaming\\360se6\\Application\\360se.exe"
# __browser_url="C:\\Users\\THINK\\AppData\\Local\\360Chrome\\Chrome\\Application\\360chrome.exe"
chrome_options=Options()
chrome_options.binary_location=__browser_url
dr=webdriver.Chrome(chrome_options=chrome_options)
# dr=webdriver.Chrome()
dr.get('https://www.baidu.com/')

