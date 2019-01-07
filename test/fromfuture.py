# # from ___future__ import division
#
#
# # s = 3/5
# # s = 3//5
#
# # print(s)
#
import threading

balance = 0
lock = threading.Lock()


def change_it(n):
    global balance
    balance += n
    balance -= n


def run_thread(n):
    for i in range(10000):
        lock.acquire()
        try:
            change_it(n)
        finally:
            lock.release()


def create_thread():
    for i in range(30):
        t1 = threading.Thread(target=run_thread, args=(1,))
        t2 = threading.Thread(target=run_thread, args=(-1,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print(balance)


def _test_thread():
    create_thread()


def test():
    _test_thread()


test()


# import threading
#
# balance = 0
#
#
# def change_it(n):
#     global balance
#     balance += n
#     balance -= n
#
#
# def run_thread(n):
#     for i in range(10000):
#         change_it(n)
#
#
# def create_thread():
#     for i in range(30):
#         t1 = threading.Thread(target=run_thread, args=(1,))
#         t2 = threading.Thread(target=run_thread, args=(-1,))
#         t1.start()
#         t2.start()
#         t1.join()
#         t2.join()
#         print(balance)
#
#
# def _test_thread():
#     create_thread()
#
#
# def test():
#     _test_thread()
#
#
# test()
