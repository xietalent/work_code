from django.shortcuts import render
from datasapp import models
from django.http import HttpResponse
from django.template import loader
from datetime import datetime
from django.contrib import messages
from .forms import datasappForm
from .models import User,Card_score
from .Hxspider  import SeleniumMiddleware

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

            # print(name)
            # print(passwd)
            # return username,passwd
            # print(form.cleaned_data)
            # print(form.cleaned_data["name"])

            # 启动爬虫
            sp = SeleniumMiddleware(name,passwd)
            sp.process_request()
            sleep(30)
            # sp.close()

            # 用户密码存入数据库
            print(form.cleaned_data)
            name = User.objects.create(**form.cleaned_data)
            # ss = **form.cleaned_data
            # print(**form.cleaned_data)

            # passwd = User.objects.create(**form.cleaned_data)
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
    jifen = Integral.objects.all()

    return render(request, 'bank/show_info.html', {"jifen": jifen})
    # return render(request,'bank/show_info.html',locals())




    # def close(self):
    #     self.close()
