from django.shortcuts import render
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
    return render(request, 'bank/info.html',context)