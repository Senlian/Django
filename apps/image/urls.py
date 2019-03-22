#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/22 11:00
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.urls import path, re_path, include
from . import views
app_name = 'image'
urlpatterns = [
    re_path(r'^upload_image/$', views.upload_image, name='upload_image'),
    re_path(r'^list_images/$', views.list_images, name='list_images'),
    re_path(r'^edit_image/(?P<image_id>\d+)/$', views.edit_image, name='edit_image'),
    re_path(r'^del_image/$', views.del_image, name='del_image'),
]
