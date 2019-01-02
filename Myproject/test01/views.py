from django.shortcuts import render,reverse
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.

# def login(request):
#
#     return HttpResponse("我是白菜")

def login(request):

    return render(request,'login/login.html')



#反向解析
def home_my(request):

    # return HttpResponseRedirect(reverse('test01:login'))   #有命名空间namespace的写法
    return render(request,'homes/home_my.html')