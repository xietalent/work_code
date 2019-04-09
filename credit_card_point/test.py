
import os
import numpy as np
import cv2
from PIL import Image
import pytesseract.pytesseract
from aip import AipOcr
import base64

def read_img():
    # img = Image.open(".\images\pingan\pingan_imgcode.png")
    img = Image.open(".\images\zx_imcode.png")

    #灰度化处理,去除干扰
    images = img.convert('L')
    # 杂点清除掉。只保留黑的和白的。返回像素对象
    data = images.load()
    w, h = images.size
    for i in range(w):
        for j in range(h):
            # if data[i, j] > 140:
            if data[i, j] > 180:
                data[i, j] = 255  # 纯白
            else:
                data[i, j] = 0  # 纯黑
    images.show()
    ims = images.tobytes()
    print(type(ims))
    print(ims)

    img = cv2.imdecode(np.fromstring(ims,np.uint8),1)
    img.show()
    # print(img)

    result = pytesseract.pytesseract.image_to_string(images)
    print(result)

    # 你的 APPID AK SK
    APP_ID = '15193395'
    API_KEY = 'HWeCszHYYnbWxcVGFLosY0KS'
    SECRET_KEY = 'FoXrkDDgoqL3gi2ynmnhtm8bjiSiiIe6'

    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

    #  读取图片

    def get_file_content(filePath):
        with open(filePath, 'rb') as fp:
            return fp.read()

    # 调用通用文字识别（高精度版）
    # client.basicAccurate(image)

    # 如果有可选参数
    options = {}
    options["recognize_granularity"] = "big"
    options["language_type"] = "CHN_ENG"
    options["detect_direction"] = "true"
    options["detect_language"] = "true"
    options["vertexes_location"] = "true"
    options["probability"] = "true"

    # for i in range(w):
    #     for j in range(h):
    #         if data[i, j] > 180:
    #             data[i, j] = 255  # 纯白
    #         else:
    #             data[i, j] = 0  # 纯黑
    #
    # # s = input("是否显示处理后图片:")
    # s = "否"
    # if s == "是":
    #     images.show()
    #     # sleep(5)
    #     # image.close()
    # else:
    #     pass

    images.save(r'images\pingan\clean_captcha.png')  # 保存处理后图片
    image2 = get_file_content(r"images\pingan\clean_captcha.png")

    # image2 = images.tobytes()
    # 带参数调用通用文字识别(高精度版)
    result = client.basicAccurate(image2, options)
    # res = result["words_result"]
    # print("识别结果为:")
    # s2 = images.split("\\")[-1]
    # s3 = s2.split('.')[0]

    # 写入文件
    # for res1 in res:
    #     with open(r'识别结果\{}.txt'.format(s3), "a", ) as fp:
    #         fp.write(res1["words"])
    #         fp.close()
    # print("该图片的识别结果为:" + result["words_result"][0]["words"])
    print(result)

read_img()

