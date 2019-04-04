# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

from tools.zhaohang.keybord_DD import DD_input
# from tools.zhaohang.keybord_winio import start_input

from selenium import webdriver
from time import sleep

sleep(1)
user_name = "13728647735"
passwd = r"ASD12%^*%^*,./<>?123ZXC456vbnm"
# 获取窗口句柄
# now_handle = driver.current_window_handle  # 获取当前窗口句柄
# print("当前窗口的句柄为:{}".format(now_handle))  # 输出当前获取的窗口句柄
# 填写账号密码
# sleep(1)
uname = DD_input()
uname.dd(user_name)
# sleep(1)
# uname.dd_table()
sleep(0.1)
# uname = DD_input()
uname.dd(passwd)
# sleep(0.2)
# uname.dd_table()
# sleep(0.2)
# uname.dd_enter()
# uname.dd_spacebar()

