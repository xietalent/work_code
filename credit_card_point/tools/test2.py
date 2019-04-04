

# account = input("用谁的账户(1/2):")
# if account == "1" :
#     phone_num = "15071469916"
#     passwd = "zc006688"
#     print("111111")
# else:
#     phone_num = "13728647735"
#     passwd = "419078chu"

# res = ['4654623,./']
#
# red = str(res).strip("['',./]")
#
# print(red)
#
# str1 = "jgsfjgkdf9gjdlk9dgjldkfj9谷歌"
#
# str2 = str1.split("9",3)
# print(str2)



# img_number = 1234
# if len(str(img_number)) != 4:
#     img_number = input("请手动输入验证码:")
# elif img_number ==1234:
#     print("这是1234,不是验证码哦")
# else:
#     print("ok了,爬开")

# n = 100
#
# sum = 0
# counter = 1
# while counter <= n:
#     sum = sum + counter
#     counter += 1
#
# print("1 到{}之和为:{}".format(n,sum))

#
# var = 1
#
# while var ==1:
#     num = input("请输入一个数字:")
#
#     num = int(num)*3
#     print("你输入了数字{}".format(num))


import selenium

#selenium 代理Ip测试
import random

# num = range(10)
#
# print(num)
#
# for i in range(1,10):
#     num = i
#     print(num)

# with open(r"E:\code\spiders\text\ss.txt","w+",encoding="utf8") as fp:
#     fp.write("爬开")
#     fp.close()


header = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
    }



with open(r"E:\code\spiders\text\proxy.txt","r",encoding="utf8") as fp:
    ip_list = []
    for i in range(1,77):
        res = fp.readline()
        # print(res)
        res = res.strip("\n")
        ip_dict = {}
        ports,ips = res.split(":")
        ip_dict[ports] = ips
        ip_list.append(ip_dict)
        # print(ip_dict)

        # print(type(res))
    print(ip_list)


import sys

sys.setrecursionlimit(1000000)

def page(pages):
    myres = pages
    print(myres)

    pages +=1

    if pages <10:
        page(pages)
    else:
        pass
    # while pages <10:
    #     pages +=1
    # return page(pages)




page(1)