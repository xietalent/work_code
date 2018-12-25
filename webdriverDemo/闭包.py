# 什么是闭包？
'''
在一些语言中（解释性语言，如python、JavaScript、PHP等），在函数中可以嵌套定义另一个函数时，如果内部函数引用了外部函数的变量，则可能产生闭包

'''
# 闭包产生的三个条件
# 1）必须有一个内部的嵌套函数
# 2）内部函数必须引用一个外部函数的变量
# 3）外部函数必须返回内嵌函数

# 在python这种解释性语言中我们可以把函数名看成是一个特殊的变量
# var fun = function(){
#
# } js中定义函数
c = 1000 # 全局变量c

def func1():
    a = 100
    # print(c)
    global c # 将c变量从全局作用域中引过来
    c = 2000 # 此时c对func1来说值只读的，如果要以读写的方式使用全局作用域中的c需要先引过来
    def func2():
        b = 200
        nonlocal a # 如果我们想以读写的方式使用外部函数的某变量需要用nonlocal引过来
        a = 400
        c = a + b
        print(c)
    print(a)

    return func2

# func2()

p = func1()
p()
print(c)

# 【闭包的作用】1、装饰器
#  是一种设计模式，可以在不改变原来函数的基本功能的基础上，给原来的函数添加一些修饰的功能，作用是，可以降低代码的耦合度
# 装饰器的本质就是一个闭包，把一个函数作为参数
def outer(func):

    def inner():
        print("==============")
        func()

    return inner


# 定义一个普通的函数
def myfunc():
    print("Hi,girl! Are free?")

myfunc()

# 通过装饰器把函数装饰
f = outer(myfunc)
f()

# 在python2.4以后装饰器也可以写成
@outer
def hello():
    print("Hello")

hello()

# 这种写法就相当于
# hello = outer(hello)

#(2)回调
def funcA(a,b,c):
    p = a**2 + b**2
    c(p) # 把c当做一个函数，给c传一个参数p

def funcB(a):
    print("你好！我是B函数")
    print(a)

funcA(100,8,funcB)

