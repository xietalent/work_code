
import re
import os

# with open(r"‪E:\code\spiders_two\text\ver.txt",'r',encoding="utf-8") as fp:
# pattern= re.compile('background-image: url\("(.*?)"\); background-position: (.*?)px (.*?)px;')
# with open("ver.txt",'r') as fp:
# # with open(r"‪E:\code\spiders_two\text\ver.txt",'r') as fp:
#     ss = fp.readline()
#
#
#     my_res = pattern.search(ss)
#     print(my_res)


slist = [1,3,2,3,45,6,7]
str1 = "arewr465q4wr464"
list1 = [i for i in str1]
dict1 = {i:j for i in str1 for j in slist}

print(list1)
print(dict1)
