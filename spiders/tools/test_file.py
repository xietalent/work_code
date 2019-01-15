from pykeyboard import PyKeyboard
from pymouse import PyMouse
from time import sleep

import time


k = PyKeyboard()

def input_str(s):
# '''输入一串英文'''
#     ss = k.return_key
    while True:
        # sleep(0.1)
        k.tap_key('a')
        # k.press_key(i)
        # k.release_key(i)
        # k.type_string('helloworld!')
        k.press_key(k.enter_key)
        # k.press_key(k.enter_key)
        # sleep(0.1)
        k.type_string('nihao')
        # sleep(0.1)
        k.press_key(k.space_key)
        k.press_key(k.enter_key)
        # sleep(0.1)
        k.press_key(k.tab_key)
        k.type_string('xinshi')



    k.press_key(k.enter_key)


input_str("hello ")
sleep(2)


