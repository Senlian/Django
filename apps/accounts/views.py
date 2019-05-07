from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.http.response import JsonResponse, HttpResponse, HttpResponseRedirect
from django.contrib.auth import views as auth_views

from .forms import AccountsLoginForm, AccountRegisterForm


# Create your views here.
class AccountsFormMixin:
    def form_valid(self, form):
        # 表单验证通过，用户登录
        auth_login(self.request, form.get_user())
        success_url = self.get_success_url()
        return JsonResponse({'success_url': success_url})


class LoginView(AccountsFormMixin, auth_views.LoginView):
    # 模板
    template_name = 'accounts/login.html'
    # 模板表单
    form_class = AccountsLoginForm
    # 表单渲染数据=form+extra_context
    extra_context = {'title': '登录', 'site_header': '用户名密码登录'}
    redirect_field_name = reverse_lazy('blog:index')


class RegisterView(auth_views.FormView):
    # 模板
    template_name = 'accounts/register.html'
    # 模板表单
    form_class = AccountRegisterForm
    # 表单渲染数据=form+extra_context
    extra_context = {'title': '注册', 'site_header': '账号注册'}
    redirect_field_name = reverse_lazy('blog:index')

