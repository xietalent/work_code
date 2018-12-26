
"""datasyn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.conf.urls import url
# from django.urls import path
# from datasapp.views import datasy
from .views import info,show_info

urlpatterns = [
    # url(r'',datasy),
    url(r'^info/$',info,name='info'),
    url(r'^show_info/$',show_info,name='show_info')
    # url(r'^datas/$',datasy),
]
