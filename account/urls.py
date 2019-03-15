#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/6 14:03
# @File       : urls.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django.urls import path, re_path, include
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, \
    PasswordResetView,PasswordResetDoneView

from . import views

app_name = 'account'
urlpatterns = [
    # 自定义方法
    # re_path('^login/$', views.user_login, name='user_login'),
    # re_path('^logout/$', views.user_logout, name='user_logout'),

    # django内置方法
    re_path('^login/$', LoginView.as_view(template_name='account/login.html'), name='user_login'),
    re_path('^logout/$', LogoutView.as_view(template_name='account/logged_out.html'), name='user_logout'),

    re_path('^password_reset/$', PasswordResetView.as_view(success_url=reverse_lazy('account:password_reset_done')), name='password_reset'),
    re_path('^password_reset_done/$', PasswordResetDoneView.as_view(), name='password_reset_done'),

    re_path('^password_change/$', PasswordChangeView.as_view(template_name='account/password_change_form.html',
                                                             success_url=reverse_lazy('account:password_change_done')),name='password_change'),
    re_path('^password_change_done/$',PasswordChangeDoneView.as_view(template_name='account/password_change_done.html'),name='password_change_done'),

    re_path('^register/$', views.register, name='user_register'),
    re_path('^userinfo/$', views.myself, name='user_info'),
    re_path('^userinfo_edit/$', views.myself_edit, name='userinfo_edit'),
    re_path('^my_image/$', views.my_image, name='my_image'),
]
