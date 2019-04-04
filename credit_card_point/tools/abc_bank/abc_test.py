

# list1 = ['245454']
#
# res = list1[0]
#
# print(res)

# nums = [1,2,3,4,5]
nums = [2,4,6,8,10]

for n in nums:
    if n %2 ==1 :
        print("Odd exist")
        break
else:
    print( "Odd not exist")

try:
    # res = 1+10
    res = [1,2,3,4,5]
    print(res)
    ss= max(res)
    print(ss)
except Exception as e:
    print( "f Exception {e}".format(e))
