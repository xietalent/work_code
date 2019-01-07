from django import forms
from django.forms import ValidationError


#创建用户注册同步数据的表单

class datasappForm(forms.Form):
    name = forms.CharField(max_length=20,label="用户",error_messages={'required':'用户不能为空'})
    passwd =   forms.CharField(widget=forms.PasswordInput,error_messages={'required':'密码不能为空'})
    img_code = forms.CharField(max_length=10,label="验证码",error_messages={'required':'验证码错误'})


# class datasappFrom2(forms.Form):
#     img_code = forms.CharField(max_length=10, label="验证码", error_messages={'required': '验证码错误'})


class loginForm(forms.Form):
    name = forms.CharField(max_length=20, label="用户", error_messages={'required': '用户不能为空'})
    passwd = forms.CharField(widget=forms.PasswordInput, error_messages={'required': '密码不能为空'})

