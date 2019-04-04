# Licensed to the Software Freedom Conservancy (SFC) under one
# -*- coding: utf-8 -*-

from zhongxin import Zhongxin_I
from zhaoshang_ import Zhanoshang_bank
from pingan_chrome import Pingan_C
from china_bank import China_bank


class Start():
    def __init__(self, *args, **kwargs):
        # super().__init__(*args, **kwargs)
        pass

    def zhong_xin(self):
        zhongx = Zhongxin_I()
        zhongx.parses()

    def zhaoshang(self):
        zhaosh = Zhanoshang_bank()
        zhaosh.start_spider()

    def pinan(self):
        pinan_bank = Pingan_C()
        pinan_bank.process_request()

    def china_b(self):
        china_ban = China_bank()
        china_ban.start_spider()

def main():
    select = input("请选择银行对应编号{中信:1,招商:2,平安:3,中行:4}:")
    runs = Start()
    if select == '1':
        runs.zhong_xin()
    elif select == '2':
        runs.zhaoshang()
    elif select == '3':
        runs.pinan()
    elif select =='4':
        runs.china_b()
    else:
        pass

if __name__ == '__main__':
    main()
