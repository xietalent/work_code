import requests

img_url = "https://www.saclub.com.cn/post/s20130510100049.jpg"
# img_url = "http://www.cf40.org.cn/plus/view.php?aid=13219"
pic= requests.get(img_url,timeout=5)

print(pic)
print(type(pic))
print(pic.content)
print(pic.url)
print(pic.headers)
print(pic.cookies)
print(type(pic.content))

file_name = "iamge" + str(1) + ".jpg"  # 图片名
with open((r"E:\code\spiders\text\zhongshihua\img\{}".format(file_name)), 'wb') as fp:
    fp.write(pic.content)
    fp.close()



