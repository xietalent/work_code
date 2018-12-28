from django.shortcuts import render
from datasapp import models
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages
from .forms import datasappForm
from .models import User, Integral

import random
from time import sleep
# Create your views here.





# def datasy(request):
#
#
#     return render(request,'bank/datasys.html')


# def info(request):
#     msg_username=' '
#     msg_passwd = ' '
#     if request.method =='POST':
#         #获取提交的数据
#         username = request.POST.get('username',None)
#         if not username:
#             msg_username = '请输入卡号'
#         passwd = request.POST.get('passwd',None)
#         if not passwd:
#             msg_passwd = '请输入登录密码'
#         print(locals())
#         #判断数据是否为空,判断数据是否满足
#         return render(request, 'bank/info.html',{'msg_username':msg_username},{'msg_passwd':msg_passwd})
#
#     num = random.randint(1,100)
#     points = num
#     context = {'points':points}
#     jifen = models.User.objects.all()
#     # return render(request, 'bank/info.html',{"jifen":jifen})
#     messages.success(request,"信息"+"同步成功")
#     return render(request, 'bank/info.html',locals())

def info(request):
    form = datasappForm(use_required_attribute=False)
    if request.method == "POST":
        # sleep(5)
        # 处理数据
        datauser = User()
        datauser.name = request.POST.get('name')
        datauser.passwd = request.POST.get('passwd')
        form = datasappForm(request.POST, use_required_attribute=False)
        if form.is_valid():
            name = form.data['name']
            passwd = form.data['passwd']

            print(name)
            print(passwd)
            # return username,passwd
            print(form.cleaned_data)
            print(form.cleaned_data["name"])

            # 启动爬虫
            sp = SeleniumMiddleware(name,passwd)
            sp.process_request()
            sleep(30)
            # sp.close()

            # 用户密码存入数据库
            name = User.objects.create(**form.cleaned_data)

            # passwd = User.objects.create(**form.cleaned_data)
            # form.save()
            messages.success(request, "信息" + "同步成功")
            # jifen = models.User.objects.all()
            jifen = models.Integral.objects.all()
            return render(request, 'bank/show_info.html', {"jifen": jifen})
    num = random.randint(1, 100)
    points = num
    context = {'points': points}
    jifen = models.User.objects.all()
    # jifen = models.Integral.objects.all()
    # messages.success(request, "信息" + "同步成功")
    return render(request, 'bank/info.html', {'form': form}, {'jifen': jifen})


def show_info(request):
    jifen = models.User.objects.all()
    # return render(request,'bank/info.html',{"jifen":jifen})
    messages.success(request, "信息" + "同步成功")
    # jifen = models.User.objects.all()
    jifen = Integral.objects.all()

    return render(request, 'bank/show_info.html', {"jifen": jifen})
    # return render(request,'bank/show_info.html',locals())


from selenium import webdriver
from logging import getLogger
from aip import AipOcr
from time import sleep
import lxml
from lxml import etree
import pytesseract
import pytesseract.pytesseract
from urllib import request
from PIL import Image


