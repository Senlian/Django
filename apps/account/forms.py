#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'''
# @license    : (C) Copyright 2013-{YEAR}, Node Supply Chain Manager Corporation Limited.
# @author     : Administrator
# @Email      :
# @Time       : 2019/3/28 13:41
# @File       : forms.py
# @Software   : PyCharm
# @Modules     :python3 -m pip install 
# @Desc       : 
'''
from django import forms
from django.forms import widgets
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _


class AccountLoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='用户名', widget=widgets.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '用户名 | 邮箱',
            "oninvalid": "setCustomValidity('用户名不能为空哟')",
            "oninput": "setCustomValidity('')",
        }))

    password = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '密码',
            "oninvalid": "setCustomValidity('密码不能为空哟')",
            "oninput": "setCustomValidity('')",
        }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and User.objects.filter(username=username):
            return username
        else:
            raise forms.ValidationError('用户名不存在')

class AccountRegisterForm(forms.ModelForm):
    password_agin = forms.CharField(label='确认密码', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '再次输入密码',
            "oninvalid": "setCustomValidity('请再次输入密码')",
            "oninput": "setCustomValidity('')",
            'title': '请再次输入密码!',
            'autocomplete': "off"
        }))

    class Meta:
        model = User
        fields = ('username', 'password', 'email')
        widgets = {
            'username': widgets.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'title': '用户名由小写的字母、数字和下划线组成。',
                    'placeholder': '请输入用户名',
                    'autocomplete': "off"
                }),
            'password': widgets.PasswordInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'title': '密码长度不低于6位。',
                    'placeholder': '设置您的密码',
                    'autocomplete': "off"
                }),
            'email': widgets.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'title': '请输入您的邮箱账号！',
                    'placeholder': '请输入您的邮箱账号',
                    'autocomplete': "off"
                })
        }
        labels = {'email': '邮箱'}
        help_texts = {
            'username': _('用户名由字母、下划线或数字组成'),
            'password': _('用户名由字母、下划线或数字组成'),
            'email': _('用户名由字母、下划线或数字组成'),
        }

    def clean_password_agin(self):
        form_data = self.cleaned_data
        if form_data['password_agin'] != form_data['password']:
            raise forms.ValidationError('两次密码不一致！')
        return form_data['password_agin']
