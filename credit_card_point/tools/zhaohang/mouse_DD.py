from ctypes import *
from time import sleep

import  time

dd_dll = windll.LoadLibrary(r'D:\installPakge\DD85590\DD85590.64.dll')

x= 1920//2
y = 1080//2
dd_dll.DD_mov(100,20)
sleep(1)
dd_dll.DD_mov(x,y)

dd_dll.DD_btn(1)
sleep(2)
dd_dll.DD_btn(2)


class DD_mouse(object):
    def __init__(self):

        pass