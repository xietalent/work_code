
#

from aip import AipOcr
from PIL import Image

""" 你的 APPID AK SK """
APP_ID = '15188939'
API_KEY = 'deq3Itvdip3GI42a4uazZcdD'
SECRET_KEY = 'hwmuoK78LiC1mrIQdHBa42DWOGAHRAEo '

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

""" 读取图片 """
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

#定义参数变量
options = {
    "recognize_granularity" :"big",
    "detect_direction": "true",
}


image = Image.open(r'C:\Users\Administrator\Desktop\7708.jfif')
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\5107.jfif")

# 灰度化
image = image.convert('L')
# 杂点清除掉。只保留黑的和白的。返回像素对象
data = image.load()
w, h = image.size
for i in range(w):
    for j in range(h):
        if data[i, j] > 125:
            data[i, j] = 255  # 纯白
        else:
            data[i, j] = 0  # 纯黑
image.save('clean_captcha.png')

# image2 = get_file_content(r'C:\Users\Administrator\Desktop\7708.jfif')
image2 = get_file_content('clean_captcha.png')
# print(image2)

""" 调用数字识别 """
result= client.numbers(image2)


# for key in result:
#     print(key,result[key])

print(result["words_result"][0]["words"])
""" 如果有可选参数 """
# options = {}
# options["recognize_granularity"] = "big"

# options["detect_direction"] = "true"

""" 带参数调用数字识别 """
client.numbers(image2, options)
