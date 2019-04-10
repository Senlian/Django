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
from django.db.models import Q
from django.contrib.auth.models import User
from django.core.cache import cache
from django.utils.translation import gettext_lazy as _


class AccountLoginForm(forms.Form):
    username = forms.CharField(max_length=200, label='用户名', widget=widgets.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'autocomplete': 'off',
            "autofocus": "autofocus",
            'placeholder': '用户名 | 邮箱',
            "oninvalid": "setCustomValidity('用户名不能为空哟')",
            "oninput": "setCustomValidity('')"
        }))

    password = forms.CharField(label='密码', widget=forms.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '密码',
            "oninvalid": "setCustomValidity('密码不能为空哟')",
            "oninput": "setCustomValidity('')"
        }))

    remember = forms.ChoiceField(label='记住密码', required=False, initial=False, choices=((True, 1), (False, 0)),
                                 widget=forms.CheckboxInput(
                                     attrs={
                                         'type': 'checkbox',
                                         'blank': True,
                                     }
                                 ))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and User.objects.filter(Q(username=username) | Q(email=username)):
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
            'title': '请再次输入密码!'
        }))

    email_verify = forms.CharField(label='邮箱验证码', required=False, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '请输入邮箱验证码',
            "oninvalid": "setCustomValidity('请输入正确的邮箱验证码')",
            "oninput": "setCustomValidity('')",
            'title': '请输入邮箱验证码'
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
                    "autofocus": "autofocus",
                    'pattern': '^[a-z]+(\w)*',
                    'title': '用户名由小写的字母、数字和下划线组成。',
                    "oninvalid": "setCustomValidity('用户名由小写的字母、数字和下划线组成，并以字母开头。')",
                    "oninput": "setCustomValidity('')",
                    'placeholder': '请输入用户名'
                }),
            'password': widgets.PasswordInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'autocomplete': 'off',
                    'minlength': "6",
                    'title': '密码长度不低于6位。',
                    "oninvalid": "setCustomValidity('密码长度不低于6位。')",
                    "oninput": "setCustomValidity('')",
                    'placeholder': '设置您的密码'
                }),
            'email': widgets.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'autocomplete': "off",
                    'required': True,
                    'pattern': '^([0-9A-Za-z\-_\.]+)@([0-9a-z]+\.[a-z]{2,3}(\.[a-z]{2})?)$',
                    'title': '请输入您的邮箱账号！',
                    "oninvalid": "setCustomValidity('请输入正确的邮箱地址')",
                    "oninput": "setCustomValidity('')",
                    'placeholder': '请输入您的邮箱账号'
                })
        }
        labels = {'email': '邮箱'}

    def clean_email(self):
        email = self.cleaned_data['email']

        if User.objects.filter(email=email):
            raise forms.ValidationError('邮箱已被注册')
        return email

    def clean_password_agin(self):
        form_data = self.cleaned_data
        if form_data['password_agin'] != form_data['password']:
            raise forms.ValidationError('两次密码不一致！')
        return form_data['password_agin']

    def clean_email_verify(self):
        form_email_verify = self.cleaned_data['email_verify']
        email_to = self.cleaned_data.get('email', '')
        if not email_to or form_email_verify != cache.get('email_verify_{0}'.format(email_to.split('@')[0]), ''):
            raise forms.ValidationError('验证码错误！')
        return form_email_verify


class AccountEmailForm(forms.ModelForm):
    email_type = forms.ChoiceField(label='记住密码', initial=True, choices=((True, 1), (False, 0)),
                                   widget=forms.CheckboxInput(
                                       attrs={
                                           'type': 'checkbox',
                                           'hidden': True,
                                       }))

    class Meta:
        model = User
        fields = ('email',)
        widgets = {
            'email': widgets.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'autocomplete': "off",
                    'title': '请输入您的邮箱账号！',
                    'placeholder': '请输入您的邮箱账号'
                })
        }
        labels = {'email': '邮箱'}

    def clean_email_type(self):
        form_data = self.cleaned_data
        email_type = eval(form_data['email_type'])
        try:
            email = form_data['email']
        except Exception as e:
            raise forms.ValidationError('邮箱验证失败')

        if email_type:
            if User.objects.filter(email=email):
                raise forms.ValidationError('邮箱已被注册')
        else:
            if not User.objects.filter(email=email):
                raise forms.ValidationError('该邮箱还没有注册账号')
        return email_type

    def save(self, commit=False):
        return super().save(commit=False)
