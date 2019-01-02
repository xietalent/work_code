from django.shortcuts import render
from datasapp import models
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages
from .forms import datasappForm
from .models import User,Card_score
# from .Hxspider  import SeleniumMiddleware
from .Hxspider2  import SeleniumMiddleware,Logindo

import random
from time import sleep
# Create your views here.



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

def login(request):
    # sp = SeleniumMiddleware()
    # images,brows= sp.process_request()

    form = datasappForm(use_required_attribute=False)
    # form2 = datasappFrom2(use_required_attribute=False)
    if request.method == "POST":
        # sleep(5)
        # 处理数据
        # 启动爬虫,验证码
        sp = SeleniumMiddleware()
        images, brows = sp.process_request()
        sleep(1)
        images.save("./static/img/imgcode.png")
        images.show()

        datauser = User()
        datauser.name = request.POST.get('name')
        datauser.passwd = request.POST.get('passwd')
        datauser.img_code = request.POST.get('img_code')
        form = datasappForm(request.POST, use_required_attribute=False)
        # form2 = datasappFrom2(use_required_attribute=False)

        if form.is_valid():
            name = form.data['name']
            passwd = form.data['passwd']
            img_code = form.data['img_code']
            print(img_code)


            # 启动爬虫
            # sp = SeleniumMiddleware(name,passwd)
            # sp.process_request()
            # sleep(5)
            # sp.close()

            # 启用爬虫2
            # sp = SeleniumMiddleware()
            # images,brows= sp.process_request()

            sleep(2)
            img_number = img_code
            logins = Logindo(name,passwd,img_number,brows)
            logins.process_req()

            # 用户密码存入数据库
            print(form.cleaned_data)
            # name = User.objects.create(**form.cleaned_data)
            # ss = **form.cleaned_data
            # print(**form.cleaned_data)

            clean_data = form.cleaned_data
            name = clean_data["name"]
            passwd = clean_data["passwd"]

            clean_data2 = {
                "id": None,
                "name": name,
                "passwd": passwd
            }
            print(clean_data2)
            inserts = User.objects.create(**clean_data2)

            # form.save()
            # 信箱
            messages.success(request, "信息" + "同步成功")
            jifen = models.Card_score.objects.all()
            return render(request, 'bank/show_info.html', {"jifen": jifen})

    jifen = models.User.objects.all()
    # jifen = models.Integral.objects.all()
    # messages.success(request, "信息" + "同步成功")

    return render(request,"login/login.html", {'form': form}, {'jifen': jifen})






def info(request):

    form = datasappForm(use_required_attribute=False)
    # form2 = datasappFrom2(use_required_attribute=False)
    if request.method == "POST":
        # sleep(5)
        # 处理数据
        #启动爬虫,验证码
        # sp = SeleniumMiddleware()
        # images, brows = sp.process_request()
        #
        # sleep(1)
        # images.save("./static/img/imgcode.png")
        # images.show()


        datauser = User()
        datauser.name = request.POST.get('name')
        datauser.passwd = request.POST.get('passwd')
        datauser.img_code = request.POST.get('img_code')
        form = datasappForm(request.POST, use_required_attribute=False)
        # form2 = datasappFrom2(use_required_attribute=False)


        if form.is_valid():
            name = form.data['name']
            passwd = form.data['passwd']
            img_code = form.data['img_code']
            print(img_code)

            # print(name)
            # print(passwd)
            # return username,passwd
            # print(form.cleaned_data)
            # print(form.cleaned_data["name"])

            # 启动爬虫
            # sp = SeleniumMiddleware(name,passwd)
            # sp.process_request()
            # sleep(5)
            # sp.close()

            #启用爬虫2
            # sp = SeleniumMiddleware()
            # images,brows= sp.process_request()

            # sleep(2)
            # img_number = img_code
            # logins = Logindo(name,passwd,img_number,brows)
            # logins.process_req()

            # 用户密码存入数据库
            print(form.cleaned_data)
            # name = User.objects.create(**form.cleaned_data)
            # ss = **form.cleaned_data
            # print(**form.cleaned_data)

            clean_data = form.cleaned_data
            name = clean_data["name"]
            passwd = clean_data["passwd"]

            clean_data2 = {
                "id":None,
                "name":name,
                "passwd":passwd
            }
            print(clean_data2)
            inserts = User.objects.create(**clean_data2)

            # form.save()
            #信箱
            messages.success(request, "信息" + "同步成功")
            jifen = models.Card_score.objects.all()
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
    jifen = Card_score.objects.all()

    return render(request, 'bank/show_info.html', {"jifen": jifen})
    # return render(request,'bank/show_info.html',locals())




    # def close(self):
    #     self.close()
