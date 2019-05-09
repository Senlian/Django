#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms import widgets
from django.core.cache import cache
from django.core import mail
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from django.conf import settings

from django.contrib.auth.forms import UsernameField, AuthenticationForm

# 由于定制了用户管理模块，所以不能直接使用auth.models.User模型
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
            'placeholder': '用户名 | 手机 | 邮箱',
            "oninvalid": "setCustomValidity('用户名不能为空哟')",
            "oninput": "setCustomValidity('')"
        }))
    password = forms.CharField(label='密码', widget=widgets.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '密码',
            'onblur': 'var index = parent.layer.getFrameIndex(window.name);$(".alert-danger").remove("");parent.layer.style(index, {height: "496px"});',
            "oninvalid": "setCustomValidity('密码不能为空哟')",
            "oninput": "setCustomValidity('')"
        }))

    remember = forms.BooleanField(label='下次自动登录', required=False)

    verify = forms.CharField(max_length=10, required=False, label='验证码', widget=widgets.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '验证码',
            "oninvalid": "setCustomValidity('请输入验证码')",
            "oninput": "setCustomValidity('')"
        }))

    def clean(self):
        self.cleaned_data.get('remember')
        self.cleaned_data.get('verify')
        super(AccountsLoginForm, self).clean()
        return self.cleaned_data

    def clean_username(self):
        """函数功能.
            用户验证
        Args:
            self (object): 表单实例

        Returns:
            username: str
        """
        username = self.cleaned_data['username']
        auth_user = User.objects.filter(Q(username=username) | Q(email=username) | Q(phone=username))
        if username and auth_user:
            return auth_user[0].username
        else:
            raise forms.ValidationError('用户名不存在')

    def clean_password(self):
        """函数功能.
            密码验证
        Args:
            self (object): 表单实例

        Returns:
            password: str
        """
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        self.user_cache = authenticate(self.request, username=username, password=password)
        if self.user_cache is None:
            raise forms.ValidationError('密码和用户名不匹配')
        return password

    def clean_remember(self):
        """函数功能.
            通过session实现下次自动登录，
            remember=True，设置session保存周期为settings.SESSION_COOKIE_AGE
            remember=False，设置session保存周期为0，即退出浏览器清楚
        Args:
            self (object): 表单实例

        Returns:
            remember: Boolean
        """
        remember = self.cleaned_data.get('remember', False)
        if remember:
            self.request.session.set_expiry(None)
        else:
            self.request.session.set_expiry(0)
        return remember

    def clean_verify(self):
        """函数功能.
                验证码验证
        Args:
            self (object): 表单实例

        Returns:
            verify: str
        """
        verify = self.cleaned_data.get('verify', '')
        verify_code = self.request.session.get('verify', None)
        if verify_code and verify.lower() != verify_code.lower():
            raise forms.ValidationError('请输入正确的验证码')
        return verify


class AccountRegisterForm(forms.ModelForm):
    verify = forms.CharField(label='邮箱验证码', required=False, widget=forms.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'autocomplete': 'off',
            'placeholder': '请输入邮箱验证码',
            "oninvalid": "setCustomValidity('请输入正确的邮箱验证码')",
            "oninput": "setCustomValidity('')",
            'title': '请输入您在邮箱中收到的验证码'
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
                    'placeholder': '用于登录的用户名'
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
                    # 'pattern': '^([0-9A-Za-z\-_\.]+)@([0-9a-z]+\.[a-z]{2,3}(\.[a-z]{2})?)$',
                    'title': '请输入您的邮箱账号！',
                    "oninvalid": "setCustomValidity('请输入正确的邮箱地址')",
                    "oninput": "setCustomValidity('')",
                    'placeholder': '请输入您的邮箱账号'
                })
        }
        # 定义字段label_tag
        labels = {'email': '邮箱'}

    def clean_email(self):
        """函数功能.
                验证邮箱是否被注册
        Args:
            self (object): 表单实例

        Returns:
            verify: str
        """
        email = self.cleaned_data['email']
        if email and User.objects.filter(email=email):
            raise forms.ValidationError('邮箱{0}已被注册'.format(email))
        return email

    def clean_verify(self):
        """函数功能.
                邮箱验证码验证
        Args:
            self (object): 表单实例

        Returns:
            verify: str
        """
        verify = self.cleaned_data['verify']
        try:
            email = self.cleaned_data['email']
        except Exception as e:
            raise forms.ValidationError('邮箱已经注册或邮箱地址错误！')
        if email is not None and verify.strip().lower() != cache.get(
                'register_verify_{0}'.format(email.strip().lower().split('@')[0]), '').strip().lower():
            raise forms.ValidationError('验证码错误！')
        return verify


class AccountEmailForm(forms.Form):
    is_staff = forms.BooleanField(label='是否注册', required=False, initial=True)
    email = forms.EmailField(label='请输入您账号所绑定的邮箱地址', required=False, widget=widgets.EmailInput(
        attrs={
            'type': 'email',
            'class': 'form-control-lg',
            'autocomplete': "off",
            'required': False,
            'title': '请输入您的邮箱账号！',
            'onblur': '$(".alert-danger").remove("");',
            "oninvalid": "setCustomValidity('请输入正确的邮箱地址')",
            "oninput": "setCustomValidity('')",
            'placeholder': '邮箱'
        }))

    def clean_email(self):
        email = self.cleaned_data['email']
        is_staff = self.cleaned_data['is_staff']
        if not User.objects.filter(email=email):
            if is_staff:
                raise forms.ValidationError('该邮箱还没有在本站注册。')
        else:
            if not is_staff:
                raise forms.ValidationError('该邮箱已经在本站注册。')
        return email

    def get_user(self, email):
        auth_user = User.objects.filter(email=email)
        if auth_user:
            return auth_user[0].username
        else:
            from django.contrib.auth.models import AnonymousUser
            return AnonymousUser.username

    def set_cache(self, key, value, timeout):
        cache.set(key, value, timeout)

    def send_email(self, subject, to_email, from_email=None, message=None, html_message=None, **kwargs):
        from_email = from_email or settings.EMAIL_HOST_USER
        print('send')
        mail.send_mail(subject=subject, message=message, from_email=from_email,
                       recipient_list=[to_email], html_message=html_message, **kwargs)
        print('send ok')
