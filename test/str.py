


# s1 = "['/mall/base/validateImg.action?type=dynamicImgCode']"
#
# s2 = s1.split("'" , 2)
#
# s4 = s2[1]
#
# print(s2)
# print(s4)
# s2 = s1.strip("['")
# s3 = s2.strip("']")

# s3 = s1[2:-2]
#
# print(s3)


list2 = [1,2,4,5,6]

res2 = map(str,list2)

print(list2)



from functools import  reduce


def  myInt(strData):
    listStr = list(strData)

    def strToInt(strInt):
        # return  int(strInt)
        return {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "0": 0}[strInt]
    def func(a,b):
        return  a*10 + b
    return  reduce(func,map(strToInt,listStr))

strData = "564392"
print(myInt(strData))
print(type(myInt(strData)))


def add(a,b):
    return  a + b

res = reduce(add,list(range(1,101)))
print(res)
print(type(res))