from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

import os

__browser_url=r'C:\Users\Administrator\AppData\Roaming\360se6\Application\360se.exe'

chrome_options=Options()
chrome_options.binary_location=__browser_url
driver=webdriver.Chrome(chrome_options=chrome_options)
driver.get('https://www.baidu.com/')
sleep(3)

driver.execute_script("window.scrollBy(0,200)","")  #向下滚动200px

driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")  #向下滚动到页面底部

