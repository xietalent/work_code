import pytesseract
import pytesseract.pytesseract
import PIL
import PIL.Image
from PIL import Image
from  time import sleep

#导入文件
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\als.jpg")
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\001.jpg")
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\002.jpg")
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\ima.jfif")
image=PIL.Image.open(r"C:\Users\Administrator\Desktop\7708.jfif")
# image=PIL.Image.open(r"C:\Users\Administrator\Desktop\5107.jfif")
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"

# 灰度化
image  = image.convert('L')

# 杂点清除掉。只保留黑的和白的。返回像素对象
data = image.load()
w, h = image.size
for i in range(w):
    for j in range(h):
        if data[i, j] > 125:
            data[i, j] = 255 # 纯白
        else:
            data[i, j] = 0 # 纯黑
image.save('clean_captcha.png')
image.show()

result = pytesseract.pytesseract.image_to_string(image)
print("识别为:{}".format(result))

# print("识别为:"+ pytesseract.pytesseract.image_to_string(image,lang="chi_sim"))

# image=PIL.Image.open(r"C:\Users\Tsinghua-yincheng\Desktop\SZday16\ocrdata\libaby.bmp")
# pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
# print(pytesseract.pytesseract.image_to_string(image,lang="chi_sim"))

#版本4不支持bmp
#版本4还是用3.02数据
#https://github.com/tesseract-ocr
