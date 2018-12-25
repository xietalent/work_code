# from selenium import webdriver
#
# browser = webdriver.Chrome()
#
#
# browser2 = webdriver.PhantomJS()
# browser2.get('http://www.baidu.com')
# print("网址是:"+browser2.current_url)

import  pytesseract
from PIL import Image

tessdata_dir_config = '--tessdata-dir "C:\\Program Files (x86)\\Tesseract-OCR\\tessdata"'
iamge = Image.open('./154.jpg')
res = pytesseract.image_to_string(iamge,config=tessdata_dir_config)
print(res)