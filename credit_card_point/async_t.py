import threading
import asyncio
import time

from threading import Thread

# @asyncio.coroutine
# def hello(name):
#     print("")

def consumer():
    r = ''
    while True:
        n = yield r
        print(n)
        if not n:
            return
        print("[CONSUMER] Consuming {}".format(n))
        r = '2000k'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n +=1
        print("[PRODUCER] Producing {}".format(n))
        r = c.send(n)
        print('[PRODUCER] Consumer return: {}'.format(r))
    c.close()

c = consumer()
produce(c)