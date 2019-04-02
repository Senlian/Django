from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy, reverse
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from .forms import AccountLoginForm, AccountRegisterForm


# Create your views here.
@csrf_exempt
def AccountLoginView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('article:index')
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
                return JsonResponse({'is_login':'ok'})
            else:
                account_login_form.errors.update({'password': '密码错误'})

        return render(request, 'account/login.html',
                      {'form': account_login_form, 'title': '登录', 'site_title': '用户管理', 'site_header': '账号登录'})


@login_required(login_url=reverse_lazy('account:login'))
def AccountLogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('article:index')


def AccountRegisterView(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('article:index')
        account_register_form = AccountRegisterForm()
        return render(request, 'account/register.html',
                      {'form': account_register_form, 'title': '注册', 'site_title': '用户管理', 'site_header': '账号注册'})
    else:
        account_register_form = AccountRegisterForm(request.POST)
    return redirect('article:index')
