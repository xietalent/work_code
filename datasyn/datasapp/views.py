from django.shortcuts import render
from datasapp import models
from time import sleep
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages
from .forms import datasappForm,loginForm
from .models import User,Card_score
# from .Hxspider  import SeleniumMiddleware
from .Hxspider2  import SeleniumMiddleware,Logindo

import random
import threading

# Create your views here.


def login(request):
    form = loginForm(use_required_attribute=False)
    if request.method == "POST":

        # images,brows = threading.Thread(target=SeleniumMiddleware().process_request())
        # 启动爬虫,验证码
        sp = SeleniumMiddleware()
        images,brows = sp.process_request()
        # global brows
        # if form.is_valid():
            # info(request,brows)
            # sleep(1)
            # images.save("./static/img/imgcode.png")
            # images.show()

        # return  info(request,brows)
        return  render(request, 'bank/info.html')


    return render(request,"login/login.html")


def info(request,brows):
    form = datasappForm(use_required_attribute=False)
    # t2 = threading.Thread(target=SeleniumMiddleware().process_request())
    # t2.start()
    # form2 = datasappFrom2(use_required_attribute=False)
    if request.method == "POST":
        # sleep(4)
        # 处理数据
        #启动爬虫,验证码
        # sp = SeleniumMiddleware()
        # images, brows = sp.process_request()
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
            # sp = SeleniumMiddleware()
            # images, brows = sp.process_request()

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
            # render(request, 'bank/show_info.html')

            #启用爬虫2


            name = form.data['name']
            passwd = form.data['passwd']
            img_code = form.data['img_code']
            print("验证码是:"+img_code)

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
            img_code = clean_data["img_code"]

            clean_data2 = {
                "id":None,
                "name":name,
                "passwd":passwd,
                "img_code":img_code
            }

            print(clean_data2)
            inserts = User.objects.create(**clean_data2)
            # form.save()
            #信箱
            messages.success(request, "信息" + "同步成功")
            jifen = models.Card_score.objects.all()
            return render(request, 'bank/show_info.html', {"jifen": jifen})
    # num = random.randint(1, 100)
    # points = num
    # context = {'points': points}
    users = models.User.objects.all()
    # messages.success(request, "信息" + "同步成功")
    return render(request, 'bank/info.html', {'form': form}, {'users': users})




def show_info(request):
    jifen = models.User.objects.all()
    # return render(request,'bank/info.html',{"jifen":jifen})
    messages.success(request, "信息" + "同步成功")
    # jifen = models.User.objects.all()
    jifen = Card_score.objects.all()
#
    return render(request, 'bank/show_info.html', {"jifen": jifen})
    # return render(request,'bank/show_info.html',locals())




    # def close(self):
    #     self.close()
