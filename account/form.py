#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/6 14:13
# @File       : form.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django import forms
from django.contrib.auth.models import User

from .models import UserProfile, UserInfo


# Form 表单数据不写入数据库
class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)


# ModelForm需要将表单数据写入数据库
class RegisterForm(forms.ModelForm):
    password = forms.CharField(label='password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='password2', widget=forms.PasswordInput)

    class Meta:
        # 对应数据模型，表示该表单存入对应表
        model = User
        # 数据库更改的字段
        fields = ("username", "email")
        # 数据库排除的字段
        # exclude = ()

    # 数据校验,在调用RegisterForm实例的is_valid方法时候执行
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("password do not match.")
        return cd['password2']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('birth', 'phone')


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)


class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school', 'company', 'profession', 'address', 'aboutme', 'photo')


if __name__ == '__main__':
    pass
