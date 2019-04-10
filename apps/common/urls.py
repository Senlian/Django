#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/28 13:52
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install
# @Desc       :
'''
from django.urls import re_path
from . import views as common_views


app_name = 'common'
urlpatterns = [
    re_path(r'^verify/$', common_views.CreateVerifyView, name='verify'),
]
