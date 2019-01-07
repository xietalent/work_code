from selenium import webdriver
browser = webdriver.Ie()

browser.get('https://www.baidu.com/')
browser.get('https://bank.pingan.com.cn/m/main/index.html')


# items = [{'my_integral': '0积分'}, {'bill': []}]
# ll = items[0]['my_integral']
# lp = items[1]['bill']
# print(lp)
# print(ll)
# print(
#     ll.lstrip()
# )

# my_in = {'my_integral': '0积分'}
# my_in = my_in["my_integral"]
# print(my_in)

# from enum import Enum
#
# class Color(Enum):
#     red = 1
#     orange = 2
#     yellow = 3
#     green = 4
#     blue = 5
#     indigo = 6
#     purple = 7
#
#
# print(Color['red'])
# print(Color(2))
#
# ss = Color.red.name
# ss = Color.red.value
#
# print(
#     ss
# )
#
# for c in Color:
#     print(c)

data1 = {'name': '11111111111', 'passwd': 'zc006688', 'img_code': '000999'}

name = data1["name"]
print(name)

passwd = data1["passwd"]

img_code = data1["img_code"]
data2 = {
    "name":name,
    "passwd":passwd
}
print(data2)

