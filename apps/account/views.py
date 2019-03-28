from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from .forms import LoginForm


# Create your views here.

def AccountLoginView(request):
    if request.method == 'GET':
        account_form = LoginForm()
        return render(request, 'admin/login.html',
                      {'form': account_form, 'title': '用户登录', 'site_title': '用户管理', 'site_header': '账号登录'})
    account_form = LoginForm(request.POST)
    if account_form.is_valid():
        account_info = account_form.cleaned_data
        user = authenticate(username=account_info.get('username', ''), password=account_info.get('password', ''))
        if user:
            login(request, user)
            return HttpResponse(user)

        return render(request, 'admin/login.html',
                      {'form': account_form, 'title': '用户登录', 'site_title': '用户管理', 'site_header': '账号登录'})
        return render(request, 'admin/login.html',
                      {'form': account_form, 'title': '用户登录', 'site_title': '用户管理', 'site_header': '账号登录'})
