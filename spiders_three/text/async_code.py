#
#
# # async def mouse():
# #     pass
from asyncio import wait
from retrying import retry
import time
import asyncio
import time
import requests
#
#
# async def demo1():
#     print("start1")
#     print("end1")
#
# async def demo2():
#     print("start2")
#     print("1")
#     print("2")
#     print('end2')
#
# c = demo1()
# d = demo2()
# # wait(3)
#
# try:
#     c.send(None)
# except StopIteration as s:
#     print(s)
#
#
# try:
#     d.send(None)
# except Exception as e:
#     print(e)
#     print(c)
#     print(d)
#
# print("1111111111111")
#
# def demoaa():
#     print("demoaa")
#     return "dfa"
# def demos():
#     print("start1")
#     yield demoaa()
#     print("end1")
#
# s = demos()
# # s.send(None)

def hel():
    print("ehofh")
    yield 2
    print("hhha")

s = hel()
# s.send(None)
s.send(None)

it = iter([1,2,3,4,5,6])

next(it)
# while True:
#     try:
#         x = next(it)
#         print(x)
#     except StopIteration:
#         break

async def test2(i):
    r = await other_test(i)
    print(i,r)

async def other_test(i):
    r = requests.get(i)
    print(i)
    await asyncio.sleep(2)
    print(time.time()-start)
    return r

url = ["https://segmentfault.com/p/1210000013564725",
       "https://www.jianshu.com/p/83badc8028bd",
       "https://www.baidu.com/"]

loop = asyncio.get_event_loop()
task = [asyncio.ensure_future(test2(i)) for i in url]
start = time.time()
loop.run_until_complete(asyncio.wait(task))
endtime = time.time()-start
print("总时间:{}".format(endtime))
loop.close()

import requests
from retrying import retry

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

@retry(stop_max_attempt_number=None)  # 最大重试次数，所有次数全部报错，才会报错
def _parse_url(url):
    print("开始请求")
    response = requests.get(url, headers=headers, timeout=3)  # 超时的时候回报错并重试
    assert response.status_code == 200  # 状态码不是200，也会报错并充实
    print("请求成功")
    return response


def parse_url(url):
    try:  # 进行异常捕获
        response = _parse_url(url)
    except Exception as e:
        print(e)
        response = None
    return response


ss = parse_url("https://www.google.com/")
