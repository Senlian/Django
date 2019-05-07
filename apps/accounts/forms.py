#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django import forms
from django.db.models import Q
from django.forms import widgets
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

from django.contrib.auth.forms import UsernameField, AuthenticationForm

User = get_user_model()


class AccountsLoginForm(AuthenticationForm):
    '''
        登录表单
    '''
    username = UsernameField(max_length=200, label='用户名', widget=widgets.TextInput(
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
            'onblur': 'var index = parent.layer.getFrameIndex(window.name);$(".alert-danger").remove("");parent.layer.style(index, {height: "496px"});',
            "oninvalid": "setCustomValidity('密码不能为空哟')",
            "oninput": "setCustomValidity('')"
        }))

    remember = forms.ChoiceField(label='记住密码', required=False, initial=False, choices=((True, 1), (False, 0)),
                                 widget=forms.CheckboxInput(
                                     attrs={
                                         'type': 'checkbox',
                                         'blank': True,
                                     }))

    def clean_username(self):
        username = self.cleaned_data['username']
        if username and User.objects.filter(Q(username=username) | Q(email=username)):
            return username
        else:
            raise forms.ValidationError('用户名不存在')

    def clean_password(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.user_cache = authenticate(self.request, username=username, password=password)
        if self.user_cache is None:
            raise forms.ValidationError('密码和用户名不匹配')
        return password


class AccountRegisterForm(forms.ModelForm):
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
