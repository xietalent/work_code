from django.shortcuts import render
from  datasapp import models
from django.http import HttpResponse
from django.template import loader
from datetime import  datetime
# Create your views here.
import random
# def datasy(request):
#
#
#     return render(request,'bank/datasys.html')


def info(request):
    num = random.randint(1,100)
    points = num
    context = {'points':points}
    jifen = models.User.objects.all()
    # return render(request, 'bank/info.html',{"jifen":jifen})
    return render(request, 'bank/info.html',locals())

def show_info(request):
    jifen =models.User.objects.all()
    return render(request,'bank/info.html',{"jifen":jifen})
    # return render(request,'bank/show_info.html',{"jifen":jifen})
    # return render(request,'bank/show_info.html',locals())