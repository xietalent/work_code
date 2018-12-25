import requests
from urllib import request,parse

imgurl = "https://creditshop.hxb.com.cn/mall/base/validateImg.action?type=dynamicImgCode"

imgs = request.urlretrieve(imgurl, "./test.png")
imgs = request.urlretrieve(imgurl, "./test.jpg")