#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from django import forms
from django.db.models import Q
from django.forms import widgets
from django.conf import settings
from django.core import mail
from django.core.cache import cache
from django.contrib.auth import (authenticate, password_validation, get_user_model)
from django.utils.translation import gettext, gettext_lazy as _
from django.contrib.auth.forms import UsernameField, AuthenticationForm

# 由于定制了用户管理模块，所以不能直接使用auth.models.User模型
User = get_user_model()

# TODO：登录表单
class AccountsLoginForm(AuthenticationForm):
    '''
        登录表单
    '''
    username = UsernameField(max_length=200, label='用户名', widget=widgets.TextInput(
        attrs={
            'type': 'text',
            'class': 'form-control',
            'title': '请输入用户名、手机或者邮箱地址',
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
            'title': '请输入密码',
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
            'title': '请输入验证码',
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


# TODO：注册表单
class AccountsRegisterForm(forms.ModelForm):
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


# TODO：设置密码表单
class AccountsSetPasswordForm(forms.Form):
    password = forms.CharField(max_length=128, label="输入新密码", widget=widgets.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'minlength': "6",
            'title': '密码长度不低于6位。',
            "oninvalid": "setCustomValidity('密码长度不低于6位。')",
            "oninput": "setCustomValidity('')",
            'placeholder': '输入新密码'
        }))
    password_ = forms.CharField(max_length=128, label="确认新密码", widget=widgets.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'minlength': "6",
            'title': '密码长度不低于6位。',
            "oninvalid": "setCustomValidity('密码长度不低于6位。')",
            "oninput": "setCustomValidity('')",
            'placeholder': '确认新密码'
        }))
    error_messages = {
        'password_mismatch': _("The two password fields didn't match."),
    }

    def __init__(self, user, *args, **kwargs):
        """函数功能.
                表单初始化
        Args:
            user: 通过uidb64解析获得用户信息

        Returns:
            None
        """
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_password_(self):
        password = self.cleaned_data.get('password')
        password_ = self.cleaned_data.get('password_')
        if password and password_:
            if password != password_:
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        password_validation.validate_password(password_, self.user)
        return password_

    def save(self, commit=True):
        password = self.cleaned_data["password"]
        self.user.set_password(password)
        if commit:
            self.user.save()
        return self.user


# TODO：修改密码表单
class AccountsChangePwdForm(AccountsSetPasswordForm):
    password_old = forms.CharField(max_length=128, label="输入旧密码", widget=widgets.PasswordInput(
        attrs={
            'type': 'password',
            'class': 'form-control',
            'autocomplete': 'off',
            'minlength': "6",
            'title': '密码长度不低于6位。',
            "oninvalid": "setCustomValidity('密码长度不低于6位。')",
            "oninput": "setCustomValidity('')",
            'placeholder': '输入旧密码'
        }))

    error_messages = {
        **AccountsSetPasswordForm.error_messages,
        'password_incorrect': _("Your old password was entered incorrectly. Please enter it again."),
    }

    field_order = ['password_old', 'password', 'password_']

    def clean_password_old(self):
        """
        Validate that the password_old field is correct.
        """
        password_old = self.cleaned_data["password_old"]
        if not self.user.check_password(password_old):
            raise forms.ValidationError(
                self.error_messages['password_incorrect'],
                code='password_incorrect',
            )
        return password_old


# TODO：邮件表单
class AccountsEmailForm(forms.Form):
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
        """函数功能.
                邮箱验证
        Args:
            self (object): 表单实例

        Returns:
            verify: str
        """
        email = self.cleaned_data['email']
        is_staff = self.cleaned_data['is_staff']
        if not User.objects.filter(email=email):
            if is_staff:
                raise forms.ValidationError('该邮箱还没有在本站注册。')
        else:
            if not is_staff:
                raise forms.ValidationError('该邮箱已经在本站注册。')
        return email

    def get_user(self, email=None):
        """函数功能.
            根据邮箱获取用户名
        Args:
            self (object): 表单实例
            email: 邮箱，默认self.cleaned_data['email']

        Returns:
            verify: str
        """
        email = email or self.cleaned_data['email']
        auth_user = User.objects.filter(email=email)
        if auth_user:
            return auth_user[0]
        else:
            from django.contrib.auth.models import AnonymousUser
            return AnonymousUser

    def set_cache(self, key, value, timeout):
        """函数功能.
            设置缓存
        Args:
            self (object): 表单实例
            key: 缓存键
            value: 缓存键值
            timeout: 过期时间

        Returns:
            dict: {key: value}
        """
        cache.set(key, value, timeout)
        return {key: value}

    def send_email(self, subject, to_email=None, from_email=None, message=None, html_message=None, **kwargs):
        """函数功能.
            发送邮件
        Args:
            self (object): 表单实例
            subject: 邮件主题
            to_email: 收件人
            from_email: 发件人
            message: 消息主题
            html_message: html格式消息
            kwargs: 其他参数

        Returns:
            Boolean: 是否发送成功
        """
        from_email = from_email or settings.EMAIL_HOST_USER
        try:
            to_email = to_email or self.cleaned_data['email']
            mail.send_mail(subject=subject, message=message, from_email=from_email,
                           recipient_list=[to_email], html_message=html_message, **kwargs)
            return True
        except:
            return False
