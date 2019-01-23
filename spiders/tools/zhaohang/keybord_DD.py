from ctypes import *

import  time

dd_dll = windll.LoadLibrary(r'D:\installPakge\DD85590\DD85590.64.dll')
# dd_dll = windll.LoadLibrary(r'D:\installPakge\DD85590\DD64.dll')

class DD_input(object):
    def __init__(self,):
        self.vk = {'5': 205, 'c': 503, 'n': 506, 'z': 501, '3': 203, '1': 201, 'd': 403, '0': 210, 'l': 409, '8': 208, 'w': 302,
        'u': 307, '4': 204, 'e': 303, '[': 311, 'f': 404, 'y': 306, 'x': 502, 'g': 405, 'v': 504, 'r': 304, 'i': 308,
        'a': 401, 'm': 507, 'h': 406, '.': 509, ',': 508, ']': 312, '/': 510, '6': 206, '2': 202, 'b': 505, 'k': 408,
        '7': 207, 'q': 301, "'": 411, '\\': 313, 'j': 407, '`': 200, '9': 209, 'p': 310, 'o': 309, 't': 305, '-': 211,
        '=': 212, 's': 402, ';': 410,'spacebar':603,'table':300,' ':603,}
        # 需要组合shift的按键。
        self.vk2 = {'"': "'", '#': '3', ')': '0', '^': '6', '?': '/', '>': '.', '<': ',', '+': '=', '*': '8','&': '7', '{': '[', '_': '-','|': '\\', '~': '`', ':': ';', '$': '4', '}': ']', '%': '5', '@': '2', '!': '1', '(': '9'}

    def down_up(self,code):
        # 进行一组按键。
        dd_dll.DD_key(self.vk[code], 1)
        dd_dll.DD_key(self.vk[code], 2)

    def dd(self,key):
        # 500是shift键码。
        for i in key:
            if i.isupper():
                # 如果是一个大写的字符。

                # 按下抬起。
                dd_dll.DD_key(500, 1)
                time.sleep(0.1)
                self.down_up(i.lower())
                dd_dll.DD_key(500, 2)

            elif i in '~!@#$%^&*()_+{}|:"<>?':
                # 如果是需要这样按键的字符。
                dd_dll.DD_key(500, 1)
                time.sleep(0.1)
                self.down_up(self.vk2[i])
                dd_dll.DD_key(500, 2)
            else:
                self.down_up(i)
    def dd_table(self):
        dd_dll.DD_key(300, 1)
        time.sleep(0.1)
        dd_dll.DD_key(300, 2)

    def dd_enter(self):
        dd_dll.DD_key(313, 1)
        time.sleep(0.1)
        dd_dll.DD_key(313, 2)



    # input("按任意键继续...")
    # 之后等待两秒。
    time.sleep(0.5)

    # 测试按键。
    # for i in 'http://www.ddxoft.com':
    #     dd(i)

class DD_mouse(object):

    pass

if __name__ == '__main__':
    # dd_list = input("输入字符串:")
    dd_list = r"efaeffaf5465465"
    ddin = DD_input()
    ddin.dd(dd_list)




