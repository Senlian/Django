from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect, requires_csrf_token
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_deny, xframe_options_sameorigin
from django.contrib.auth.models import User
from django.core.cache import cache
from django.core import mail
from django.conf import settings
from django.views import View
import random, string, json

from .forms import AccountLoginForm, AccountRegisterForm, AccountEmailForm
from common.views import CreateVerifyView


# Create your views here.
@method_decorator(csrf_exempt, name='POST')
@xframe_options_sameorigin
def AccountLoginView(request):
    """函数功能.

    函数功能说明.

    Args:
        request (int): arg1的参数说明

    Returns:
        render: 返回值说明

    """
    if request.user.is_authenticated or not request.META.get('HTTP_REFERER', ''):
        return redirect('blog:index')

    is_login = False
    if request.method == 'GET':
        CreateVerifyView(request)
        account_login_form = AccountLoginForm()
        return render(request, 'account/login.html',
                      {'form': account_login_form, 'title': '登录', 'site_title': '用户管理', 'site_header': '账号登录'})
    else:
        account_login_form = AccountLoginForm(request.POST)
        if account_login_form.is_valid():
            account_info = account_login_form.cleaned_data
            # 账户验证
            username = account_info.get('username', '')
            password = account_info.get('password', '')
            remember = eval(account_info.get('remember', False))

            account = authenticate(username=username, password=password)
            verify_code = request.session.get('verify', None).lower()
            verify_in = request.POST.get('verify', None).lower()
            if account and account.is_active:
                # 内置方法登陆，该方法会在数据库存储django_session表中
                if not verify_in:
                    account_login_form.errors.update({'verify': ['请输入验证码']})
                elif verify_in != verify_code:
                    CreateVerifyView(request)
                    account_login_form.errors.update({'verify': ['验证码错误']})
                else:
                    login(request, account)
                    is_login = account.is_active
            else:
                CreateVerifyView(request)
                account_login_form.errors.update({'password': ['密码错误']})

        account_login_form.errors.update({'is_login': is_login})
        response = JsonResponse(account_login_form.errors)

        # response.set_cookie('username', account_info.get('username', ''))
        return response
        # return render(request, 'account/login.html',{'form': account_login_form, 'title': '登录', 'site_title': '用户管理', 'site_header': '账号登录'})


@login_required(login_url=reverse_lazy('account:login'))
def AccountLogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('blog:index')


def AccountRegisterView(request):
    if request.user.is_authenticated or not request.META.get('HTTP_REFERER', ''):
        return redirect('blog:index')
    is_register = False
    if request.method == 'GET':
        # if request.user.is_authenticated:
        #     return redirect('blog:index')
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
    title = '注册验证码通知'
    email_verify = ''.join(random.sample(string.ascii_lowercase + string.digits, 6))
    content = '您正在本站进行注册，验证码为 {0}, 如非本人操作请忽略。'.format(email_verify)
    email_from = settings.DEFAULT_FROM_EMAIL
    TIMER = 30
    is_send = False

    account_email_form = AccountEmailForm(request.POST)

    if account_email_form.is_valid():
        email_to = account_email_form.cleaned_data['email']
        cache.set('email_verify_{0}'.format(email_to.split('@')[0]), email_verify, TIMER)
        try:
            mail.send_mail(title,
                           content,
                           email_from,
                           [email_to.strip()],
                           fail_silently=True, )
            is_send = True
        except Exception as e:
            account_email_form.errors.update({'email_verify': ["验证码发送失败"]})
        finally:
            account_email_form.errors.update({'is_send': is_send, 'timer': TIMER})
    return JsonResponse(account_email_form.errors)


def AccountSendResetEmailView(request):
    TIMER = 30
    is_send = False
    if request.method == 'GET':
        account_email_form = AccountEmailForm()
        return render(request, 'account/password_reset_email.html', {'form': account_email_form})
    else:
        account_email_form = AccountEmailForm(request.POST)
        if account_email_form.is_valid():
            title = '密码重置'
            email_from = settings.DEFAULT_FROM_EMAIL
            email_to = account_email_form.cleaned_data['email']
            content = '你正在请求重置密码'
            try:
                mail.send_mail(title,
                               content,
                               email_from,
                               [email_to.strip()],
                               fail_silently=True, )
                is_send = True
            except Exception as e:
                account_email_form.errors.update({'email': ["邮件发送失败"]})
            finally:
                account_email_form.errors.update({'is_send': is_send, 'timer': TIMER})
    return JsonResponse(account_email_form.errors)


class AccountPasswordRestView(View):
    def get(self, request):
        return render(request, 'account/password_reset.html', {'title': '密码', 'site_title': '用户管理', 'site_header': '密码重置'})

    def post(self, request):
        return HttpResponse('reset post')
