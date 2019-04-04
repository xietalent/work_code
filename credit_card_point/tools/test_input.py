
import pymouse,pykeyboard,os,sys
from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse

from time import sleep

# driver = webdriver.Chrome()
# driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")
#
# sleep(3)
#
# # 默认在取消按钮上，先切换到保存文件上
# k = PyKeyboard()
#
# # 发送tab
# k.press_key(k.tab_key)
# k.release_key(k.tab_key)
#
# sleep(3)
# # 发送回车
# # 这里用到两个方法，一个是press_key按住Tab键，另外一个是release_key释放按键。其实还有个方法tap_key
# # tap_key模拟点击
# # 先看下tap_key源码是怎么设计的，实际上tap_key就是封装的press_key和release_key这2个方法
# # character 传对应的键盘事件
# n=1
# # 默认只点一次
# interval=0
# # 如果有多次点击操作，中间的间隙时间，默认sleep时间为0
# def tap_key(self, character='', n=1, interval=0):
# # """Press and release a given character key n times."""
#     for i in range(n):
#         self.press_key(character)
#         self.release_key(character)
#         sleep(interval)




# # 改成tap_key操作

# driver = webdriver.Chrome()
# driver.get("https://www.autoitscript.com/files/autoit3/autoit-v3-setup.exe")
#
# sleep(3)
# 默认在取消按钮上，先切换到保存文件上
# k = PyKeyboard()

# 模拟Tab
# sleep(3)
# 发送Enter回车
# k.tap_key(k.enter_key)
# PyKeyboard其它操作
# 除了能模拟tab,enter这种操作，也能模拟在输入框输入内容.
# 基本操作方法,如输入h:k.tap_key(“h”)
# coding:utf-8
from selenium import webdriver
from pykeyboard import PyKeyboard
from pymouse import PyMouse
import time

# driver = webdriver.Chrome()
driver = webdriver.Chrome360()
driver.get("https://www.baidu.com/")
sleep(3)
k = PyKeyboard()

def input_str(s):
# '''输入一串英文'''
#     ss = k.return_key
    for i in s:
        sleep(0.1)
        k.tap_key(i)
        # k.press_key(i)
        # k.release_key(i)
        # k.type_string('helloworld!')
    k.press_key(k.enter_key)
    # k.press_key(k.enter_key)
    sleep(2)
    k.type_string('world!')
    sleep(2)
    k.press_key(k.enter_key)
    sleep(2)
    k.press_key(k.tab_key)
    k.type_string('xinshi')
    sleep(2)

    k.press_key(k.enter_key)
input_str("hello")
sleep(2)


sleep(5)

# driver.close()
driver.quit()