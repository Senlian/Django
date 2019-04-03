from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core import mail
from django.conf import settings

import random, string

from .forms import AccountLoginForm, AccountRegisterForm, AccountEmailForm


# Create your views here.
@method_decorator(csrf_exempt, name='POST')
def AccountLoginView(request):
    is_login = False
    if request.method == 'GET':
        # if request.user.is_authenticated:
        #     return redirect('article:index')
        account_login_form = AccountLoginForm()
        return render(request, 'account/login.html',
                      {'form': account_login_form, 'title': '登录', 'site_title': '用户管理', 'site_header': '账号登录'})
    else:
        account_login_form = AccountLoginForm(request.POST)
        if account_login_form.is_valid():
            account_info = account_login_form.cleaned_data
            # 账户验证
            account = authenticate(username=account_info.get('username', ''), password=account_info.get('password', ''))
            if account and account.is_active:
                # 内置方法登陆，该方法会在数据库存储django_session表中
                login(request, account)
                is_login = account.is_active
            else:
                account_login_form.errors.update({'password': ['密码错误']})
        account_login_form.errors.update({'is_login': is_login})
        return JsonResponse(account_login_form.errors)
        # return render(request, 'account/login.html',{'form': account_login_form, 'title': '登录', 'site_title': '用户管理', 'site_header': '账号登录'})


@login_required(login_url=reverse_lazy('account:login'))
def AccountLogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('article:index')


def AccountRegisterView(request):
    is_register = False
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('article:index')
        account_register_form = AccountRegisterForm()
        return render(request, 'account/register.html',
                      {'form': account_register_form, 'title': '注册', 'site_title': '用户管理', 'site_header': '账号注册'})
    else:
        account_register_form = AccountRegisterForm(request.POST)
        if account_register_form.is_valid():
            new_user = account_register_form.save(commit=False)
            new_user.set_password(account_register_form.cleaned_data['password'])
            new_user.save()
            account_register_form.save_m2m()
            login(request, new_user)
            is_register = True

    account_register_form.errors.update({'is_register': is_register})
    return JsonResponse(account_register_form.errors)


@require_POST
def AccountEmailVerifyView(request):
    email_verify = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
    cache.set('email_verify', email_verify, 30)
    is_send = True
    account_email_form = AccountEmailForm(request.POST)
    if account_email_form.is_valid():
        email_to = account_email_form.cleaned_data['email']
        try:
            mail.send_mail('注册验证码通知',
                           '您正在本站进行注册，验证码为 {0}, 如非本人操作请忽略。'.format(email_verify),
                           settings.DEFAULT_FROM_EMAIL,
                           [email_to.strip()],
                           fail_silently=True, )

        except Exception as e:
            account_email_form.errors.update({'email_verify': ["验证码发送失败"]})
        finally:
            account_email_form.errors.update({'is_send': is_send})
    return JsonResponse(account_email_form.errors)
