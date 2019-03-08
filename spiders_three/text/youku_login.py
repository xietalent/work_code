from selenium import webdriver
from time import sleep

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
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from PIL import Image
from io import BytesIO
from PIL import Image
from urllib import request,response
# from tools.keybord_DD import DD_input

import random
import time
import re
import requests
import time

driver = webdriver.Chrome()

driver.get("http://point.youku.com/page/mall/index")

driver.find_element_by_class_name("nologin").click()

sleep(1)

# driver.find_element_by_xpath("//div[@id='YT-loginFrame-body']/form/div[1]/input").send_keys("1234")
driver.find_element_by_id("YT-ytaccount").send_keys("15071469916")

# driver.find_element_by_xpath("//div[@id='YT-loginFrame-body']/form/div[2]/input").send_keys("1234")
driver.find_element_by_id("YT-ytpassword").send_keys("zx150219")

def start_move(distance):
    # 点击滑块滑动
    element = driver.find_element_by_id("nc_1_n1z")
    # 点击小图片滑动
    # element = driver.find_element_by_xpath(
    #     "//div[@class='jigsaw']/div[@class='jigsaw-bg']/div[contains(@class,'jigsaw-block')]")

    # 这里就是根据移动进行调试，计算出来的位置不是百分百正确的，加上一点偏移
    distance -= element.size.get('width') / 2
    # distance += 15
    distance += 21

    # 按下鼠标左键
    ActionChains(driver).click_and_hold(element).perform()
    time.sleep(0.5)
    while distance > 0:
        if distance > 10:
            # 如果距离大于10，就让他移动快一点
            # span = random.randint(5, 8)
            span = random.randint(10, 15)
        else:
            # 快到缺口了，就移动慢一点
            span = random.randint(2, 3)
        ActionChains(driver).move_by_offset(span, 0).perform()
        distance -= span
        time.sleep(random.randint(10, 50) / 100)

    ActionChains(driver).move_by_offset(distance, 1).perform()
    ActionChains(driver).release(on_element=element).perform()

def img_code(driver):

    pass


driver.find_element_by_id("YT-nloginSubmit").click()
sleep(3)
try :
    distance = 320
    start_move(distance)
    sleep(2)
    img_code = input("请输入图形验证码:")
    driver.find_element_by_id("nc_1_captcha_input").send_keys(img_code)
    sleep(0.1)
    driver.find_element_by_id("nc_1_scale_submit").click()

except:
    pass


# sleep(0.1)
# driver.find_element_by_id("YT-nloginSubmit").click()

sleep(5)
# driver.quit()