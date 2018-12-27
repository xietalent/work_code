from django import forms
from django.forms import ValidationError


#创建用户注册同步数据的表单

class datasappForm(forms.Form):
    name = forms.CharField(max_length=20,label="用户",error_messages={'required':'用户不能为空'})
    passwd =   forms.CharField(widget=forms.PasswordInput,error_messages={'required':'密码不能为空'})