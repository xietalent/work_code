from aip import AipOcr
from PIL import Image


""" 你的 APPID AK SK """
APP_ID = '15193395'
API_KEY = 'HWeCszHYYnbWxcVGFLosY0KS'
SECRET_KEY = 'FoXrkDDgoqL3gi2ynmnhtm8bjiSiiIe6'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)


""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()


""" 调用通用文字识别（高精度版） """
# client.basicAccurate(image)

""" 如果有可选参数 """
# options = {
#     "detect_direction":"true",
#     "probability":"true"
# }
options = {}
options["recognize_granularity"] = "big"
options["language_type"] = "CHN_ENG"
options["detect_direction"] = "true"
options["detect_language"] = "true"
options["vertexes_location"] = "true"
options["probability"] = "true"

# image = Image.open(r'C:\Users\Administrator\Desktop\als.jpg')
image0 = input("请输入图片路径:")


image = Image.open(image0)
# image = Image.open(r'C:\Users\Administrator\Desktop\7708.jfif')

# 灰度化
image = image.convert('L')
# 杂点清除掉。只保留黑的和白的。返回像素对象
data = image.load()
w, h = image.size
for i in range(w):
    for j in range(h):
        if data[i, j] >180:
            data[i, j] = 255  # 纯白
        else:
            data[i, j] = 0  # 纯黑

s = input("是否显示处理后图片:")
if s == "是":
    image.show()
else:
    pass
image.save('clean_captcha.png')
# image2 = get_file_content(r'C:\Users\Administrator\Desktop\als.jpg')
image2 = get_file_content("clean_captcha.png")

""" 带参数调用通用文字识别（高精度版） """
result = client.basicAccurate(image2, options)

res = result["words_result"]

# print("识别结果为:")

s2 = image0.split("\\")[-1]

s3 = s2.split('.')[0]
#写入文件
for  res1 in res:
    with open(r'D:\文字识别\识别结果\{}.txt'.format(s3),"a",) as fp:
        fp.write(res1["words"])
        fp.close()


# print("该图片的识别结果为:"+result["words_result"][0]["words"])

# C:\Users\Administrator\Desktop\005.jpg