class SeleniumMiddleware():
    def __init__(self, name, passwd, timeout=None, service_args=[]):
        self.logger = getLogger(__name__)
        self.timeout = timeout
        self.name = name
        self.passwd = passwd
        # self.browser = webdriver.PhantomJS()
        self.browser = webdriver.Chrome()

    def __del__(self):
        self.browser.close()

    # def process_request(self,request,spider):
    def process_request(self):
        self.logger.debug('PhantomJS is Starting')
        # page = request.meta.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")

        self.browser.get("https://creditshop.hxb.com.cn/mall/member/loginSSL.action")
        # self.browser.get("https://creditshop.hxb.com.cn/mall/member/doLogin.action")
        sleep(3)
        page_html2 = self.browser.page_source

        # 截取验证码的截图
        location = self.browser.find_element_by_id("imgCode").location
        self.browser.save_screenshot("feng.png")
        page_snap_obj = Image.open("feng.png")


        size = self.browser.find_element_by_id("imgCode").size
        left = location['x']
        top = location['y']
        right = location['x'] + size['width']
        bottom = location['y'] + size['height']

        images = page_snap_obj.crop((left, top, right, bottom))
        images.save("imcode.png")
        # images.show()
        # self.browser.save_screenshot("jifen02.png")

        # t验证码处理
        # """
        APP_ID = '15188939'
        API_KEY = 'deq3Itvdip3GI42a4uazZcdD'
        SECRET_KEY = 'hwmuoK78LiC1mrIQdHBa42DWOGAHRAEo '

        client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

        #读取图片
        def get_file_content(filePath):
            with open(filePath, 'rb') as fp:
                return fp.read()

        # 定义参数变量
        options = {
            "recognize_granularity": "big",
            "detect_direction": "true",
        }

        # image = Image.open(r"E:\code\test\imcode.png")

        # 灰度化
        # image = image.convert('L')
        image = images.convert('L')
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
        image.show()

        # image2 = get_file_content(r'C:\Users\Administrator\Desktop\7708.jfif')
        image2 = get_file_content('clean_captcha.png')
        # print(image2)

        #调用数字识别
        result = client.numbers(image2)
        # for key in result:
        #     print(key,result[key])

        # print(result["words_result"][0]["words"])

        #可选参数添加
        client.numbers(image2, options)

        # result = pytesseract.pytesseract.image_to_string(image)
        print("验证码识别为:{}".format(result["words_result"][0]["words"]))  # 查看识别结果

        img_number = result["words_result"][0]["words"]

        self.browser.save_screenshot("jifen001.png")

        sleep(1)
        # imgcode = input("请输入验证码:{}".format(result))
        sleep(2)
        self.browser.find_element_by_id("doLogin_loginNumber").send_keys("{}".format(self.name))
        # self.browser.find_element_by_id("doLogin_loginNumber").send_keys("6259691129820511")
        # self.browser.find_element_by_id("doLogin_loginPwd").send_keys("zc006688")
        self.browser.find_element_by_id("doLogin_loginPwd").send_keys("{}".format(self.passwd))
        # self.browser.find_element_by_name("imgCode").send_keys("{}".format(imgcode))
        self.browser.find_element_by_name("imgCode").send_keys("{}".format(img_number))
        sleep(5)

        # 登录
        self.browser.find_element_by_id("doLogin_0").click()
        sleep(3)

        # 我的积分
        self.browser.find_element_by_id("leftMenu1").click()
        sleep(2)

        # 1  打开可用积分查询栏
        # self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a/@href").click()
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[1]/a").click()
        sleep(3)

        # 点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen02.png")
        page_html = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        items = []
        response = etree.HTML(page_html)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            item = {}
            my_integral = div.xpath(".//div[@class='boundCarBox']//div/b/text()")[0]

            item = {
                "my_integral": my_integral,
            }
            items.append(item)
            print(my_integral)
            print(type(my_integral))
            print(items)

        # 2  打开信用卡积分明细查询
        self.browser.find_element_by_xpath("//div[(@class='details_member_left_box')][1]//li[2]/a").click()
        sleep(3)

        # 点击查询
        self.browser.find_element_by_class_name("inputBoxSubmit").click()
        sleep(2)
        self.browser.save_screenshot("jifen03.png")
        page_html2 = self.browser.page_source

        # print("当前网址"+self.browser.page_source)
        # return page_html
        response = etree.HTML(page_html2)
        divs = response.xpath(".//div[@class='details_member']/div[@class='details_member_right']")
        for div in divs:
            # item = {}
            bill = div.xpath(".//div[@class='details_member']//div[@class='faqBox']/em/text()")

            item = {
                "bill": bill,
            }
            items.append(item)
            print(bill)
            print(type(bill))
            print(items)

        return page_html

    # def close(self):
    #     self.close()
