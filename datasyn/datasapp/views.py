from django.shortcuts import render
from  datasapp import models
from django.http import HttpResponse
from django.template import loader
from datetime import  datetime
from django.contrib import messages
from .forms import datasappForm
# Create your views here.
import random
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
    form = datasappForm()
    if request.method =="POST":
        #处理数据
        form = datasappForm(request.POST,use_required_attribute=False)
        # if form.is_valid():
        username = form.data['username']
        print(username)

    num = random.randint(1, 100)
    points = num
    context = {'points':points}
    jifen = models.User.objects.all()
    messages.success(request, "信息" + "同步成功")
    return render(request, 'bank/info.html',{'form':form},locals())

def show_info(request):
    jifen =models.User.objects.all()
    # return render(request,'bank/info.html',{"jifen":jifen})
    messages.success(request, "信息" + "同步成功")
    jifen = models.User.objects.all()
    return render(request,'bank/show_info.html',{"jifen":jifen})
    # return render(request,'bank/show_info.html',locals())