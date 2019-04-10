#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/4/1 13:44
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.urls import path, re_path
from . import views as blog_views

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', blog_views.BlogIndexView, name='index'),
]