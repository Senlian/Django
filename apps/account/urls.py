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
from django.urls import path, re_path
from django.contrib.auth import views as auth_views
from . import views as account_views


app_name = 'account'
urlpatterns = [
    re_path(r'^login/$', account_views.AccountLoginView, name='login'),
    re_path(r'^logout/$', account_views.AccountLogoutView, name='logout'),
    re_path(r'^register/$', account_views.AccountRegisterView, name='register'),
    re_path(r'^password_reset_email/$', account_views.AccountSendResetEmailView, name='password_reset_email'),
    re_path(r'^send_email_verify/$', account_views.AccountEmailVerifyView, name='send_email_verify'),
]
