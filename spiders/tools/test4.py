# coding=gbk




import os

print(os.path.abspath("."))

ss = os.getenv('LOCALAPPDATA')

print(ss)

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome360()
driver.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("seleniumhq" + Keys.RETURN)
time.sleep(3)
driver.quit()