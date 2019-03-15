#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/4 15:50
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.urls import path, re_path, include
from . import views

app_name = 'blog'
urlpatterns = [
    re_path(r'^$', views.blog_title, name='blog_title'),
    re_path(r'^(?P<article_id>\d)/$', views.blog_articles, name='blog_articles'),
]
