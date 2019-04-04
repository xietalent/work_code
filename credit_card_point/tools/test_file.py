from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
from time import sleep

import time



driver = webdriver.Chrome360()
# driver.get("https://perbank.abchina.com/EbankSite/startup.do?r=6FD4F769ED09906B")
driver.get("https://user.cmbchina.com/User/Login")
# driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")

time.sleep(3)
# 默认在取消按钮上，先切换到保存文件上
k = PyKeyboard()

# 模拟Tab
time.sleep(2)
k.press_key(k.enter_key)
k.release_key(k.enter_key)
time.sleep(1)
k.tap_key(k.tab_key)


k.type_string('wodeshijie')
k.press_key(k.space_key)
k.release_key(k.space_key)
time.sleep(2)

k.press_key(k.tab_key)
k.release_key(k.tab_key)
k.tap_key(k.enter_key)
time.sleep(2)
s = '123123'
for i in s:
    sleep(0.1)
    k.tap_key(i)
k.type_string('adfasd4546423')
# 发送Enter回车
k.press_key(k.tab_key)
k.release_key(k.tab_key)
k.type_string('dsad')

k.press_key(k.space_key)
k.release_key(k.space_key)


# k.tap_key(k.enter_key)

# time.sleep(5)
# driver.close()



