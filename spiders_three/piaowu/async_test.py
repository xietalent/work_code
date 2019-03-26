
import time
import asyncio
from time import sleep

async def timer():
    for i in range(100):
        print(i)
        await  asyncio.sleep(2)
        sleep(0.1)
        print(i*10)
# timer()

#range
# range
# class MyRange():
#     def __init__(self,start_nums,end_nums=None,step=1):
#         if end_nums is not None:
#             self.start = start_nums
#             self.end = end_nums
#             self.step = step
#         else:
#             self.start = 0
#             self.end = start_nums
#             self.step = step
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         if self.step>0:
#             if self.start<self.end:
#                 count = self.start
#                 self.start +=self.step
#                 return count
#             else:
#                 raise StopIteration
#         elif self.step <0:
#             if self.start > self.end:
#                 count = self.start
#                 self.start += self.step
#                 return count
#             else:
#                 raise StopIteration
#         else:
#             print("憨憨,步长不能为0")
#             raise StopIteration
#
# for i in MyRange(1000,100,-3):
#     print(i)


import threading
import asyncio

async def hello(num=1):
    print('Hello world! (%s)' % threading.currentThread())
    print(num)
    print(time.clock())
    await asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())
    print(num+5)
    # print(time.clock())

# loop = asyncio.get_event_loop()
# tasks = [hello(1), hello(2)]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()

from selenium import webdriver

# bro = webdriver.Chrome()
#
# bro.get("https://passport.damai.cn/login?")


class Complex:
    def __init__(self, realpart, imagpart):
        self.r = realpart
        self.i = imagpart

# x = Complex(3.0, -4.5)
# x.counter = 1
# while x.counter < 10:
#     x.counter = x.counter * 2
# print(x.counter)
# del x

class MyClass:
    """A simple example class"""
    i = 12345
    def f(self):
        return 'hello world'

x = MyClass()

s = x.f
print(s)
print(x.i)

# while True:
#     print(s())

