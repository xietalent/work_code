from django import forms
from django.forms import ValidationError


#创建用户注册同步数据的表单

class datasappForm(forms.Form):
    username = forms.CharField(max_length=40,min_length=12)
    passwd =   forms.CharField(widget=forms.PasswordInput)