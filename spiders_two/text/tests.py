
def anagramSolution(s1,s2):
    if s1 == s2:
        print("{}和{}是同一个词".format(s1, s2))
        return False
    if len(s1) == len(s2):
        ss = True
        for _ in s1:
            res1 = s1.count(_)
            res2 = s2.count(_)
            if res1 == res2 :
                pass
            else:
                ss = None
                break
        if ss :
            print("{}和{}是易位词".format(s1, s2))
        else:
            print("{}和{}不是易位词".format(s1, s2))
    else:
        print("{}和{}不是易位词".format(s1,s2))


# s1 = input("请输入第一个单词:")
# s2 = input("请输入第二个单词:")
# res = anagramSolution(s1,s2)

# s1 = "qwe"
# s2 = "ewq"

# for i in s1:
#     print(i)
#     print(s1.count(i))
#     print(s2.count(i))

str = "python"

print(str.center(200,"-"))

res = "订单号：   8333711542175490048"
res2 = res.split("：")[1]
print(res2)
res3 = res.split("：")[1].split(" ")[3]
res3 = res.split("：")[1].strip(" ")
print(res3)


str1 = "×1"

str2 = str1.split("×")
print(str2)
# res = ""